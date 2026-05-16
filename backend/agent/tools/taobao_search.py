"""
淘宝商品搜索工具 (用户视角)

直接抓取 s.taobao.com 搜索结果页，提取商品信息。
不走淘宝开放平台API（API以店铺为中心），走买家搜索视角。

依赖: playwright (需先安装 playwright install chromium)
"""

from typing import Optional
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout


def search_taobao(
    keyword: str,
    page_num: int = 1,
    timeout: int = 20000,
    headless: bool = True,
) -> dict:
    """
    搜索淘宝商品

    Args:
        keyword:  搜索关键词，如 "帽子", "登山鞋", "帐篷"
        page_num: 页码，从1开始
        timeout:  页面加载超时(毫秒)
        headless: 是否无头模式

    Returns:
        {
            "success": bool,
            "data": {
                "keyword": str,
                "page": int,
                "total_pages": int | None,
                "items": [
                    {
                        "title": str,
                        "price": str,
                        "sales": str,
                        "location": str,
                        "tags": [str],
                        "shop_name": str,
                        "shop_url": str,
                        "item_url": str,
                    }
                ]
            },
            "error": str | None
        }
    """
    url = f"https://s.taobao.com/search?q={keyword}&s={(page_num - 1) * 44}"

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            locale="zh-CN",
        )
        page = context.new_page()

        try:
            page.goto(url, timeout=timeout, wait_until="domcontentloaded")

            # 关闭可能弹出的登录窗口
            try:
                page.keyboard.press("Escape")
                page.wait_for_timeout(1500)
            except Exception:
                pass

            # 等待搜索结果加载
            try:
                page.wait_for_selector('[data-name="item"]', timeout=timeout)
            except PwTimeout:
                # 可能被反爬或需要登录，返回错误
                return {
                    "success": False,
                    "data": None,
                    "error": "搜索结果未加载，可能需要登录或遇到反爬验证"
                }

            # 提取商品列表
            items = page.eval_on_selector_all(
                '[data-name="item"]',
                """(elements) => {
                    return elements.map(el => {
                        // 商品链接
                        const link = el.querySelector('a[href*="item.taobao.com"], a[href*="detail.tmall.com"]');
                        const href = link ? link.href : '';

                        // 商品标题
                        const titleEl = el.querySelector('[class*="Title"], [class*="title"]');
                        const title = titleEl ? titleEl.textContent.trim() : '';

                        // 价格
                        const priceEl = el.querySelector('[class*="Price"], [class*="price"], em');
                        const price = priceEl ? priceEl.textContent.trim() : '';

                        // 销量
                        const salesEl = el.querySelector('[class*="Sales"], [class*="sales"], [class*="deal"]');
                        const sales = salesEl ? salesEl.textContent.trim() : '';

                        // 地区
                        const locEl = el.querySelector('[class*="Location"], [class*="location"]');
                        const location = locEl ? locEl.textContent.trim() : '';

                        // 店铺链接
                        const shopEl = el.querySelector('a[href*="store.taobao.com"], a[href*="shop/view_shop"]');
                        const shopUrl = shopEl ? shopEl.href : '';

                        // 店铺名
                        const shopNameEl = el.querySelector('[class*="ShopName"], [class*="shopName"], [class*="seller"]');
                        const shopName = shopNameEl ? shopNameEl.textContent.trim() : '';

                        // 标签
                        const tagEls = el.querySelectorAll('[class*="Tag"], [class*="tag"], [class*="icon-service"]');
                        const tags = Array.from(tagEls).map(t => t.textContent.trim()).filter(Boolean);

                        return {
                            title: title,
                            price: price,
                            sales: sales,
                            location: location,
                            tags: tags,
                            shop_name: shopName,
                            shop_url: shopUrl,
                            item_url: href
                        };
                    });
                }"""
            )

            # 尝试获取总页数
            total_pages: Optional[int] = None
            try:
                page_info = page.eval_on_selector(
                    '[class*="pagination"], [class*="Pagination"], [class*="page"]',
                    "(el) => el.textContent"
                )
                if page_info and "100" in page_info:
                    total_pages = 100
            except Exception:
                pass

            # 过滤掉空标题的无效条目
            valid_items = [it for it in items if it["title"]]

            return {
                "success": True,
                "data": {
                    "keyword": keyword,
                    "page": page_num,
                    "total_pages": total_pages,
                    "items": valid_items,
                },
                "error": None,
            }

        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
            }
        finally:
            browser.close()


# --- 命令行入口: python taobao_search.py 帽子 ---
if __name__ == "__main__":
    import sys
    import json

    kw = sys.argv[1] if len(sys.argv) > 1 else "帽子"
    pg = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    result = search_taobao(kw, page_num=pg, headless=False)
    print(json.dumps(result, ensure_ascii=False, indent=2))
