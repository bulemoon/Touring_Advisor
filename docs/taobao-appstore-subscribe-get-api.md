# 淘宝开放平台 API 文档

> 来源: https://open.taobao.com/api.htm?docId=285&docType=2
> 抓取时间: 2026-05-16
> 当前分类: **用户API**（共 442 个API分组，6849 个API）

---

## 一、API 目录总览（用户API）

本分类包含 **442** 个API分组，**6849** 个API接口。

### 淘宝交易API (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.trades.sold.get` |
| 2 | `taobao.trade.memo.add` |
| 3 | `taobao.trade.memo.update` |
| 4 | `taobao.trade.fullinfo.get` |
| 5 | `taobao.trade.close` |
| 6 | `taobao.trades.sold.increment.get` |
| 7 | `taobao.trade.confirmfee.get` |
| 8 | `taobao.trade.ordersku.update` |
| 9 | `taobao.trade.shippingaddress.update` |
| 10 | `taobao.trade.amount.get` |
| 11 | `taobao.trade.receivetime.delay` |
| 12 | `taobao.trade.postage.update` |
| 13 | `taobao.trades.sold.incrementv.get` |
| 14 | `taobao.trades.sold.query` |
| 15 | `taobao.top.oaid.merge` |
| 16 | `taobao.top.once.token.get` |
| 17 | `taobao.trade.invoice.amount.get` |
| 18 | `taobao.top.secret.extend` |
| 19 | `taobao.fulfillment.order.assemble` |
| 20 | `taobao.top.secret.bill.detail` |
| 21 | `taobao.trade.sellermemos.get` |
| 22 | `taobao.trade.sellerflags.get` |
| 23 | `taobao.trade.invoice.summary.get` |
| 24 | `taobao.trade.support.refund.open` |
| 25 | `taobao.ofn.subsidy.difference.refund.query` |
| 26 | `taobao.ofn.subsidy.difference.refund.cancel` |
| 27 | `taobao.ofn.subsidy.difference.refund.apply` |

</details>

### 淘宝用户API

| # | API名称 |
|---|--------|
| 1 | `taobao.user.buyer.get` |
| 2 | `taobao.user.seller.get` |
| 3 | `taobao.user.avatar.get` |
| 4 | `taobao.user.openuid.getbynick` |

### 淘宝商品API (71 APIs)

<details>
<summary>展开查看全部 71 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.items.onsale.get` |
| 2 | `taobao.item.img.upload` |
| 3 | `taobao.item.img.delete` |
| 4 | `taobao.item.propimg.delete` |
| 5 | `taobao.item.propimg.upload` |
| 6 | `taobao.item.sku.add` |
| 7 | `taobao.item.sku.get` |
| 8 | `taobao.item.sku.update` |
| 9 | `taobao.item.skus.get` |
| 10 | `taobao.item.update.delisting` |
| 11 | `taobao.item.update.listing` |
| 12 | `taobao.item.delete` |
| 13 | `taobao.item.joint.img` |
| 14 | `taobao.item.joint.propimg` |
| 15 | `taobao.items.inventory.get` |
| 16 | `taobao.items.custom.get` |
| 17 | `taobao.skus.custom.get` |
| 18 | `taobao.item.sku.delete` |
| 19 | `taobao.item.quantity.update` |
| 20 | `taobao.item.templates.get` |
| 21 | `taobao.item.sku.price.update` |
| 22 | `taobao.skus.quantity.update` |
| 23 | `taobao.item.anchor.get` |
| 24 | `tmall.item.desc.modules.get` |
| 25 | `taobao.item.barcode.update` |
| 26 | `tmall.item.schema.add` |
| 27 | `tmall.product.add.schema.get` |
| 28 | `tmall.product.match.schema.get` |
| 29 | `tmall.product.schema.match` |
| 30 | `tmall.product.schema.add` |
| 31 | `tmall.product.update.schema.get` |
| 32 | `tmall.product.schema.update` |
| 33 | `tmall.item.schema.update` |
| 34 | `tmall.item.update.schema.get` |
| 35 | `tmall.product.schema.get` |
| 36 | `tmall.item.increment.update.schema.get` |
| 37 | `tmall.item.schema.increment.update` |
| 38 | `tmall.item.price.update` |
| 39 | `taobao.item.seller.get` |
| 40 | `taobao.items.seller.list.get` |
| 41 | `tmall.item.outerid.update` |
| 42 | `tmall.item.shiptime.update` |
| 43 | `tmall.item.simpleschema.add` |
| 44 | `tmall.item.add.simpleschema.get` |
| 45 | `tmall.item.simpleschema.update` |
| 46 | `tmall.item.quantity.update` |
| 47 | `tmall.item.calculate.hscode.get` |
| 48 | `tmall.item.combine.get` |
| 49 | `tmall.item.hscode.detail.get` |
| 50 | `taobao.item.update.listing.tmall` |
| 51 | `taobao.item.update.delisting.tmall` |
| 52 | `tmall.item.hscode.audit.results.query` |
| 53 | `taobao.item.promotion.rule.get` |
| 54 | `alibaba.item.publish.schema.get` |
| 55 | `alibaba.item.publish.submit` |
| 56 | `alibaba.item.edit.schema.get` |
| 57 | `alibaba.item.edit.submit` |
| 58 | `alibaba.item.operate.delete` |
| 59 | `alibaba.item.operate.downshelf` |
| 60 | `alibaba.item.operate.upshelf` |
| 61 | `alibaba.item.publish.props.get` |
| 62 | `alibaba.item.edit.fastupdate` |
| 63 | `alibaba.item.publish.market.get` |
| 64 | `tmall.item.apple.shiptime.update` |
| 65 | `taobao.sku.update.listing.tmall` |
| 66 | `alibaba.item.publish.distribute.submit` |
| 67 | `alibaba.item.publish.props.distribute.get` |
| 68 | `alibaba.item.publish.schema.distribute.get` |
| 69 | `alibaba.item.publish.props.omnichannel.get` |
| 70 | `alibaba.item.publish.omnichannel.submit` |
| 71 | `alibaba.item.publish.schema.omnichannel.get` |

</details>

### 淘宝物流API (33 APIs)

<details>
<summary>展开查看全部 33 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.areas.get` |
| 2 | `taobao.logistics.companies.get` |
| 3 | `taobao.logistics.orders.detail.get` |
| 4 | `taobao.logistics.orders.get` |
| 5 | `taobao.logistics.partners.get` |
| 6 | `taobao.logistics.trace.search` |
| 7 | `taobao.logistics.online.send` |
| 8 | `taobao.logistics.online.cancel` |
| 9 | `taobao.logistics.online.confirm` |
| 10 | `taobao.logistics.dummy.send` |
| 11 | `taobao.delivery.template.get` |
| 12 | `taobao.delivery.templates.get` |
| 13 | `taobao.delivery.template.delete` |
| 14 | `taobao.delivery.template.add` |
| 15 | `taobao.delivery.template.update` |
| 16 | `taobao.logistics.consign.order.createandsend` |
| 17 | `taobao.wlb.stores.baseinfo.get` |
| 18 | `taobao.wlb.order.jz.query` |
| 19 | `taobao.wlb.order.jz.consign` |
| 20 | `alibaba.ascp.logistics.offline.send` |
| 21 | `alibaba.ascp.logistics.consign.resend` |
| 22 | `taobao.logistics.instant.trace.search` |
| 23 | `alibaba.ascp.logistics.seller.writeoff` |
| 24 | `alibaba.ascp.logistics.seller.send` |
| 25 | `alibaba.ascp.logistics.seller.orders.get` |
| 26 | `taobao.logistics.trace.get` |
| 27 | `alibaba.ascp.logistics.consign.modify` |
| 28 | `alibaba.ascp.logistics.seller.writelogisticsnode` |
| 29 | `taobao.logistics.express.bill.sum.sync` |
| 30 | `taobao.logistics.fulfilorder.search` |
| 31 | `taobao.logistics.reverseorder.erp.search` |
| 32 | `taobao.logistics.returnorder.svc.search` |
| 33 | `alibaba.logistics.mail.order.delivery.preference.add` |

</details>

### 淘宝退款API (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.refunds.apply.get` |
| 2 | `taobao.refunds.receive.get` |
| 3 | `taobao.refund.get` |
| 4 | `taobao.refund.messages.get` |
| 5 | `taobao.refund.message.add` |
| 6 | `taobao.refund.refuse` |
| 7 | `taobao.rp.refunds.agree` |
| 8 | `taobao.rp.returngoods.agree` |
| 9 | `taobao.rp.refund.review` |
| 10 | `taobao.rp.returngoods.refill` |
| 11 | `taobao.rp.returngoods.refuse` |
| 12 | `taobao.refund.refusereason.get` |
| 13 | `tmall.dispute.receive.get` |
| 14 | `taobao.special.refund.get` |
| 15 | `taobao.special.refunds.receive.get` |
| 16 | `taobao.refund.status.get` |
| 17 | `taobao.rp.refund.intercept` |
| 18 | `taobao.refund.negotiatereturn` |
| 19 | `taobao.refund.negotiatereturn.render` |
| 20 | `taobao.refund.detail.get` |
| 21 | `taobao.refund.negotiate.canapply` |
| 22 | `taobao.refund.smart.deliveryintercept.feedback` |
| 23 | `taobao.refund.smart.support.negotiationtypes.get` |
| 24 | `taobao.refund.smart.negotiation.status.get` |
| 25 | `taobao.refund.smart.negotiation.submit` |
| 26 | `taobao.refund.dispute.seller.proof.strategy` |
| 27 | `taobao.refund.negotiate.validate` |

</details>

### 用户API (31 APIs)

<details>
<summary>展开查看全部 31 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.appstore.subscribe.get` |
| 2 | `taobao.opensecurity.uid.get` |
| 3 | `taobao.open.account.delete` |
| 4 | `taobao.open.account.update` |
| 5 | `taobao.open.account.create` |
| 6 | `taobao.open.account.list` |
| 7 | `account.aliyuncs.com.GetPubKey.2013-07-01` |
| 8 | `taobao.open.account.search` |
| 9 | `taobao.open.account.token.apply` |
| 10 | `alibaba.aliqin.flow.wallet.check.balance` |
| 11 | `tmall.service.settleadjustment.modify` |
| 12 | `taobao.alitrip.flightchange.add` |
| 13 | `taobao.rdc.aligenius.account.validate` |
| 14 | `taobao.messageaccount.messsage.reply` |
| 15 | `taobao.miniapp.userInfo.get` |
| 16 | `alibaba.ailabs.user.speech.guide` |
| 17 | `taobao.koubei.tribe.open.verify.code.apply` |
| 18 | `taobao.koubei.tribe.open.user.query` |
| 19 | `alibaba.beneift.draw` |
| 20 | `alibaba.benefit.send` |
| 21 | `taobao.miniapp.user.phone.get` |
| 22 | `taobao.newretail.division.record.list.get` |
| 23 | `taobao.lark.pos.itemprod.findterminal` |
| 24 | `alibaba.lsy.miniapp.user.get` |
| 25 | `taobao.miniapp.eleuser.phone.get` |
| 26 | `taobao.miniapp.eleuserinfo.get` |
| 27 | `alibaba.seller.vendor.write.client` |
| 28 | `taobao.user.openid.get` |
| 29 | `alibaba.databank.open.oneservice.dataready` |
| 30 | `alibaba.databank.open.oneservice.getdata` |
| 31 | `taobao.miniapp.user.phone.get.server` |

</details>

### 类目API

| # | API名称 |
|---|--------|
| 1 | `taobao.itemcats.get` |
| 2 | `taobao.itemcats.authorize.get` |
| 3 | `aliexpress.social.discategory.get` |
| 4 | `alibaba.imap.pv.autofill` |
| 5 | `alibaba.imap.category.predict` |
| 6 | `alibaba.imap.fixedmapping.query` |
| 7 | `taobao.item.catprops.modification.get` |

### 商品API (85 APIs)

<details>
<summary>展开查看全部 85 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.product.get` |
| 2 | `taobao.products.search` |
| 3 | `taobao.product.add` |
| 4 | `taobao.product.img.upload` |
| 5 | `taobao.product.propimg.upload` |
| 6 | `taobao.product.update` |
| 7 | `taobao.products.get` |
| 8 | `taobao.aftersale.get` |
| 9 | `taobao.ump.promotion.get` |
| 10 | `tmall.product.specs.get` |
| 11 | `tmall.product.spec.pic.upload` |
| 12 | `tmall.product.spec.get` |
| 13 | `tmall.product.spec.add` |
| 14 | `tmall.product.specs.ticket.get` |
| 15 | `tmall.product.template.get` |
| 16 | `tmall.item.add.schema.get` |
| 17 | `tmall.item.sizemapping.templates.list` |
| 18 | `tmall.item.sizemapping.template.get` |
| 19 | `tmall.item.sizemapping.template.delete` |
| 20 | `tmall.item.sizemapping.template.update` |
| 21 | `tmall.item.sizemapping.template.create` |
| 22 | `taobao.item.qualification.display.get` |
| 23 | `tmall.item.vip.schema.add` |
| 24 | `tmall.item.vip.schema.update` |
| 25 | `tmall.item.vip.add.schema.get` |
| 26 | `tmall.item.vip.update.schema.get` |
| 27 | `tmall.item.update.simpleschema.get` |
| 28 | `tmall.item.dapei.template.query` |
| 29 | `taobao.baike.import.zhubao.picture` |
| 30 | `taobao.baike.import.zhubao.data` |
| 31 | `alibaba.gpu.add.schema.get` |
| 32 | `alibaba.gpu.schema.add` |
| 33 | `alibaba.gpu.update.schema.get` |
| 34 | `alibaba.gpu.schema.update` |
| 35 | `alibaba.gpu.schema.catsearch` |
| 36 | `taobao.item.carturl.get` |
| 37 | `aliexpress.social.item.promotion` |
| 38 | `aliexpress.social.item.search` |
| 39 | `aliexpress.social.item.ranking` |
| 40 | `taobao.miniapp.items.get` |
| 41 | `cainiao.cntec.item.change.message` |
| 42 | `taobao.banamadpc.item.add` |
| 43 | `taobao.banamadpc.item.update` |
| 44 | `taobao.banamadpc.item.select.prop` |
| 45 | `taobao.banamadpc.item.edit.render` |
| 46 | `taobao.banamadpc.item.render` |
| 47 | `tmall.item.store.update.schema.get` |
| 48 | `tmall.item.store.schema.update` |
| 49 | `alibaba.gsp.supply.image.upload` |
| 50 | `alitrip.travel.elements.search` |
| 51 | `alibaba.jym.industry.information.callbak` |
| 52 | `alibaba.jym.item.external.goods.batch.modifyprice` |
| 53 | `alibaba.jym.item.external.goods.batch.onsale` |
| 54 | `alibaba.jym.item.external.goods.batchtask.query` |
| 55 | `alibaba.jym.item.external.goods.detail.query` |
| 56 | `alibaba.jym.item.external.goods.status.batch.query` |
| 57 | `alibaba.jym.item.external.goods.batch.offsale` |
| 58 | `alibaba.jym.item.external.goods.batch.publish` |
| 59 | `tmall.item.sku.status.get` |
| 60 | `tmall.item.sku.status.update` |
| 61 | `tmall.item.sku.sort.get` |
| 62 | `tmall.item.sku.sort.update` |
| 63 | `tmall.item.sku.new.get` |
| 64 | `tmall.item.sku.new.update` |
| 65 | `taobao.ump.promotion.sku.get` |
| 66 | `tmall.item.setscombines.edit` |
| 67 | `alibaba.jym.item.property.def.query` |
| 68 | `alibaba.jym.item.game.sever.query` |
| 69 | `alibaba.jym.item.external.goods.batch.delete` |
| 70 | `tmall.item.series.itemseries.insertorupdate` |
| 71 | `tmall.item.series.itemseries.insertseriesitem` |
| 72 | `tmall.item.series.itemseries.removeitemfromseries` |
| 73 | `cainiao.cntec.supplier.product.update` |
| 74 | `alibaba.xsd.item.query` |
| 75 | `alibaba.xsd.item.store.save` |
| 76 | `alibaba.xsd.item.save` |
| 77 | `alibaba.xsd.item.store.scroll.query` |
| 78 | `tmall.item.origin.async` |
| 79 | `taobao.item.origin.async` |
| 80 | `taobao.item.omnichannel.origin.async` |
| 81 | `tmall.item.omnichannel.origin.async` |
| 82 | `alibaba.gpu.schema.catbrand.get` |
| 83 | `alibaba.xsd.item.channel.status` |
| 84 | `alibaba.xsd.item.nr.bind` |
| 85 | `alibaba.xsd.item.nr.price` |

</details>

### 交易API (51 APIs)

<details>
<summary>展开查看全部 51 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.trade.get` |
| 2 | `taobao.trade.wtvertical.get` |
| 3 | `taobao.trade.voucher.upload` |
| 4 | `alibaba.trade.aliance.create` |
| 5 | `alibaba.wdk.trade.order.query` |
| 6 | `alibaba.wdk.trade.order.create` |
| 7 | `alibaba.wdk.trade.order.cancel` |
| 8 | `alibaba.wdk.trade.refund.create` |
| 9 | `alibaba.wdk.trade.refund.query` |
| 10 | `alibaba.wdk.trade.refund.inform` |
| 11 | `cainiao.refund.refundactions.display` |
| 12 | `cainiao.refund.refundactions.get` |
| 13 | `cainiao.refund.refundactions.judgement` |
| 14 | `alibaba.wdk.pos.trade.create` |
| 15 | `alibaba.wdk.pos.trade.query` |
| 16 | `alibaba.wdk.pos.trade.reverse` |
| 17 | `alibaba.wdk.trade.discount.bill.get` |
| 18 | `taobao.open.trades.sold.get` |
| 19 | `taobao.open.trade.get` |
| 20 | `taobao.koubei.tribe.open.order.page` |
| 21 | `alitrip.rail.trade.refund` |
| 22 | `alibaba.lst.vas.tradeflow.save` |
| 23 | `taobao.xhotel.distribution.order.detail.search` |
| 24 | `aliexpress.payment.exchange.get` |
| 25 | `cainiao.cntec.supplier.order.service` |
| 26 | `taobao.opentrade.customization.refund.enable` |
| 27 | `taobao.life.reservation.trade.consume.notice` |
| 28 | `taobao.life.reservation.item.order.confirm` |
| 29 | `taobao.life.reservation.item.order.change` |
| 30 | `taobao.wtt.trade.service.get` |
| 31 | `taobao.trade.simple.get` |
| 32 | `taobao.trades.simple.sold.get` |
| 33 | `taobao.trades.simple.sold.increment.get` |
| 34 | `taobao.trades.sold.history.get` |
| 35 | `taobao.servindustry.finance.geex.order.update` |
| 36 | `taobao.servindustry.finance.geex.order.loan` |
| 37 | `taobao.servindustry.finance.insurance.agreement.sign` |
| 38 | `alibaba.jym.fulfillment.ioscharge.callback` |
| 39 | `alibaba.jym.fulfillment.card.callback` |
| 40 | `alibaba.alicom.trade.advertiseinfo.get` |
| 41 | `taobao.ofn.self.recycle.auth` |
| 42 | `taobao.ofn.spu.inspection.report` |
| 43 | `taobao.ofn.recycle.order.detail` |
| 44 | `taobao.ofn.recycle.order.fulfillment` |
| 45 | `taobao.security.order.risk.level.search` |
| 46 | `alibaba.jym.insurance.picc.claim.callback` |
| 47 | `taobao.opentrade.customization.oss.get` |
| 48 | `taobao.opentrade.customization.file.update` |
| 49 | `taobao.opentrade.customization.file.get` |
| 50 | `taobao.open.trades.sold.increment.get` |
| 51 | `taobao.shangou.trades.sold.get` |

</details>

### 评价API

| # | API名称 |
|---|--------|
| 1 | `taobao.traderates.get` |
| 2 | `taobao.traderate.add` |
| 3 | `taobao.traderate.list.add` |
| 4 | `taobao.traderate.explain.add` |
| 5 | `tmall.traderate.feeds.get` |
| 6 | `tmall.traderate.itemtags.get` |
| 7 | `taobao.fliggy.wrate.getmixratelist` |

### 物流API (73 APIs)

<details>
<summary>展开查看全部 73 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.logistics.address.search` |
| 2 | `taobao.logistics.address.remove` |
| 3 | `taobao.logistics.address.modify` |
| 4 | `taobao.logistics.address.add` |
| 5 | `taobao.logistics.consign.resend` |
| 6 | `taobao.wms.order.warehouse.route.get` |
| 7 | `cainiao.cloudprint.crashinfos.put` |
| 8 | `cainiao.cboss.workplatform.biztype.querybyid` |
| 9 | `cainiao.cboss.workplatform.logistics.iscainiaoorder` |
| 10 | `cainiao.member.courier.cpresign` |
| 11 | `taobao.nextone.logistics.sign.update` |
| 12 | `taobao.nextone.logistics.warehouse.update` |
| 13 | `alibaba.alink.message.history.action` |
| 14 | `taobao.wlb.import.threepl.resource.get` |
| 15 | `taobao.wlb.import.threepl.offline.consign` |
| 16 | `aliexpress.logistics.createwarehouseorder` |
| 17 | `taobao.logistics.express.modify.appoint` |
| 18 | `taobao.rdc.aligenius.warehouse.resend.logistics.msg.post` |
| 19 | `taobao.rdc.aligenius.warehouse.resend.update` |
| 20 | `alibaba.ele.fengniao.trade.update` |
| 21 | `alibaba.ele.fengniao.cancel.merchant` |
| 22 | `alibaba.ele.fengniao.order.push` |
| 23 | `alibaba.ele.fengniao.chainstore.sign.contract` |
| 24 | `alibaba.ele.fengniao.order.query` |
| 25 | `alibaba.ele.fengniao.shippingorder.event` |
| 26 | `alibaba.ele.fengniao.carrierdriver.location` |
| 27 | `alibaba.ele.fengniao.service.package.query` |
| 28 | `alibaba.ele.fengniao.chainstore.ranges` |
| 29 | `alibaba.ele.fengniao.chainstore.contract.cancel` |
| 30 | `alibaba.ele.fengniao.chainstore.contract.change` |
| 31 | `alibaba.ele.fengniao.chainstore.update` |
| 32 | `alibaba.ele.fengniao.merchant.contract.cancel` |
| 33 | `taobao.rdc.aligenius.warehouse.reverse.event.update` |
| 34 | `taobao.rdc.aligenius.warehouse.reverse.uploading` |
| 35 | `alibaba.ele.fengniao.carrier.capacity.query` |
| 36 | `taobao.rdc.aligenius.logistics.packages.notice` |
| 37 | `cainiao.data.logistics.cp.delivery.aging.predict` |
| 38 | `cainiao.data.logistics.delivery.aging.predict` |
| 39 | `cainiao.reachable.batchjudge` |
| 40 | `wdk.logistic.network.warehouse.resource.relation.query.to.codes` |
| 41 | `wdk.logistic.network.resource.group.query` |
| 42 | `wdk.logistic.network.warehouse.delivery.relation.query` |
| 43 | `wdk.logistic.network.warehouse.resource.relation.query.from` |
| 44 | `alibaba.tcls.fulfill.qa.order.create` |
| 45 | `taobao.open.seller.biz.logistic.time.rule` |
| 46 | `taobao.open.seller.biz.logistic.seller.bind` |
| 47 | `aliexpress.local.logistic.label.print` |
| 48 | `aliexpress.local.logistics.order.create` |
| 49 | `aliexpress.local.logistics.shipping.method.query` |
| 50 | `aliexpress.local.logistics.order.info.query` |
| 51 | `aliexpress.local.logistics.report.shipped` |
| 52 | `aliexpress.local.logistics.label.print` |
| 53 | `cainiao.waybill.cloudprint.netprint.bind` |
| 54 | `cainiao.waybill.cloudprint.netprint.verifycode` |
| 55 | `alibaba.ascp.logistics.cp.get` |
| 56 | `alibaba.ascp.logistics.identcode.query` |
| 57 | `alibaba.tcls.fulfill.qa.order.query` |
| 58 | `alibaba.tcls.qa.order.advance` |
| 59 | `alibaba.ascp.logistics.identcode.upload` |
| 60 | `wdk.logistics.mps.car.entrypark.identify.check` |
| 61 | `wdk.logistics.mps.car.entrypark.in` |
| 62 | `wdk.logistics.mps.car.entrypark.out` |
| 63 | `alibaba.fengniao.ecology.knight.info.snapshot.query` |
| 64 | `alibaba.fengniao.ecology.insurance.order.snapshot.query` |
| 65 | `alibaba.fengniao.ecology.insurance.case.snapshot.query` |
| 66 | `alibaba.fengniao.ecology.settlement.record.snapshot.query` |
| 67 | `alibaba.fengniao.ecology.settlement.receipt.snapshot.query` |
| 68 | `alibaba.fengniao.ecology.settlement.tax.snapshot.query` |
| 69 | `alibaba.fengniao.ecology.settlement.waybill.snapshot.query` |
| 70 | `alibaba.fengniao.ecology.attachment.info.query` |
| 71 | `alibaba.fengniao.ecology.safety.info.query` |
| 72 | `alibaba.fengniao.ecology.insurance.case.query` |
| 73 | `alibaba.fengniao.ecology.insurance.order.query` |

</details>

### 店铺API (21 APIs)

<details>
<summary>展开查看全部 21 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.shopcats.list.get` |
| 2 | `taobao.sellercats.list.get` |
| 3 | `taobao.sellercats.list.add` |
| 4 | `taobao.sellercats.list.update` |
| 5 | `alibaba.interact.sensor.clipbroad` |
| 6 | `alibaba.data.item.get` |
| 7 | `alibaba.data.coupon.get` |
| 8 | `taobao.store.followurl.get` |
| 9 | `taobao.shop.seller.get` |
| 10 | `alibaba.koubeishops.property.get` |
| 11 | `alibaba.shop.coupon.apply` |
| 12 | `alibaba.shop.category.all.get` |
| 13 | `alibaba.shop.category.get` |
| 14 | `taobao.mcn.shopcats.list.get` |
| 15 | `alibaba.xsd.stores.query` |
| 16 | `alibaba.xsd.store.create` |
| 17 | `alibaba.xsd.store.info.update` |
| 18 | `alibaba.xsd.store.address.update` |
| 19 | `alibaba.xsd.store.open` |
| 20 | `alibaba.xsd.store.close` |
| 21 | `alibaba.xsd.store.business.category.list` |

</details>

### 分销API (88 APIs)

<details>
<summary>展开查看全部 88 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.fenxiao.orders.get` |
| 2 | `taobao.fenxiao.product.add` |
| 3 | `taobao.fenxiao.product.update` |
| 4 | `taobao.fenxiao.productcats.get` |
| 5 | `taobao.fenxiao.products.get` |
| 6 | `taobao.fenxiao.grades.get` |
| 7 | `taobao.fenxiao.order.confirm.paid` |
| 8 | `taobao.fenxiao.distributor.items.get` |
| 9 | `taobao.fenxiao.cooperation.get` |
| 10 | `taobao.fenxiao.login.user.get` |
| 11 | `taobao.fenxiao.product.sku.delete` |
| 12 | `taobao.fenxiao.product.sku.add` |
| 13 | `taobao.fenxiao.product.sku.update` |
| 14 | `taobao.fenxiao.product.skus.get` |
| 15 | `taobao.fenxiao.product.image.upload` |
| 16 | `taobao.fenxiao.product.image.delete` |
| 17 | `taobao.fenxiao.order.remark.update` |
| 18 | `taobao.fenxiao.product.gradeprice.update` |
| 19 | `taobao.fenxiao.product.map.add` |
| 20 | `taobao.scitem.outercode.get` |
| 21 | `taobao.scitem.get` |
| 22 | `taobao.scitem.query` |
| 23 | `taobao.scitem.update` |
| 24 | `taobao.scitem.add` |
| 25 | `taobao.scitem.map.delete` |
| 26 | `taobao.scitem.map.query` |
| 27 | `taobao.scitem.map.add` |
| 28 | `taobao.inventory.store.query` |
| 29 | `taobao.inventory.adjust.external` |
| 30 | `taobao.inventory.store.manage` |
| 31 | `taobao.inventory.initial` |
| 32 | `taobao.inventory.query` |
| 33 | `taobao.fenxiao.product.gradeprice.get` |
| 34 | `taobao.fenxiao.productcat.delete` |
| 35 | `taobao.fenxiao.productcat.update` |
| 36 | `taobao.fenxiao.productcat.add` |
| 37 | `taobao.inventory.initial.item` |
| 38 | `taobao.fenxiao.refund.get` |
| 39 | `taobao.fenxiao.distributor.products.get` |
| 40 | `taobao.fenxiao.dealer.requisitionorder.close` |
| 41 | `taobao.fenxiao.dealer.requisitionorder.get` |
| 42 | `taobao.fenxiao.dealer.requisitionorder.query` |
| 43 | `taobao.fenxiao.dealer.requisitionorder.remark.update` |
| 44 | `taobao.fenxiao.refund.query` |
| 45 | `taobao.fenxiao.product.quantity.update` |
| 46 | `tmall.inventory.query.forstore` |
| 47 | `taobao.inventory.warehouse.query` |
| 48 | `taobao.inventory.warehouse.manage` |
| 49 | `taobao.region.warehouse.manage` |
| 50 | `taobao.region.sale.query` |
| 51 | `taobao.region.warehouse.query` |
| 52 | `taobao.fenxiao.product.import.from.auction` |
| 53 | `taobao.fenxiao.product.to.channel.import` |
| 54 | `tmall.channel.products.get` |
| 55 | `taobao.kaola.scitem.add` |
| 56 | `tmall.supplychain.channel.product.release` |
| 57 | `tmall.supplychain.channel.product.release.status.get` |
| 58 | `tmall.supplychain.channel.product.price.update` |
| 59 | `tmall.supplychain.channel.product.upshelf` |
| 60 | `tmall.supplychain.channel.product.downshelf` |
| 61 | `tmall.supplychain.channel.product.quantity.get` |
| 62 | `tmall.supplychain.channel.product.quantity.update` |
| 63 | `alibaba.ascp.cnsku.update` |
| 64 | `alibaba.ascp.cnsku.search` |
| 65 | `taobao.fenxiao.yph.orders.get` |
| 66 | `taobao.fenxiao.yph.order.get` |
| 67 | `taobao.fenxiao.yph.refunds.get` |
| 68 | `taobao.fenxiao.yph.refund.get` |
| 69 | `alibaba.fenxiao.cbutotaobao.relation.add` |
| 70 | `alibaba.ascp.cnsku.add` |
| 71 | `alibaba.ascp.cnsku.modify` |
| 72 | `taobao.fenxiao.distributor.product.quantity.get` |
| 73 | `alibaba.ascp.cnsku.mapping.delete` |
| 74 | `taobao.fenxiao.settlement.invoice.genurl` |
| 75 | `taobao.fenxiao.settlement.invoice.submit` |
| 76 | `taobao.fenxiao.settlement.statement.get` |
| 77 | `taobao.fenxiao.settlement.expense.query` |
| 78 | `taobao.gongxiao.sales.get` |
| 79 | `taobao.gongxiao.refund.get` |
| 80 | `taobao.fenxiao.settlement.redconfirm.submit` |
| 81 | `taobao.fenxiao.refund.sup.agree` |
| 82 | `taobao.fenxiao.refund.sup.refuse` |
| 83 | `taobao.fenxiao.returngoods.sup.agree` |
| 84 | `taobao.fenxiao.returngoods.sup.refuse` |
| 85 | `taobao.fenxiao.returngoods.sup.refuseconfirm` |
| 86 | `taobao.fenxiao.returngoods.sup.confirmgoods` |
| 87 | `taobao.fenxiao.order.cancel` |
| 88 | `taobao.fenxiao.order.ship` |

</details>

### 旺旺API

| # | API名称 |
|---|--------|
| 1 | `taobao.airisland.kefueval.get` |

### 淘宝客API (42 APIs)

<details>
<summary>展开查看全部 42 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.tbk.item.info.get` |
| 2 | `taobao.tbk.shop.get` |
| 3 | `taobao.tbk.shop.recommend.get` |
| 4 | `taobao.tbk.spread.get` |
| 5 | `taobao.tbk.coupon.get` |
| 6 | `taobao.tbk.tpwd.create` |
| 7 | `taobao.tbk.dg.newuser.order.get` |
| 8 | `taobao.tbk.sc.adzone.create` |
| 9 | `taobao.tbk.dg.newuser.order.sum` |
| 10 | `taobao.tbk.sc.publisher.info.save` |
| 11 | `taobao.tbk.sc.publisher.info.get` |
| 12 | `taobao.tbk.sc.invitecode.get` |
| 13 | `taobao.tbk.dg.vegas.tlj.create` |
| 14 | `taobao.tbk.sc.punish.order.get` |
| 15 | `taobao.tbk.dg.punish.order.get` |
| 16 | `taobao.tbk.sc.order.details.get` |
| 17 | `taobao.tbk.sc.relation.refund` |
| 18 | `taobao.tbk.sc.vegas.send.report` |
| 19 | `taobao.tbk.dg.vegas.send.report` |
| 20 | `taobao.tbk.activity.info.get` |
| 21 | `taobao.tbk.sc.activity.info.get` |
| 22 | `taobao.tbk.dg.optimus.promotion` |
| 23 | `taobao.tbk.sc.optimus.promotion` |
| 24 | `taobao.tbk.dg.vegas.send.status` |
| 25 | `taobao.tbk.sc.relation.record` |
| 26 | `taobao.tbk.cart.coupon.expire.user.query` |
| 27 | `taobao.tbk.dg.cpa.activity.detail` |
| 28 | `taobao.tbk.dg.tpwd.report.get` |
| 29 | `taobao.tbk.dg.cpa.activity.report` |
| 30 | `taobao.tbk.dg.vegas.tlj.stop` |
| 31 | `taobao.tbk.dg.vegas.tlj.report` |
| 32 | `taobao.tbk.dg.tpwd.risk.report` |
| 33 | `taobao.tbk.sc.material.recommend` |
| 34 | `taobao.tbk.dg.material.recommend` |
| 35 | `taobao.tbk.sc.membergroup.optional` |
| 36 | `taobao.tbk.optimus.tou.material.ids.get` |
| 37 | `taobao.tbk.sc.material.optional.upgrade` |
| 38 | `taobao.tbk.dg.material.optional.upgrade` |
| 39 | `taobao.tbk.seed.kox.write` |
| 40 | `taobao.tbk.dg.rta.sr.issue.match` |
| 41 | `taobao.tbk.sc.rta.sr.issue.match` |
| 42 | `taobao.tbk.dg.vegas.tlj.list.report` |

</details>

### 工具API (44 APIs)

<details>
<summary>展开查看全部 44 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.time.get` |
| 2 | `taobao.kfc.keyword.search` |
| 3 | `taobao.appip.get` |
| 4 | `taobao.top.auth.token.refresh` |
| 5 | `taobao.top.auth.token.create` |
| 6 | `taobao.httpdns.get` |
| 7 | `taobao.top.ipout.get` |
| 8 | `taobao.top.secret.get` |
| 9 | `taobao.top.openid.convert` |
| 10 | `taobao.top.secret.register` |
| 11 | `taobao.top.sdk.feedback.upload` |
| 12 | `taobao.streetest.session.get` |
| 13 | `taobao.qimen.trade.users.get` |
| 14 | `taobao.qimen.trade.user.delete` |
| 15 | `taobao.qimen.trade.user.add` |
| 16 | `taobao.qimen.events.produce` |
| 17 | `taobao.qimen.event.produce` |
| 18 | `taobao.tmc.auth.get` |
| 19 | `taobao.rdc.aligenius.refunds.check` |
| 20 | `alibaba.interact.sensor.ui` |
| 21 | `alibaba.retail.shorturl.get` |
| 22 | `taobao.files.get` |
| 23 | `taobao.openlink.session.get` |
| 24 | `taobao.openuid.get` |
| 25 | `taobao.openuid.get.bytrade` |
| 26 | `taobao.openuid.get.bymixnick` |
| 27 | `aliexpress.social.locale.get` |
| 28 | `aliexpress.social.currency.get` |
| 29 | `aliexpress.social.country.get` |
| 30 | `alibaba.ais.assets.tag.get` |
| 31 | `alibaba.ais.assets.tag.abort` |
| 32 | `alibaba.ais.assets.tag.generate` |
| 33 | `alibaba.mos.falcon.pos.counter.query` |
| 34 | `wdk.rexout.device.info.get` |
| 35 | `wdk.rexout.device.iot.registerid` |
| 36 | `wdk.rexout.resource.list.check` |
| 37 | `taobao.top.connector.event.publish` |
| 38 | `taobao.top.event.publish` |
| 39 | `taobao.muyang.topapi.getinfo` |
| 40 | `taobao.top.event.subscription.query` |
| 41 | `taobao.picture.qnaigc.upload` |
| 42 | `taobao.top.connector.picture.upload` |
| 43 | `taobao.item.competitoritem.gs.applegethistory` |
| 44 | `alitrip.hotel.mi.hotel.detail.query` |

</details>

### 物流宝API (23 APIs)

<details>
<summary>展开查看全部 23 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.wlb.order.consign` |
| 2 | `taobao.wlb.notify.message.page.get` |
| 3 | `taobao.wlb.tmsorder.query` |
| 4 | `taobao.wlb.item.map.get` |
| 5 | `taobao.wlb.item.combination.get` |
| 6 | `taobao.wlb.inventorylog.query` |
| 7 | `taobao.wlb.subscription.query` |
| 8 | `taobao.wlb.order.page.get` |
| 9 | `taobao.wlb.orderitem.page.get` |
| 10 | `taobao.wlb.orderstatus.get` |
| 11 | `taobao.wlb.item.get` |
| 12 | `taobao.wlb.tradeorder.get` |
| 13 | `taobao.wlb.inventory.detail.get` |
| 14 | `taobao.wlb.item.query` |
| 15 | `taobao.wlb.wlborder.get` |
| 16 | `taobao.wlb.orderdetail.date.get` |
| 17 | `taobao.wlb.waybill.shengxian.get` |
| 18 | `taobao.wlb.order.jzpartner.query` |
| 19 | `taobao.wlb.wms.inventory.lack.upload` |
| 20 | `cainiao.bms.order.consign.confirm` |
| 21 | `cainiao.merchant.inventory.adjust` |
| 22 | `taobao.uop.tob.order.create` |
| 23 | `cainiao.waybill.cloudprint.netprint.print` |

</details>

### 直通车API

| # | API名称 |
|---|--------|
| 1 | `taobao.simba.login.authsign.get` |
| 2 | `taobao.simba.rpt.adgroupkeywordeffect.get` |
| 3 | `taobao.simba.rpt.adgroupkeywordbase.get` |
| 4 | `taobao.simba.rpt.adgroupbase.get` |
| 5 | `taobao.simba.rpt.adgroupcreativeeffect.get` |
| 6 | `taobao.simba.rpt.adgroupcreativebase.get` |
| 7 | `taobao.simba.insight.catsforecastnew.get` |
| 8 | `taobao.simba.insight.wordssubdata.get` |
| 9 | `taobao.simba.insight.catsinfo.get` |
| 10 | `taobao.simba.bidword.pricetools` |

### 机票API (60 APIs)

<details>
<summary>展开查看全部 60 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.flightchange.get` |
| 2 | `taobao.alitrip.ie.agent.shopping.push` |
| 3 | `alitrip.tripvp.agent.order.issue` |
| 4 | `alitrip.tripvp.agent.order.get` |
| 5 | `taobao.alitrip.ie.agent.refund.new.fillconfirmfee` |
| 6 | `alitrip.agent.flight.sell.modify.list` |
| 7 | `alitrip.agent.flight.sell.modify.refuse` |
| 8 | `alitrip.agent.flight.sell.refund.detail` |
| 9 | `alitrip.agent.flight.sell.modify.approve` |
| 10 | `alitrip.agent.flight.sell.modify.detail` |
| 11 | `alitrip.agent.flight.sell.refund.refuse` |
| 12 | `alitrip.agent.flight.sell.refund.approve` |
| 13 | `alitrip.agent.flight.sell.refund.list` |
| 14 | `alitrip.agent.flight.sell.modify.backfill` |
| 15 | `alitrip.agent.flight.sell.ticketing.list` |
| 16 | `alitrip.agent.flight.sell.ticketing.detail` |
| 17 | `alitrip.agent.flight.sell.ticketing.issue` |
| 18 | `alitrip.policy.rule.upload` |
| 19 | `alitrip.policy.normal.upload` |
| 20 | `alitrip.policy.special.upload` |
| 21 | `alitrip.policy.process` |
| 22 | `alitrip.policy.domfare.compare` |
| 23 | `alitrip.policy.domfare.flowdata` |
| 24 | `alitrip.agent.coordinate.handle` |
| 25 | `alitrip.agent.coordinate.reject` |
| 26 | `alitrip.agent.coordinate.processing` |
| 27 | `alitrip.agent.coordinate.list` |
| 28 | `alitrip.agent.flight.intention.list` |
| 29 | `alitrip.agent.flight.intention.confirm` |
| 30 | `alitrip.agent.coordinate.upload` |
| 31 | `alitrip.agent.coordinate.detail` |
| 32 | `alitrip.agent.coordinate.goback` |
| 33 | `alitrip.agent.coordinate.process` |
| 34 | `taobao.fliggy.flight.agent.auxproduct.push` |
| 35 | `taobao.fliggy.flight.agent.auxproduct.delete` |
| 36 | `alitrip.policy.normal.compression.upload` |
| 37 | `alitrip.policy.special.compression.upload` |
| 38 | `alitrip.policy.rule.compression.upload` |
| 39 | `alitrip.intl.policy.task.query` |
| 40 | `alitrip.intl.policy.owner.delete` |
| 41 | `alitrip.intl.policy.normal.delete` |
| 42 | `alitrip.intl.policy.normal.upload` |
| 43 | `alitrip.intl.policy.owner.upload` |
| 44 | `alitrip.policy.price.compare.query` |
| 45 | `alitrip.intl.policy.owner.param` |
| 46 | `alitrip.policy.price.compare.flowdata.query` |
| 47 | `alitrip.intl.policy.normal.param` |
| 48 | `alitrip.agent.flight.sell.ticketing.uploadmodifyticketproof` |
| 49 | `alitrip.agent.flight.sell.ticketing.uploadtpticketproof` |
| 50 | `alitrip.domestic.policy.price.compare.query` |
| 51 | `alitrip.agent.flightchange.add` |
| 52 | `taobao.fliggy.flight.agent.auxproduct.dimension.flight.push` |
| 53 | `alitrip.agent.flight.offer.push` |
| 54 | `alitrip.airline.mail.captcha.pagequery` |
| 55 | `alitrip.policy.direct.airline.whitelist.query` |
| 56 | `alitrip.policy.direct.airline.whitelist.batchadd` |
| 57 | `alitrip.policy.direct.airline.whitelist.fullupdate` |
| 58 | `alitrip.policy.direct.airline.whitelist.batchdelete` |
| 59 | `alitrip.policy.direct.price.refresh.query` |
| 60 | `alitrip.policy.direct.price.refresh.upload` |

</details>

### ONS消息服务

| # | API名称 |
|---|--------|
| 1 | `taobao.jushita.jms.user.get` |
| 2 | `taobao.jushita.jms.user.add` |
| 3 | `taobao.jushita.jms.user.delete` |
| 4 | `taobao.jushita.jms.group.get` |
| 5 | `taobao.jushita.jms.topics.get` |

### 营销API (94 APIs)

<details>
<summary>展开查看全部 94 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.promotion.coupon.send` |
| 2 | `taobao.promotion.activity.get` |
| 3 | `taobao.promotion.coupon.add` |
| 4 | `taobao.promotion.coupons.get` |
| 5 | `taobao.promotion.meal.get` |
| 6 | `taobao.ump.mbb.getbyid` |
| 7 | `taobao.ump.tool.get` |
| 8 | `taobao.ump.tools.get` |
| 9 | `taobao.ump.activity.add` |
| 10 | `taobao.ump.activity.update` |
| 11 | `taobao.ump.activity.delete` |
| 12 | `taobao.ump.activity.get` |
| 13 | `taobao.ump.activities.get` |
| 14 | `taobao.ump.detail.get` |
| 15 | `taobao.ump.details.get` |
| 16 | `taobao.ump.detail.add` |
| 17 | `taobao.ump.detail.update` |
| 18 | `taobao.ump.detail.delete` |
| 19 | `taobao.ump.range.add` |
| 20 | `taobao.ump.range.delete` |
| 21 | `taobao.ump.range.get` |
| 22 | `taobao.ump.mbb.getbycode` |
| 23 | `taobao.promotion.limitdiscount.detail.get` |
| 24 | `taobao.marketing.promotion.kfc` |
| 25 | `taobao.ump.mbbs.list.get` |
| 26 | `taobao.ump.activities.list.get` |
| 27 | `taobao.ump.detail.list.add` |
| 28 | `taobao.promotionmisc.tool.check` |
| 29 | `tmall.promotag.tag.apply` |
| 30 | `tmall.promotag.tag.find` |
| 31 | `tmall.promotag.taguser.judge` |
| 32 | `tmall.promotag.taguser.remove` |
| 33 | `tmall.promotag.taguser.save` |
| 34 | `tmall.promotag.tag.removetag` |
| 35 | `taobao.promotionmisc.item.activity.update` |
| 36 | `taobao.promotionmisc.mjs.activity.add` |
| 37 | `taobao.promotionmisc.mjs.activity.get` |
| 38 | `taobao.promotionmisc.activity.range.add` |
| 39 | `taobao.promotionmisc.activity.range.list.get` |
| 40 | `taobao.promotionmisc.activity.range.remove` |
| 41 | `taobao.promotionmisc.activity.range.all.remove` |
| 42 | `taobao.promotionmisc.mjs.activity.list.get` |
| 43 | `taobao.promotionmisc.mjs.activity.update` |
| 44 | `taobao.promotionmisc.mjs.activity.delete` |
| 45 | `taobao.promotionmisc.item.activity.add` |
| 46 | `taobao.promotionmisc.item.activity.get` |
| 47 | `taobao.promotionmisc.item.activity.list.get` |
| 48 | `taobao.promotionmisc.item.activity.delete` |
| 49 | `taobao.promotion.coupon.sns.send` |
| 50 | `taobao.promotion.benefit.activity.delete` |
| 51 | `taobao.promotion.benefit.activity.send` |
| 52 | `taobao.mobile.promotion.benefit.activity.send` |
| 53 | `taobao.promotion.benefit.selector` |
| 54 | `taobao.promotion.benefit.activity.update` |
| 55 | `taobao.promotion.benefit.activity.relation` |
| 56 | `taobao.promotion.benefit.activity.time.update` |
| 57 | `taobao.promotion.benefit.activity.detail.get` |
| 58 | `taobao.promotion.coupon.seller.search` |
| 59 | `taobao.promotion.coupon.apply` |
| 60 | `taobao.mobile.promotion.benefit.activity.send.share` |
| 61 | `taobao.promotionmisc.common.item.detail.list.get` |
| 62 | `taobao.promotionmisc.common.item.activity.add` |
| 63 | `taobao.promotionmisc.common.item.detail.delete` |
| 64 | `taobao.promotionmisc.common.item.detail.update` |
| 65 | `taobao.promotionmisc.common.item.detail.add` |
| 66 | `taobao.promotionmisc.common.item.activity.list.get` |
| 67 | `taobao.promotionmisc.common.item.activity.get` |
| 68 | `taobao.promotionmisc.common.item.activity.delete` |
| 69 | `taobao.promotionmisc.common.item.activity.update` |
| 70 | `taobao.mobile.promotion.coupon.seller.search` |
| 71 | `taobao.mobile.promotion.coupon.apply` |
| 72 | `alibaba.wdk.marketing.coupon.sendma` |
| 73 | `tmall.promotion.coupon.use` |
| 74 | `tmall.promotion.coupon.query` |
| 75 | `taobao.ump.promotion.global.discount.get` |
| 76 | `alibaba.latour.strategy.issue` |
| 77 | `alibaba.wdk.coupon.abandon` |
| 78 | `alibaba.wdk.coupon.sku.query` |
| 79 | `alibaba.wdk.coupon.sku.remove` |
| 80 | `alibaba.wdk.coupon.template.query` |
| 81 | `alibaba.wdk.coupon.template.terminate` |
| 82 | `alibaba.wdk.coupon.spread.apply` |
| 83 | `alibaba.wdk.coupon.sku.add` |
| 84 | `alibaba.wdk.coupon.template.create` |
| 85 | `alibaba.wdk.coupon.template.update` |
| 86 | `alibaba.latour.strategy.show` |
| 87 | `alibaba.benefit.query` |
| 88 | `alibaba.benefit.draw` |
| 89 | `taobao.card.expandcard.query` |
| 90 | `alibaba.asr.dataservice.promotionrule.write` |
| 91 | `alibaba.asr.dataservice.promotionrule.delete` |
| 92 | `alibaba.asr.dataservice.promotionrule.query` |
| 93 | `alibaba.lafite.seller.benefit.list` |
| 94 | `alibaba.lafite.seller.activity.list` |

</details>

### 数据API

| # | API名称 |
|---|--------|
| 1 | `alibaba.nrs.item.pricetag.recognize` |
| 2 | `alibaba.nrs.item.rtdata.backflow` |
| 3 | `taobao.ads.data.import` |
| 4 | `taobao.ads.data.query` |

### 酒店API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.order.official.qualification.get` |
| 2 | `taobao.xhotel.order.offline.settle.cancel` |
| 3 | `taobao.xhotel.order.hotelsign.query` |
| 4 | `taobao.xhotel.data.service.hotel.serviceindex` |
| 5 | `taobao.xhotel.data.service.order.detail` |
| 6 | `alitrip.xhotel.channel.order.create.res.query` |
| 7 | `taobao.xhotel.bnbpromo.update` |
| 8 | `taobao.xhotel.city.distribution.get` |
| 9 | `alitrip.hotel.mi.settle.query` |
| 10 | `alitrip.hotel.mi.settle.trigger` |
| 11 | `taobao.xhotel.cm.ota.hotelrateamountnotif.post` |
| 12 | `taobao.xhotel.cm.ota.hotelproduct.post` |
| 13 | `taobao.xhotel.combo.add` |
| 14 | `taobao.xhotel.combo.update` |
| 15 | `taobao.xhotel.cm.ota.hotelavailnotif.post` |

### 店铺会员管理API (33 APIs)

<details>
<summary>展开查看全部 33 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.crm.grade.get` |
| 2 | `taobao.crm.shopvip.cancel` |
| 3 | `taobao.crm.members.increment.get` |
| 4 | `taobao.crm.members.group.batchadd` |
| 5 | `taobao.crm.grade.set` |
| 6 | `taobao.crm.members.groups.batchdelete` |
| 7 | `taobao.crm.groups.get` |
| 8 | `taobao.crm.group.update` |
| 9 | `taobao.crm.group.add` |
| 10 | `taobao.crm.members.search` |
| 11 | `taobao.crm.memberinfo.update` |
| 12 | `taobao.crm.members.get` |
| 13 | `taobao.crm.group.delete` |
| 14 | `taobao.crm.group.append` |
| 15 | `taobao.crm.group.move` |
| 16 | `taobao.crm.grouptask.check` |
| 17 | `taobao.crm.grademkt.member.add` |
| 18 | `taobao.crm.grademkt.member.detail.query` |
| 19 | `taobao.crm.grademkt.member.detail.delete` |
| 20 | `taobao.crm.grademkt.member.detail.create` |
| 21 | `taobao.crm.grademkt.member.query` |
| 22 | `taobao.crm.member.group.get` |
| 23 | `taobao.crm.service.channel.shortlink.create` |
| 24 | `taobao.crm.exchange.activity.create` |
| 25 | `taobao.crm.members.increment.get.privy` |
| 26 | `taobao.crm.members.search.privy` |
| 27 | `taobao.crm.members.get.privy` |
| 28 | `taobao.crm.memberinfo.update.privy` |
| 29 | `taobao.crm.members.group.batchadd.privy` |
| 30 | `taobao.member.hismemberdata.get.privy` |
| 31 | `taobao.crm.members.groups.batchdelete.privy` |
| 32 | `taobao.crm.member.group.get.privy` |
| 33 | `taobao.crm.exchange.crowdinstance.add.privy` |

</details>

### 多媒体平台API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.picture.category.get` |
| 2 | `taobao.picture.get` |
| 3 | `taobao.picture.delete` |
| 4 | `taobao.picture.upload` |
| 5 | `taobao.picture.category.add` |
| 6 | `taobao.picture.category.update` |
| 7 | `taobao.picture.update` |
| 8 | `taobao.picture.userinfo.get` |
| 9 | `taobao.picture.isreferenced.get` |
| 10 | `taobao.picture.pictures.get` |
| 11 | `taobao.picture.pictures.count` |
| 12 | `taobao.interactive.list.getbyuser` |
| 13 | `taobao.miniapp.cloud.picture.token` |
| 14 | `alibaba.tjb.picture.upload` |
| 15 | `alibaba.tjb.picture.folder.query` |
| 16 | `alibaba.tjb.picture.userstorage.query` |
| 17 | `alibaba.tjb.picture.folder.create` |

</details>

### 子账号管理API

| # | API名称 |
|---|--------|
| 1 | `taobao.sellercenter.subusers.get` |
| 2 | `taobao.sellercenter.user.permissions.get` |
| 3 | `taobao.sellercenter.subuser.permissions.roles.get` |
| 4 | `taobao.sellercenter.roles.get` |
| 5 | `taobao.sellercenter.role.add` |
| 6 | `taobao.subusers.get` |
| 7 | `taobao.subuser.fullinfo.get` |
| 8 | `taobao.subuser.departments.get` |
| 9 | `taobao.subuser.dutys.get` |
| 10 | `taobao.subuser.info.update` |
| 11 | `taobao.sellercenter.subusers.page` |
| 12 | `taobao.subusers.page` |
| 13 | `taobao.subusers.subaccount.search` |
| 14 | `taobao.subusers.info.query` |

### 服务平台API (31 APIs)

<details>
<summary>展开查看全部 31 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.vas.service.validate` |
| 2 | `taobao.vas.subscribe.get` |
| 3 | `taobao.vas.order.search` |
| 4 | `taobao.vas.subsc.search` |
| 5 | `taobao.fuwu.sale.link.gen` |
| 6 | `taobao.fuwu.scores.get` |
| 7 | `taobao.weike.subscinfo.get` |
| 8 | `taobao.weike.performance.put` |
| 9 | `taobao.fuwu.sku.get` |
| 10 | `taobao.fuwu.sp.confirm.apply` |
| 11 | `taobao.fuwu.purchase.order.confirm` |
| 12 | `taobao.fuwu.sp.billreord.add` |
| 13 | `taobao.fuwu.purchase.order.pay` |
| 14 | `taobao.weike.eservice.schedule.get` |
| 15 | `taobao.weike.eservice.subusers.get` |
| 16 | `taobao.weike.eservice.order.get` |
| 17 | `tmall.car.lease.consume` |
| 18 | `tmall.car.leaseorder.get` |
| 19 | `tmall.car.contract.download` |
| 20 | `tmall.servicecenter.tp.funds.recover.query` |
| 21 | `tmall.servicecenter.tp.funds.send.query` |
| 22 | `tmall.car.lease.freedownpayment.put` |
| 23 | `taobao.recycle.ofnpreredpacket.tpdeductsuccess` |
| 24 | `taobao.recycle.ofnpreredpacket.get` |
| 25 | `taobao.recycle.ofnsubsidy.old.get` |
| 26 | `taobao.recycle.prededuct.blacklist.order.sync` |
| 27 | `taobao.recycle.order.fulfill.sync` |
| 28 | `taobao.recycle.prededuct.settle.sync` |
| 29 | `taobao.recycle.prededuct.old.get` |
| 30 | `taobao.item.competitoritem.gs.dimension` |
| 31 | `taobao.recycle.old.waybillno.report` |

</details>

### 退款API

| # | API名称 |
|---|--------|
| 1 | `taobao.rdc.aligenius.sendgoods.cancel` |
| 2 | `taobao.rdc.aligenius.identification.case.result.update` |
| 3 | `taobao.rdc.aligenius.identification.case.update` |
| 4 | `aliyun.fbt.refund.erp.intercept` |
| 5 | `taobao.retrieve.strategy.delete` |
| 6 | `taobao.retrieve.strategy.save` |
| 7 | `taobao.retrieve.strategy.search` |
| 8 | `taobao.retrieve.record.search` |
| 9 | `taobao.retrieve.strategy.find` |
| 10 | `taobao.retrieve.strategy.create` |
| 11 | `taobao.shangou.refund.list` |

### 质检品控API

| # | API名称 |
|---|--------|
| 1 | `taobao.qt.report.get` |
| 2 | `taobao.ts.property.get` |
| 3 | `taobao.ts.subscribe.get` |
| 4 | `taobao.qt.report.update` |
| 5 | `taobao.qt.report.add` |
| 6 | `taobao.qt.report.delete` |
| 7 | `taobao.qt.reports.get` |

### 天猫服务商品API (122 APIs)

<details>
<summary>展开查看全部 122 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.servicecenter.contracts.search` |
| 2 | `tmall.servicecenter.tasks.search` |
| 3 | `tmall.servicecenter.workcard.status.update` |
| 4 | `tmall.servicecenter.task.get` |
| 5 | `tmall.servicecenter.workcard.push` |
| 6 | `tmall.msf.identify.status.query` |
| 7 | `tmall.msf.reservation` |
| 8 | `tmall.servicecenter.anomalyrecourse.querybyid` |
| 9 | `tmall.service.settleadjustment.request` |
| 10 | `tmall.service.settleadjustment.get` |
| 11 | `tmall.service.settleadjustment.cancel` |
| 12 | `tmall.servicecenter.task.feedbacknoneedservice` |
| 13 | `tmall.servicecenter.picture.upload` |
| 14 | `tmall.servicecenter.worker.create` |
| 15 | `tmall.servicecenter.worker.querycapacitytask` |
| 16 | `tmall.servicecenter.worker.querypage` |
| 17 | `tmall.servicecenter.servicestore.updateservicestore` |
| 18 | `tmall.servicecenter.servicestore.deleteservicestore` |
| 19 | `tmall.servicecenter.servicestore.deleteservicestorecoverservice` |
| 20 | `tmall.servicecenter.servicestore.createservicestore` |
| 21 | `tmall.servicecenter.worker.update` |
| 22 | `tmall.servicecenter.servicemonitormessage.update` |
| 23 | `tmall.servicecenter.servicemonitormessage.search` |
| 24 | `tmall.servicecenter.workcard.reassign` |
| 25 | `tmall.servicecenter.workcard.verifycode.resend` |
| 26 | `tmall.servicecenter.servicestore.update` |
| 27 | `tmall.servicecenter.workcard.query` |
| 28 | `tmall.servicecenter.servicestore.create` |
| 29 | `tmall.servicecenter.servicestore.updatestatus` |
| 30 | `tmall.mallitemcenter.supplier.ability.update` |
| 31 | `tmall.mallitemcenter.supplier.price.upload` |
| 32 | `tmall.mallitemcenter.serviceproduct.query` |
| 33 | `tmall.mallitemcenter.subscribe.query` |
| 34 | `tmall.servicecenter.workcard.reserve` |
| 35 | `tmall.servicecenter.workcard.complete` |
| 36 | `tmall.servicecenter.workcard.signin` |
| 37 | `tmall.servicecenter.spserviceorder.query` |
| 38 | `tmall.servicecenter.workcard.assignworker` |
| 39 | `tmall.servicecenter.workcard.reservefail` |
| 40 | `tmall.servicecenter.workcard.suspend` |
| 41 | `alibaba.ssc.supplyplatform.serviceability.save` |
| 42 | `alibaba.ssc.supplyplatform.servicecapacity.delete` |
| 43 | `alibaba.ssc.supplyplatform.serviceability.delete` |
| 44 | `alibaba.ssc.supplyplatform.servicecapacity.save` |
| 45 | `alibaba.ssc.servicecenter.servicestore.query` |
| 46 | `alibaba.mallitemcenter.entitledservice.supplier.query` |
| 47 | `alibaba.servicecenter.spserviceorder.query` |
| 48 | `alibaba.servicecenter.workcard.create` |
| 49 | `alibaba.servicecenter.workcard.cancel` |
| 50 | `alibaba.servicecenter.spserviceorder.update` |
| 51 | `tmall.servicecenter.worker.taglist.get` |
| 52 | `alibaba.ssc.supplyplatform.servicestore.save` |
| 53 | `alibaba.ssc.supplyplatform.servicestore.offline` |
| 54 | `tmall.servicecenter.workcard.repairprogress.update` |
| 55 | `tmall.servicecenter.workcard.evaluate` |
| 56 | `tmall.servicecenter.workcard.expressorder.consign` |
| 57 | `tmall.servicecenter.workcard.expressorder.create` |
| 58 | `tmall.servicecenter.workcard.virtualphone.bind` |
| 59 | `tmall.servicecenter.workcard.call.record` |
| 60 | `tmall.servicecenter.workcard.logisticsorder.update` |
| 61 | `tmall.servicecenter.workcard.logisticsorder.query` |
| 62 | `alibaba.servicecenter.fulfiltask.buyeraddress.change` |
| 63 | `tmall.servicecenter.workcard.querybyseller` |
| 64 | `tmall.servicecenter.fulfiltask.insurance.action` |
| 65 | `alibaba.servicecenter.workcard.serviceprogress.update` |
| 66 | `tmall.servicecenter.servicemonitormessage.info` |
| 67 | `tmall.servicecenter.workcard.logisticsorder.tpcancel` |
| 68 | `tmall.servicecenter.workcard.extracharge.create` |
| 69 | `tmall.servicecenter.spserviceorder.epoc.receive` |
| 70 | `tmall.servicecenter.spserviceorder.epoc.upload` |
| 71 | `tmall.servicecenter.spserviceorder.epoc.transfer` |
| 72 | `tmall.servicecenter.spserviceorder.create` |
| 73 | `tmall.servicecenter.workcard.desensitization.query` |
| 74 | `tmall.ssc.supplyplatform.capacity.edit` |
| 75 | `alibaba.ssc.supplyplatform.servicedefinition.querysku` |
| 76 | `tmall.service.settlement.billinfo.query` |
| 77 | `tmall.service.settleadjustment.operate` |
| 78 | `tmall.ssc.workcard.accept` |
| 79 | `tmall.servicecenter.anomalyrecourse.homedecoration.querybyid` |
| 80 | `tmall.service.settlement.fb.bill.query` |
| 81 | `tmall.service.settlement.fb.bill.detail.query` |
| 82 | `tmall.fuwu.homedecoration.supplyrule.categoryworkerlist` |
| 83 | `tmall.fuwu.homedecoration.supplyrule.list` |
| 84 | `tmall.fuwu.homedecoration.workerlevel.list` |
| 85 | `tmall.fuwu.homedecoration.seller.workcard.notes` |
| 86 | `tmall.fuwu.homedecoration.seller.workcard.list` |
| 87 | `alibaba.servicecenter.fulfiltask.reserveandaddress.change` |
| 88 | `tmall.msf.new.reservation` |
| 89 | `alibaba.homedecoration.areacapacity.query` |
| 90 | `alibaba.homedecoration.areacapacity.current.query` |
| 91 | `alibaba.homedecoration.areacapacity.save` |
| 92 | `alibaba.ssc.brand.licensor.workercard.query` |
| 93 | `tmall.service.settlement.file.upload` |
| 94 | `tmall.service.settlement.invoice.upload` |
| 95 | `tmall.servicecenter.anomalyrecourse.homedecoration.update` |
| 96 | `tmall.servicecenter.anomalyrecourse.homedecoration.query` |
| 97 | `alibaba.ssc.yichao.workcard.reserve` |
| 98 | `alibaba.ssc.yichao.workcard.signin` |
| 99 | `alibaba.ssc.yichao.workcard.complete` |
| 100 | `alibaba.ssc.yichao.workcard.cancel` |
| 101 | `alibaba.ssc.yichao.workcard.assignworker` |
| 102 | `alibaba.servicecenter.workcard.reserveandaddress.change` |
| 103 | `alibaba.ssc.yichao.claim.upload` |
| 104 | `alibaba.ssc.yichao.claim.again` |
| 105 | `alibaba.ssc.yichao.claim.start` |
| 106 | `alibaba.ssc.yichao.insurance.inspect` |
| 107 | `tmall.mallitemcenter.supplier.ability.update.batch` |
| 108 | `alibaba.ssc.yichao.insurance.query` |
| 109 | `tmall.servicecenter.homedecoration.consultation.close` |
| 110 | `tmall.servicecenter.homedecoration.consultation.append` |
| 111 | `tmall.servicecenter.homedecoration.consultation.respond` |
| 112 | `tmall.servicecenter.homedecoration.consultation.query` |
| 113 | `alibaba.ssc.yichao.claim.query` |
| 114 | `alibaba.ssc.supplyplatform.workermobile.authentication` |
| 115 | `alibaba.ssc.supplyplatform.workermobile.auth.get` |
| 116 | `alibaba.ssc.supplyplatform.workermobile.auth.del` |
| 117 | `alibaba.ssc.homedecoration.workcard.assigncustomerservice` |
| 118 | `alibaba.ssc.homedecoration.warehouse.getpkgrelateinfo` |
| 119 | `alibaba.ssc.homedecoration.pkglogisticsinfo.query` |
| 120 | `alibaba.home.onsiteservice.trade.geturl` |
| 121 | `alibaba.home.onsiteservice.expression.query` |
| 122 | `alibaba.home.installationguide.expression.query` |

</details>

### 天猫精品库API

| # | API名称 |
|---|--------|
| 1 | `tmall.items.extend.search` |

### 聚石塔API (40 APIs)

<details>
<summary>展开查看全部 40 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.rds.db.create` |
| 2 | `taobao.rds.db.get` |
| 3 | `taobao.rds.db.delete` |
| 4 | `taobao.jushita.jdp.user.delete` |
| 5 | `taobao.jushita.jdp.user.add` |
| 6 | `taobao.jushita.jdp.users.get` |
| 7 | `taobao.jds.trade.traces.get` |
| 8 | `taobao.jds.trades.statistics.diff` |
| 9 | `taobao.jds.trades.statistics.get` |
| 10 | `taobao.jds.hluser.update` |
| 11 | `taobao.jds.hluser.get` |
| 12 | `taobao.jds.refund.traces.get` |
| 13 | `taobao.oc.tradetag.attach` |
| 14 | `taobao.oc.trades.bytag.get` |
| 15 | `taobao.oc.tradetags.get` |
| 16 | `taobao.oc.tradetrace.alerts.get` |
| 17 | `taobao.oc.ap.contracturl.get` |
| 18 | `taobao.oc.ap.contractsigned.get` |
| 19 | `taobao.qimen.orderstatus.update` |
| 20 | `taobao.rds.db.createaccount` |
| 21 | `taobao.rds.db.getdb` |
| 22 | `taobao.jst.sms.message.send` |
| 23 | `taobao.jst.sms.message.direct.batchsend` |
| 24 | `taobao.jst.sms.message.shorturl.create` |
| 25 | `taobao.jst.sms.message.shorturl.query` |
| 26 | `taobao.jst.sms.oaid.message.send` |
| 27 | `alibaba.modifyaddress.isv.bindseller.check` |
| 28 | `taobao.modifyaddress.open` |
| 29 | `taobao.modifysku.query.status` |
| 30 | `taobao.jst.sms.signname.create` |
| 31 | `taobao.jst.sms.signname.query` |
| 32 | `taobao.jst.sms.signname.delete` |
| 33 | `taobao.jst.sms.template.create` |
| 34 | `taobao.jst.sms.template.query` |
| 35 | `taobao.jst.sms.template.delete` |
| 36 | `taobao.jst.sms.template.modify` |
| 37 | `taobao.modifyorder.order.check` |
| 38 | `taobao.jst.sms.signname.report` |
| 39 | `taobao.top.biz.seller.sign` |
| 40 | `taobao.jst.sms.signname.create.new` |

</details>

### 电子物流API (30 APIs)

<details>
<summary>展开查看全部 30 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.vmarket.eticket.beforeconsume` |
| 2 | `taobao.vmarket.eticket.consume` |
| 3 | `taobao.vmarket.eticket.resend` |
| 4 | `taobao.vmarket.eticket.send` |
| 5 | `taobao.vmarket.eticket.reverse` |
| 6 | `taobao.vmarket.eticket.codes.get` |
| 7 | `taobao.vmarket.eticket.oplogs.get` |
| 8 | `taobao.vmarket.eticket.tasks.get` |
| 9 | `taobao.vmarket.eticket.manage.notify` |
| 10 | `taobao.vmarket.eticket.auth.beforeconsume` |
| 11 | `taobao.vmarket.eticket.auth.consume` |
| 12 | `taobao.vmarket.eticket.qrcode.upload` |
| 13 | `taobao.vmarket.eticket.time.expand` |
| 14 | `taobao.vmarket.eticket.store.get` |
| 15 | `taobao.vmarket.eticket.flow.resend` |
| 16 | `taobao.vmarket.eticket.flow.consume` |
| 17 | `taobao.vmarket.eticket.failsend` |
| 18 | `taobao.eticket.merchant.ma.reverse` |
| 19 | `taobao.eticket.merchant.img.upload` |
| 20 | `taobao.eticket.merchant.ma.available` |
| 21 | `taobao.eticket.merchant.ma.consume` |
| 22 | `taobao.eticket.merchant.ma.resend` |
| 23 | `taobao.eticket.merchant.ma.failsend` |
| 24 | `taobao.eticket.merchant.ma.send` |
| 25 | `taobao.eticket.merchant.tbma.get` |
| 26 | `taobao.eticket.merchant.ma.delay` |
| 27 | `taobao.eticket.merchant.package.query` |
| 28 | `taobao.eticket.merchant.package.create` |
| 29 | `taobao.eticket.merchant.notice.refundstatus` |
| 30 | `taobao.eticket.merchant.report.query` |

</details>

### 彩票API

| # | API名称 |
|---|--------|
| 1 | `taobao.caipiao.signstatus.check` |
| 2 | `taobao.caipiao.lotterytypes.get` |
| 3 | `taobao.caipiao.present.stat.get` |
| 4 | `taobao.caipiao.shop.info.input` |
| 5 | `taobao.caipiao.goods.info.input` |
| 6 | `taobao.caipiao.goods.info.get` |
| 7 | `taobao.caipiao.marketing.put` |

### 账务API

| # | API名称 |
|---|--------|
| 1 | `taobao.bill.accounts.get` |
| 2 | `taobao.bill.book.bills.get` |
| 3 | `taobao.bill.bills.get` |
| 4 | `taobao.tae.book.bills.get` |
| 5 | `taobao.tae.book.bill.get` |
| 6 | `taobao.tae.accounts.get` |
| 7 | `taobao.tae.bills.get` |
| 8 | `taobao.tae.bill.get` |

### 拍卖API (38 APIs)

<details>
<summary>展开查看全部 38 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.auction.zc.project.detail` |
| 2 | `taobao.auction.zc.project.query` |
| 3 | `taobao.auction.zc.project.proxy` |
| 4 | `taobao.auction.zc.auction.public` |
| 5 | `taobao.auction.zc.auction.draft.public` |
| 6 | `taobao.auction.zc.project.detail.result` |
| 7 | `taobao.auction.zc.bidresult.get` |
| 8 | `taobao.auction.zc.itemlist.pagequery` |
| 9 | `taobao.auction.standard.auction.operate` |
| 10 | `taobao.auction.zc.bidderinfo.pagequery` |
| 11 | `taobao.auction.standard.auction.publish` |
| 12 | `taobao.auction.zc.spcuser.incr.update` |
| 13 | `taobao.auction.zc.project.notice.detail` |
| 14 | `taobao.auction.gov.publish.upload.video` |
| 15 | `taobao.auction.zc.bidderinfo.pdf` |
| 16 | `taobao.paimai.auctioncat.nft.checknftuseridentify` |
| 17 | `taobao.auction.beike.item.sync` |
| 18 | `taobao.auction.vehicle.detect.report.update` |
| 19 | `taobao.auction.zc.vehicle.detect.status.process` |
| 20 | `taobao.paimai.nft.orderinfo.query` |
| 21 | `taobao.auction.gov.get.bankinfo` |
| 22 | `taobao.auction.zc.merchant.user.check` |
| 23 | `taobao.auction.zc.update.vr.status` |
| 24 | `taobao.auction.titan.get.communitylist` |
| 25 | `taobao.auction.titan.get.carinfo` |
| 26 | `taobao.auction.zc.project.notice.list` |
| 27 | `taobao.paimai.pmp.identify.apply.query` |
| 28 | `taobao.paimai.auctionruby.task.query` |
| 29 | `taobao.paimai.auctionruby.task.promotion` |
| 30 | `taobao.paimai.auctionruby.order.query` |
| 31 | `taobao.auction.paimai.vehicle.callback` |
| 32 | `taobao.auction.zc.spec.bidder.fast.update` |
| 33 | `taobao.auction.paimai.loan.searchloanbank` |
| 34 | `taobao.auction.loan.online.buildloanorderno` |
| 35 | `taobao.auction.paimai.loan.getloanauctionbyitemid` |
| 36 | `taobao.auction.get.divison` |
| 37 | `taobao.auction.loan.online.sendmissedcallremindersms` |
| 38 | `taobao.auction.auctions.result.save` |

</details>

### 千牛接口

| # | API名称 |
|---|--------|
| 1 | `taobao.qianniu.task.message.send` |
| 2 | `taobao.qianniu.tasks.get` |
| 3 | `taobao.qianniu.task.cancel` |
| 4 | `taobao.qianniu.task.finish` |
| 5 | `taobao.qianniu.task.update` |
| 6 | `taobao.qianniu.taskmeta.update` |
| 7 | `taobao.qianniu.task.create` |
| 8 | `taobao.qianniu.tasks.count` |
| 9 | `taobao.qianniu.taskmetas.get` |
| 10 | `taobao.qianniu.task.remove` |
| 11 | `taobao.qianniu.number.put` |
| 12 | `taobao.qianniu.buyer.tag.get` |
| 13 | `taobao.qianniu.cloudkefu.onlinestatuslog.get` |
| 14 | `taobao.qncopilot.picture.audit` |

### 消息服务API

| # | API名称 |
|---|--------|
| 1 | `taobao.tmc.groups.get` |
| 2 | `taobao.tmc.group.delete` |
| 3 | `taobao.tmc.group.add` |
| 4 | `taobao.tmc.messages.confirm` |
| 5 | `taobao.tmc.messages.consume` |
| 6 | `taobao.tmc.message.produce` |
| 7 | `taobao.tmc.user.cancel` |
| 8 | `taobao.tmc.user.permit` |
| 9 | `taobao.tmc.user.get` |
| 10 | `taobao.tmc.messages.produce` |
| 11 | `taobao.tmc.queue.get` |
| 12 | `taobao.tmc.user.topics.get` |
| 13 | `taobao.tmc.topic.group.delete` |
| 14 | `taobao.tmc.topic.group.add` |
| 15 | `alibaba.lsy.miniapp.msg.push` |

### 本地生活API (87 APIs)

<details>
<summary>展开查看全部 87 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.place.storecategory.get` |
| 2 | `taobao.place.store.create` |
| 3 | `taobao.place.store.modify` |
| 4 | `taobao.place.store.delete` |
| 5 | `alibaba.alsc.crm.marketing.encrypt` |
| 6 | `alibaba.alsc.crm.marketing.share.customer.info` |
| 7 | `alibaba.alsc.crm.rule.querymdayerule` |
| 8 | `alibaba.alsc.crm.rule.queryjoinmrule` |
| 9 | `alibaba.alsc.crm.rule.querydishrule` |
| 10 | `alibaba.alsc.crm.rule.querygrowrule` |
| 11 | `alibaba.alsc.crm.rule.level.querylevelrule` |
| 12 | `alibaba.alsc.crm.rule.querytaglist` |
| 13 | `alibaba.alsc.crm.rule.querympricerule` |
| 14 | `alibaba.alsc.crm.card.active` |
| 15 | `alibaba.alsc.crm.card.open` |
| 16 | `alibaba.alsc.crm.point.querypointflow` |
| 17 | `alibaba.alsc.crm.point.cal` |
| 18 | `alibaba.alsc.crm.card.pagetmp` |
| 19 | `alibaba.alsc.crm.card.batch.sell` |
| 20 | `alibaba.alsc.crm.card.batch.active` |
| 21 | `alibaba.alsc.crm.card.searchcard` |
| 22 | `alibaba.alsc.crm.card.query.template` |
| 23 | `alibaba.alsc.crm.point.reversepoint` |
| 24 | `alibaba.alsc.crm.point.chkpntbypay` |
| 25 | `alibaba.alsc.crm.point.extra.consume` |
| 26 | `alibaba.alsc.crm.point.extracharge` |
| 27 | `alibaba.alsc.crm.point.consumepoint` |
| 28 | `alibaba.alsc.crm.customer.create` |
| 29 | `alibaba.alsc.crm.customer.update` |
| 30 | `alibaba.alsc.crm.customer.get` |
| 31 | `alibaba.alsc.crm.customer.resetppw` |
| 32 | `alibaba.alsc.crm.customer.checkppw` |
| 33 | `alibaba.alsc.crm.point.rule.get` |
| 34 | `alibaba.alsc.crm.recharge.dedutprecheck.get` |
| 35 | `alibaba.alsc.crm.recharge.unchargecheck.get` |
| 36 | `alibaba.alsc.crm.recharge.chargeprecheck.get` |
| 37 | `alibaba.alsc.crm.recharge.account.flowdetail.get` |
| 38 | `alibaba.alsc.crm.recharge.account.get` |
| 39 | `alibaba.alsc.crm.recharge.accountflows.get` |
| 40 | `alibaba.alsc.crm.recharge.undedut.update` |
| 41 | `alibaba.alsc.crm.recharge.dedut.update` |
| 42 | `alibaba.alsc.crm.recharge.uncharge.update` |
| 43 | `alibaba.alsc.crm.recharge.charge.update` |
| 44 | `alibaba.alsc.crm.recharge.qryrule` |
| 45 | `alibaba.alsc.crm.voucher.template.list` |
| 46 | `alibaba.alsc.crm.promotion.list` |
| 47 | `alibaba.alsc.crm.customer.voucher.list` |
| 48 | `alibaba.alsc.crm.menu.list` |
| 49 | `alibaba.alsc.crm.card.qry` |
| 50 | `alibaba.alsc.crm.customer.updateppw` |
| 51 | `alibaba.alsc.crm.marketing.issue.voucher` |
| 52 | `alibaba.alsc.crm.card.bindcard` |
| 53 | `alibaba.alsc.crm.rule.queryoptplan` |
| 54 | `alibaba.alsc.crm.voucher.status.change` |
| 55 | `alibaba.alsc.crm.card.bindcustomer` |
| 56 | `alibaba.alsc.crm.voucher.send` |
| 57 | `taobao.koubei.saas.base.operation.config.sync` |
| 58 | `alibaba.alsc.order.order.upload` |
| 59 | `alibaba.alsc.crm.card.qryphysical` |
| 60 | `taobao.place.store.extend.add` |
| 61 | `alibaba.alsc.crm.open.assert.verify` |
| 62 | `alibaba.alsc.crm.open.assert.refund` |
| 63 | `alibaba.alsc.crm.open.customer.get` |
| 64 | `alibaba.alsc.crm.open.customer.save` |
| 65 | `alibaba.alsc.crm.open.point.operate` |
| 66 | `alibaba.alsc.crm.open.rule.get` |
| 67 | `alibaba.alsc.crm.open.recharge.operate` |
| 68 | `alibaba.alsc.crm.open.order.backflow` |
| 69 | `alibaba.alsc.kms.access` |
| 70 | `alibaba.alsc.saas.codec.code.attrs.query` |
| 71 | `alibaba.alsc.consumerecord.sync` |
| 72 | `alibaba.alsc.chuda.template.send` |
| 73 | `alibaba.alsc.right.token.check` |
| 74 | `taobao.servindustry.finance.insurance.invoice.insurancenos` |
| 75 | `taobao.servindustry.finance.insurance.invoice.feedback` |
| 76 | `alibaba.alsc.growth.interactive.task.receivetask` |
| 77 | `alibaba.alsc.growth.interactive.task.pageviewtrigger` |
| 78 | `alibaba.alsc.growth.interactive.task.receivetaskprize` |
| 79 | `alibaba.alsc.growth.interactive.sns.converturl` |
| 80 | `alibaba.alsc.growth.interactive.link.genshortlink` |
| 81 | `alibaba.alsc.user.center.info.query` |
| 82 | `alibaba.alsc.notify.subscribe.query` |
| 83 | `alibaba.alsc.notify.subscribe.close` |
| 84 | `alibaba.alsc.notify.subscribe.open` |
| 85 | `alibaba.alsc.notify.subscribe.send` |
| 86 | `alibaba.misc.battery.incentive.get` |
| 87 | `alibaba.alsc.growth.interactive.task.trigger` |

</details>

### 阿里云ocsAPI

| # | API名称 |
|---|--------|
| 1 | `m-kvstore.aliyuncs.com.CreateInstance.2015-03-01` |
| 2 | `m-kvstore.aliyuncs.com.DescribeRegions.2015-03-01` |

### 淘宝同城API

| # | API名称 |
|---|--------|
| 1 | `taobao.cityretail.wmfl.convert.warehouse` |
| 2 | `tmall.cityretail.wmfl.order.logistics.query` |

### 房产API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihouse.laike.login.query` |
| 2 | `alibaba.alihouse.laike.permission.async` |

### YunOS

| # | API名称 |
|---|--------|
| 1 | `yunos.cosmo.data.push` |
| 2 | `aliyun.cosmo.gateway.invoke` |

### 阿里云API

| # | API名称 |
|---|--------|
| 1 | `account.aliyuncs.com.CreateApp.2013-07-01` |
| 2 | `account.aliyuncs.com.ListAppkeyByOwnerAndBid.2013-07-01` |
| 3 | `account.aliyuncs.com.CreateAliyunAccount.2013-07-01` |
| 4 | `slb.aliyuncs.com.SetLoadBalancerName.2013-02-21` |
| 5 | `slb.aliyuncs.com.DescribeBackendServers.2013-02-21` |
| 6 | `slb.aliyuncs.com.DeleteLoadBalancerListener.2013-02-21` |
| 7 | `odps.aliyuncs.com.DescribeOdpsService.2014-12-15` |
| 8 | `account.aliyuncs.com.CreateAppForBid.2013-07-01` |
| 9 | `account.aliyuncs.com.CreateAliyunAccountForBid.2013-07-01` |
| 10 | `account.aliyuncs.com.DeleteAppForBid.2013-07-01` |
| 11 | `push.aliyuncs.com.pushMsg.2015-03-18` |
| 12 | `push.aliyuncs.com.pushNotification.2015-03-18` |
| 13 | `push.aliyuncs.com.push.20150518` |

### 火车票API (42 APIs)

<details>
<summary>展开查看全部 42 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.train.agent.express.set` |
| 2 | `taobao.train.agent.bookticket.confirm.vtwo` |
| 3 | `taobao.train.agent.bookorders.get.vtwo` |
| 4 | `taobao.train.agent.returnorders.get.vtwo` |
| 5 | `taobao.train.agent.handleticket.confirm.vtwo` |
| 6 | `taobao.train.agent.order.get.vtwo` |
| 7 | `taobao.train.agent.returnticket.confirm.vtwo` |
| 8 | `taobao.train.agent.handrefund.refundfee` |
| 9 | `taobao.train.agent.returnticketinfo.get.vtwo` |
| 10 | `taobao.train.agent.ticket.status.callback` |
| 11 | `taobao.train.agent.order.query` |
| 12 | `taobao.train.agent.order.ignore` |
| 13 | `taobao.train.agent.order.lock` |
| 14 | `taobao.train.agent.order.confirm` |
| 15 | `taobao.train.agent.order.fail` |
| 16 | `taobao.train.stop.agent.callback` |
| 17 | `taobao.train.purchase.order.payurl` |
| 18 | `taobao.train.agent.changeissue.confirm.vtwo` |
| 19 | `taobao.train.agent.untreatedchange.query.vtwo` |
| 20 | `taobao.train.agent.changeorderdetail.query.vtwo` |
| 21 | `taobao.train.agent.freechildrendeal.confirm.vtwo` |
| 22 | `taobao.train.agent.freechildrenlist.query.vtwo` |
| 23 | `taobao.train.agent.freechildrendetail.query.vtwo` |
| 24 | `taobao.train.employement.order.query` |
| 25 | `taobao.train.agent.order.list` |
| 26 | `taobao.train.agent.reserveorderlist.query` |
| 27 | `taobao.train.agent.reserveorderoccupy.confirm` |
| 28 | `taobao.train.agent.reserveorderoccupy.fail` |
| 29 | `taobao.train.agent.occupyorder.query` |
| 30 | `taobao.train.agent.occupyorder.confirm.fail` |
| 31 | `taobao.train.agent.occupyorder.confirm.succ` |
| 32 | `taobao.train.agent.nate.callback.vtwo` |
| 33 | `taobao.train.agent.nate.cancel.vtwo` |
| 34 | `taobao.train.agent.query.transaction.vtwo` |
| 35 | `taobao.train.agent.refund.standalone.vtwo` |
| 36 | `taobao.train.agent.order.existnotcomplete` |
| 37 | `taobao.train.agent.order.occupy.vtwo` |
| 38 | `taobao.train.agent.change.occupy.vtwo` |
| 39 | `taobao.train.agent.refund.vtwo` |
| 40 | `taobao.train.agent.order.issue.vtwo` |
| 41 | `taobao.train.agent.change.issue.vtwo` |
| 42 | `taobao.train.agent.nate.confirm.vtwo` |

</details>

### Tanx API

| # | API名称 |
|---|--------|
| 1 | `taobao.tanx.nativetemplates.get` |

### 手淘开放API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.weitao.feed.isrelation` |
| 2 | `taobao.wireless.bunting.shop.shorturl.create` |
| 3 | `taobao.oauth.code.create` |
| 4 | `alibaba.interact.sensor.social` |
| 5 | `alibaba.interact.sensor.trade` |
| 6 | `alibaba.interact.lotteryactivity.register` |
| 7 | `alibaba.interact.allsparkisv.draw` |
| 8 | `alibaba.interact.aopdata.register` |
| 9 | `alibaba.interact.sensor.trade.buy` |
| 10 | `alibaba.interact.media.artwork` |
| 11 | `alibaba.interact.media.audio` |
| 12 | `taobao.weitao.follow.isrelation` |
| 13 | `taobao.logistics.fengchao.msg.send` |
| 14 | `taobao.logistics.taowai.msg.send` |
| 15 | `taobao.logistics.applet.modifydata.save` |
| 16 | `taobao.logistics.applet.package.query` |
| 17 | `taobao.logistics.openalibity.write` |

</details>

### 阿里高德

| # | API名称 |
|---|--------|
| 1 | `alibaba.amap.call.outcall.sync` |

### 宝点API

| # | API名称 |
|---|--------|
| 1 | `taobao.baodian.deposit.get` |
| 2 | `taobao.baodian.server.date.get` |
| 3 | `taobao.baodian.server.sdk.config.get` |
| 4 | `taobao.deg.user.gamegift.query` |
| 5 | `taobao.baodian.deposit.get.with.sdkversion` |

### 汽车票API (43 APIs)

<details>
<summary>展开查看全部 43 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.bus.agent.bookticket.confirm` |
| 2 | `taobao.bus.agent.city.change` |
| 3 | `taobao.bus.refundticketprice.set` |
| 4 | `taobao.bus.lastplace.get` |
| 5 | `taobao.bus.busnumber.get` |
| 6 | `taobao.bus.seatprice.get` |
| 7 | `taobao.bus.order.set` |
| 8 | `taobao.bus.city.get` |
| 9 | `taobao.bus.ticket.set` |
| 10 | `taobao.bus.cancleorder.set` |
| 11 | `taobao.bus.order.get` |
| 12 | `taobao.bus.busnumber.set` |
| 13 | `taobao.bus.tvmcreateorder.set` |
| 14 | `taobao.bus.disableqrcode.set` |
| 15 | `taobao.bus.tvmpayorder.set` |
| 16 | `taobao.bus.tvmqueryorder.get` |
| 17 | `taobao.bus.tvmbookorder.set` |
| 18 | `taobao.bus.tvmcancelorder.set` |
| 19 | `taobao.bus.tvmcreateqrcode.set` |
| 20 | `taobao.bus.tvmrefundorder.set` |
| 21 | `taobao.bus.historyorder.get` |
| 22 | `taobao.bus.refundfee.get` |
| 23 | `taobao.bus.refund.set` |
| 24 | `taobao.bus.numbers.update` |
| 25 | `taobao.bus.agent.refundticket.confirm` |
| 26 | `taobao.bus.agent.returnticket.confirm` |
| 27 | `taobao.bus.agent.refund.confirm` |
| 28 | `taobao.bus.numbers.stockprice.update` |
| 29 | `taobao.bus.invoice.return` |
| 30 | `taobao.bus.agent.multiple.refund.confirm` |
| 31 | `taobao.alitrip.bus.tickets.insurance.recommend` |
| 32 | `taobao.bus.merchant.order.get` |
| 33 | `alitrip.bus.insurance.recommend` |
| 34 | `taobao.bus.item.notify` |
| 35 | `taobao.bus.order.scheduleinfo.update` |
| 36 | `taobao.bus.station.get` |
| 37 | `taobao.bus.route.get` |
| 38 | `taobao.bus.number.get` |
| 39 | `taobao.bus.order.create` |
| 40 | `taobao.bus.order.close` |
| 41 | `taobao.bus.ticket.refund` |
| 42 | `taobao.bus.billdetail.get` |
| 43 | `taobao.bus.billtotal.get` |

</details>

### 码上淘API

| # | API名称 |
|---|--------|
| 1 | `taobao.ma.qrcode.common.create` |
| 2 | `taobao.wireless.xcode.create` |

### 游戏激励平台API

| # | API名称 |
|---|--------|
| 1 | `taobao.de.activity.info.get` |
| 2 | `taobao.de.activity.luckydraw` |
| 3 | `taobao.de.activity.machineid.get` |
| 4 | `taobao.de.activity.delivery.addr.confirm` |

### 淘宝抽奖平台API

| # | API名称 |
|---|--------|
| 1 | `taobao.de.activity.securitytoken.apply` |

### 天猫国际API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.hk.clearance.get` |
| 2 | `tmall.traceplatform.ccic.tracecode.check` |
| 3 | `tmall.traceplatform.awdc.info.upload` |
| 4 | `tmall.traceplatform.cts.info.upload` |
| 5 | `tmall.traceplatform.cts.order.stop` |
| 6 | `tmall.traceplatform.ticket.order.upload` |
| 7 | `tmall.traceplatform.ticket.picture.upload` |
| 8 | `taobao.cco.self.coordinate.handle.finish` |
| 9 | `tmall.hk.clearance.certification.get` |
| 10 | `tmall.hk.clearance.info.send` |
| 11 | `tmall.hk.clearance.order.get` |
| 12 | `taobao.cco.self.coordinate.break.order` |
| 13 | `tmall.hk.distribute.clearance.certification.get` |
| 14 | `tmall.hk.distribute.clearance.info.send` |
| 15 | `tmall.hk.distribute.logistics.detail.send` |
| 16 | `tmall.hk.trade.order.confirm` |
| 17 | `tmall.hk.clearance.declare.wechat` |

</details>

### 司法拍卖

| # | API名称 |
|---|--------|
| 1 | `taobao.auction.gov.category.get` |
| 2 | `taobao.auction.gov.publish.upload.attachfile` |
| 3 | `taobao.auction.gov.publish.upload.pic` |
| 4 | `taobao.auction.gov.get.division` |
| 5 | `taobao.auction.zc.project.public` |
| 6 | `taobao.auction.gov.get.latestbid` |
| 7 | `taobao.auction.gov.data.realtime.get` |
| 8 | `taobao.auction.gov.data.monthly.get` |
| 9 | `taobao.auction.gov.data.annually.get` |
| 10 | `taobao.auction.gov.data.topn.get` |

### 虾米API

| # | API名称 |
|---|--------|
| 1 | `alibaba.xiami.api.radio.myself.get` |

### 天猫互动接口 (46 APIs)

<details>
<summary>展开查看全部 46 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.interact.sensor.gravity` |
| 2 | `alibaba.interact.sensor.gyro` |
| 3 | `alibaba.interact.sensor.shake` |
| 4 | `alibaba.interact.sensor.blow` |
| 5 | `alibaba.interact.sensor.networkstatus` |
| 6 | `alibaba.interact.sensor.authorize` |
| 7 | `alibaba.interact.sensor.login` |
| 8 | `alibaba.interact.sensor.share` |
| 9 | `alibaba.interact.sensor.titlebarhide` |
| 10 | `alibaba.interact.sensor.takephoto` |
| 11 | `alibaba.interact.sensor.calendar` |
| 12 | `alibaba.interact.sensor.toast` |
| 13 | `alibaba.interact.sensor.openwindow` |
| 14 | `alibaba.interact.sensor.vibrate` |
| 15 | `alibaba.interact.sensor.audio` |
| 16 | `alibaba.interact.activity.register` |
| 17 | `alibaba.interact.activity.unregister` |
| 18 | `alibaba.interact.sensor.popwindow` |
| 19 | `alibaba.interact.sensor.gcanvas` |
| 20 | `alibaba.interact.sensor.gmedia` |
| 21 | `alibaba.interact.sensor.gutil` |
| 22 | `alibaba.interact.sensor.glue` |
| 23 | `alibaba.interact.isv.gateway` |
| 24 | `alibaba.interact.sensor.ma` |
| 25 | `alibaba.interact.coin.buyer.add` |
| 26 | `alibaba.interact.sensor.wangwang` |
| 27 | `alibaba.interact.sensor.makeup` |
| 28 | `taobao.weitao.feed.synchronize` |
| 29 | `alibaba.interact.onecode.issue` |
| 30 | `alibaba.interact.ump.meal.query` |
| 31 | `alibaba.interact.sensor.favorites` |
| 32 | `alibaba.interact.current.mixusernick` |
| 33 | `alibaba.interact.shop.favor` |
| 34 | `alibaba.interact.activity.apply` |
| 35 | `alibaba.interact.activity.pushtoalicom` |
| 36 | `taobao.weitao.feed.cancel` |
| 37 | `taobao.weitao.feed.synchronize.new` |
| 38 | `alibaba.interact.wireless.draw` |
| 39 | `alibaba.interact.activity.addcomment` |
| 40 | `alibaba.interact.isvlottery.isvdraw` |
| 41 | `alibaba.interact.login.alipayauth` |
| 42 | `taobao.mixnick.wetoplay` |
| 43 | `alibaba.interact.coupon.apply` |
| 44 | `taobao.mixnick.playtowe` |
| 45 | `alibaba.interact.user.islogin` |
| 46 | `alibaba.fc.mallx.interaction.ai.pic.list` |

</details>

### 生活服务API

| # | API名称 |
|---|--------|
| 1 | `taobao.place.store.relation.add` |

### 物联API

| # | API名称 |
|---|--------|
| 1 | `aliyun.alink.opendata.url.query` |
| 2 | `alibaba.alink.device.bind` |
| 3 | `alibaba.alink.device.detail.get` |
| 4 | `alibaba.alink.message.config.set` |
| 5 | `alibaba.alink.message.config.list` |
| 6 | `alibaba.alink.message.history.count` |
| 7 | `alibaba.alink.message.history.list` |
| 8 | `alibaba.alink.device.info.update` |
| 9 | `alibaba.alink.device.unbind` |
| 10 | `aliyun.alink.data.stat.report` |
| 11 | `alibaba.alink.device.unify.status.set` |
| 12 | `alibaba.alink.device.unify.status.get` |

### 酒店导购API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.city.get` |
| 2 | `taobao.xhotel.info.list.get` |
| 3 | `alitrip.hotel.rate.getmixratelist.get` |
| 4 | `taobao.xhotel.price.get.for.hello` |
| 5 | `taobao.xhotel.info.list.get.for.hello` |
| 6 | `taobao.xhotel.distribution.price` |
| 7 | `taobao.xhotel.distribution.info` |
| 8 | `taobao.xhotel.distribution.realtime.price` |
| 9 | `taobao.xhotel.distribution.stdinfo.get` |
| 10 | `taobao.xhotel.distribution.priceinput` |

### 保险API

| # | API名称 |
|---|--------|
| 1 | `alipay.baoxian.claim.uploadattachment` |
| 2 | `alipay.baoxian.claim.update` |
| 3 | `alipay.baoxian.claim.returngoodsstatus.update` |
| 4 | `alipay.baoxian.claim.survey.conclusion.submit` |
| 5 | `alipay.baoxian.localreturn.issue` |
| 6 | `alipay.baoxian.localreturn.claimapply` |
| 7 | `alipay.baoxian.localreturn.claimassess` |
| 8 | `alipay.baoxian.localreturn.claimpay` |
| 9 | `alipay.baoxian.localreturn.claimcancel` |

### 天猫美妆API

| # | API名称 |
|---|--------|
| 1 | `tmall.mei.crm.member.sync` |
| 2 | `tmall.mei.crm.callback.point.change` |
| 3 | `tmall.crm.member.front.unbind` |
| 4 | `tmall.crm.member.point.change` |
| 5 | `tmall.mei.crm.member.getbypaycode` |
| 6 | `tmall.crm.member.front.unbind.privy` |
| 7 | `tmall.mei.crm.member.sync.privy` |

### 电子面单API (37 APIs)

<details>
<summary>展开查看全部 37 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.wlb.waybill.i.get` |
| 2 | `taobao.wlb.waybill.i.search` |
| 3 | `taobao.wlb.waybill.i.fullupdate` |
| 4 | `taobao.wlb.waybill.i.print` |
| 5 | `taobao.wlb.waybill.i.querydetail` |
| 6 | `taobao.wlb.waybill.i.cancel` |
| 7 | `taobao.wlb.waybill.i.product` |
| 8 | `cainiao.cloudprint.stdtemplates.get` |
| 9 | `cainiao.cloudprint.mystdtemplates.get` |
| 10 | `cainiao.waybill.ii.product` |
| 11 | `cainiao.waybill.ii.cancel` |
| 12 | `cainiao.cloudprint.customares.get` |
| 13 | `cainiao.waybill.ii.get` |
| 14 | `cainiao.waybill.ii.update` |
| 15 | `cainiao.cloudprint.clientinfo.put` |
| 16 | `cainiao.waybill.ii.query.by.tradecode` |
| 17 | `cainiao.waybill.ii.query.by.waybillcode` |
| 18 | `cainiao.cloudprint.isvtemplates.get` |
| 19 | `cainiao.waybill.ii.search` |
| 20 | `cainiao.cloudprint.isv.resources.get` |
| 21 | `cainiao.cloudprint.templates.migrate` |
| 22 | `cainiao.cloudprint.customarea.update` |
| 23 | `cainiao.cloudprint.single.customarea.get` |
| 24 | `cainiao.smartdelivery.strategy.warehouse.i.update` |
| 25 | `cainiao.smartdelivery.strategy.warehouse.i.delete` |
| 26 | `cainiao.waybill.privacy.subscription.get` |
| 27 | `cainiao.waybill.privacy.seller.order.get` |
| 28 | `cainiao.waybill.ii.logisticsdetail.url.get` |
| 29 | `cainiao.waybill.ii.confirm` |
| 30 | `cainiao.waybill.ii.delivery` |
| 31 | `cainiao.waybill.address.reachable.query` |
| 32 | `taobao.logistics.routing.sortingcode.config` |
| 33 | `taobao.logistics.routing.precise.query` |
| 34 | `taobao.logistics.routing.keyword.query` |
| 35 | `taobao.logistics.routing.contractmapping.query` |
| 36 | `taobao.logistics.reach.trade.interrupt.stat.query` |
| 37 | `taobao.wlb.waybill.detail.query` |

</details>

### 电影票API

| # | API名称 |
|---|--------|
| 1 | `taobao.film.tfbackyard.cardschedule.update` |
| 2 | `taobao.film.data.third.party.refund.order` |
| 3 | `taobao.film.lottery.sendcode` |
| 4 | `taobao.film.account.phone.query` |
| 5 | `taobao.film.lottery.performance` |
| 6 | `alibaba.damai.perform.tfinteraction.task.query` |
| 7 | `taobao.film.lottery.performance.invalid` |
| 8 | `alibaba.damai.perform.tfinteraction.task.draw` |
| 9 | `taobao.film.lottery.performance.config.query` |

### 阿里通信API (53 APIs)

<details>
<summary>展开查看全部 53 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.aliqin.flow.publish` |
| 2 | `alibaba.aliqin.tcc.trade.identity.get` |
| 3 | `alibaba.aliqin.flow.wallet.grade` |
| 4 | `alibaba.aliqin.flow.wallet.charge` |
| 5 | `alibaba.aliqin.flow.wallet.query.charge` |
| 6 | `alibaba.aliqin.ta.sms.num.send` |
| 7 | `alibaba.aliqin.ta.sms.num.query` |
| 8 | `alibaba.tianji.supplier.order.result` |
| 9 | `alibaba.aliqin.flow.wallet.charge.rule` |
| 10 | `alibaba.tianji.distributor.order.submit` |
| 11 | `alibaba.wtt.user.regioninfo.byip.get` |
| 12 | `alibaba.aliqin.ta.number.singlecallbyvoice` |
| 13 | `alibaba.aliqin.ta.number.singlecallbytts` |
| 14 | `alibaba.aliqin.fc.voice.record.geturl` |
| 15 | `alibaba.aliqin.flow.wallet.consume` |
| 16 | `taobao.wt.trade.order.resultcallback` |
| 17 | `alibaba.base.order.supplier.notify` |
| 18 | `alibaba.aliqin.ta.voice.num.doublecall` |
| 19 | `alibaba.aliqin.flow.alipay.publish` |
| 20 | `alibaba.aliqin.flow.alipay.isbindingtbaccount` |
| 21 | `alibaba.interact.order.checkuserimei` |
| 22 | `alibaba.aliqin.fc.voice.num.cancelcall` |
| 23 | `alibaba.alicom.order.checkorderinfo` |
| 24 | `alibaba.aliqin.axb.vendor.push.call.release` |
| 25 | `alibaba.aliqin.axb.vendor.call.control` |
| 26 | `alibaba.aliqin.axb.vendor.sms.intercept` |
| 27 | `alibaba.aliqin.fc.voice.getdetail` |
| 28 | `alibaba.aliqin.axb.vendor.heart.beat` |
| 29 | `alibaba.aliqin.axb.vendor.exception.no.sync` |
| 30 | `alibaba.alicom.order.preauthorize.create` |
| 31 | `alibaba.alicom.order.preauthorize.query.fund` |
| 32 | `alibaba.aliqin.axb.vendor.push.call.event` |
| 33 | `alibaba.alicom.vt.distributeorder.create` |
| 34 | `alibaba.alicom.vt.distribute.sendcode` |
| 35 | `alibaba.alicom.vt.distribute.queryprotocol` |
| 36 | `taobao.phone.item.external.recommend` |
| 37 | `taobao.phone.order.external.create` |
| 38 | `taobao.phone.order.external.status` |
| 39 | `taobao.virtual.dsf.supplier.interface.switch` |
| 40 | `taobao.flow.order.external.create` |
| 41 | `taobao.flow.order.identifycode.get` |
| 42 | `alibaba.aliqin.tcc.trade.identity.newget` |
| 43 | `taobao.flow.order.qualified.offer.get` |
| 44 | `taobao.flow.order.external.verify` |
| 45 | `taobao.simcard.order.external.create` |
| 46 | `taobao.simcard.salenumber.select` |
| 47 | `taobao.simard.order.external.status` |
| 48 | `taobao.flow.token.external.create` |
| 49 | `taobao.simcard.agreement.query` |
| 50 | `taobao.simcard.contract.sync` |
| 51 | `taobao.simcard.contract.delete` |
| 52 | `taobao.simcard.plan.get` |
| 53 | `taobao.simcard.config.get` |

</details>

### 阿里妈妈API

| # | API名称 |
|---|--------|
| 1 | `taobao.brandonebp.rpt.campaign.get` |

### openimAPI (22 APIs)

<details>
<summary>展开查看全部 22 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.openim.ioscert.sandbox.set` |
| 2 | `taobao.openim.relations.get` |
| 3 | `taobao.openim.chatlogs.get` |
| 4 | `taobao.openim.tribe.create` |
| 5 | `taobao.openim.tribe.gettribeinfo` |
| 6 | `taobao.openim.tribe.quit` |
| 7 | `taobao.openim.tribe.join` |
| 8 | `taobao.openim.tribe.expel` |
| 9 | `taobao.openim.tribe.setmanager` |
| 10 | `taobao.openim.tribe.dismiss` |
| 11 | `taobao.openim.tribe.invite` |
| 12 | `taobao.openim.tribe.getmembers` |
| 13 | `taobao.openim.tribe.unsetmanager` |
| 14 | `taobao.openim.tribe.getalltribes` |
| 15 | `taobao.openim.tribe.modifytribeinfo` |
| 16 | `taobao.openim.app.chatlogs.get` |
| 17 | `taobao.openim.snfilterword.setfilter` |
| 18 | `taobao.openim.tribelogs.get` |
| 19 | `taobao.openim.tribe.setmembernick` |
| 20 | `taobao.openim.tribelogs.import` |
| 21 | `taobao.openim.chatlogs.import` |
| 22 | `taobao.openim.tribe.sendmsg` |

</details>

### DSP-API (16 APIs)

<details>
<summary>展开查看全部 16 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.yt.wt.order.data.pull` |
| 2 | `alibaba.alihealth.yt.wt.ad.plan.save` |
| 3 | `alibaba.alihealth.yt.wt.media.report` |
| 4 | `alibaba.alihealth.yt.wt.ad.algoreport.openorclose` |
| 5 | `alibaba.alihealth.yt.wt.media.report.switch` |
| 6 | `alibaba.alihealth.yt.wt.ad.algoreport.data.pull` |
| 7 | `alibaba.alihealth.yt.wt.ad.algobid.suggest` |
| 8 | `alibaba.alihealth.yt.wt.ad.algobid.query` |
| 9 | `alibaba.alihealth.yt.wt.ad.algobid.save` |
| 10 | `alibaba.alihealth.yt.wt.media.rta.bind` |
| 11 | `alibaba.alihealth.yt.wt.media.unauthorized.account.query` |
| 12 | `alibaba.alihealth.yt.wt.media.ocpx.effect.query` |
| 13 | `alibaba.alihealth.yt.wt.ad.allowance.query` |
| 14 | `alibaba.alihealth.yt.wt.media.rta.query` |
| 15 | `alibaba.alihealth.yt.wt.ad.allowance.switch` |
| 16 | `alibaba.alihealth.yt.wt.media.cut.report` |

</details>

### 虚拟院线API

| # | API名称 |
|---|--------|
| 1 | `youku.tv.desktop.toyou.recommend` |
| 2 | `taobao.taotv.carousel.channel.all` |
| 3 | `taobao.taotv.carousel.category.list` |
| 4 | `taobao.taotv.carousel.playlist.get` |
| 5 | `taobao.taotv.video.playlist.get` |
| 6 | `taobao.taotv.video.playlist.all` |
| 7 | `taobao.taotv.video.playlist.ottnav.get` |
| 8 | `taobao.taotv.video.playlist.page` |

### 知识库API

| # | API名称 |
|---|--------|
| 1 | `alibaba.kclub.kc.getcategorytree` |
| 2 | `alibaba.kclub.kc.qa.get` |
| 3 | `alibaba.kclub.kc.queryknowledge` |
| 4 | `alibaba.kclub.kc.qa.search` |
| 5 | `alibaba.kclub.kc.qa.search.page` |

### 反欺诈风控API

| # | API名称 |
|---|--------|
| 1 | `taobao.collinafacade.nocaptcha.sig.authenticate` |
| 2 | `taobao.antifraud.riskassessment.get` |
| 3 | `taobao.antifraud.riskuser.get` |

### 国际站外贸直通车API (40 APIs)

<details>
<summary>展开查看全部 40 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.scbp.ad.campaign.find.forbidden.keyword` |
| 2 | `alibaba.scbp.ad.campaign.update` |
| 3 | `alibaba.scbp.ad.campaign.delete` |
| 4 | `alibaba.scbp.ad.campaign.create` |
| 5 | `alibaba.scbp.ad.campaign.find.campaign.page` |
| 6 | `alibaba.scbp.ad.target.tag.estimate.uv` |
| 7 | `alibaba.scbp.ad.campaign.find.real.cost` |
| 8 | `alibaba.scbp.ad.campaign.find.campaign.effect` |
| 9 | `alibaba.scbp.ad.target.tag.find.campaign.target.tag` |
| 10 | `alibaba.scbp.ad.group.delete.forbidden.product` |
| 11 | `alibaba.scbp.ad.keyword.get.keyword.count.by.query` |
| 12 | `alibaba.scbp.ad.keyword.list.campaign.keywords` |
| 13 | `alibaba.scbp.ad.keyword.update.keyword.price.batch` |
| 14 | `alibaba.scbp.ad.keyword.create.keyword.batch` |
| 15 | `alibaba.scbp.ad.report.get.account.report` |
| 16 | `alibaba.scbp.ad.keyword.delete.keyword.batch` |
| 17 | `alibaba.scbp.ad.report.get.product.report` |
| 18 | `alibaba.scbp.ad.report.query.keyword.effect` |
| 19 | `alibaba.scbp.ad.group.find.forbidden.product` |
| 20 | `alibaba.scbp.ad.group.count.ad.group` |
| 21 | `alibaba.scbp.ad.group.create.forbidden.product` |
| 22 | `alibaba.scbp.ad.group.create.ad.group.batch` |
| 23 | `alibaba.scbp.ad.group.update.ad.group.batch` |
| 24 | `alibaba.scbp.ad.group.find.ad.group` |
| 25 | `alibaba.scbp.ad.group.delete.ad.group.batch` |
| 26 | `alibaba.scbp.ad.target.tag.merge.campaign.target.tag` |
| 27 | `alibaba.scbp.ad.report.get.target.report` |
| 28 | `alibaba.scbp.ad.campaign.delete.forbidden.keyword` |
| 29 | `alibaba.scbp.ad.report.query.single.keyword.effect` |
| 30 | `alibaba.scbp.ad.keyword.update.keyword.status.batch` |
| 31 | `alibaba.scbp.ad.campaign.create.forbidden.keyword` |
| 32 | `alibaba.scbp.ad.target.tag.get.all.enable.tag.list` |
| 33 | `alibaba.scbp.ad.customer.find.customer.info` |
| 34 | `alibaba.scbp.ad.keyword.list.relevant.products` |
| 35 | `alibaba.scbp.ad.keyword.operation.preferential.product` |
| 36 | `alibaba.scbp.ad.group.recommend.product` |
| 37 | `alibaba.scbp.ad.report.get.last.effect.date` |
| 38 | `alibaba.scbp.ad.keyword.recommend.word` |
| 39 | `alibaba.scbp.ad.target.tag.list.recommend.tag` |
| 40 | `alibaba.scbp.ad.keyword.recommend.price` |

</details>

### 天猫服务数据API (81 APIs)

<details>
<summary>展开查看全部 81 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.servicecenter.anomalyrecourse.remark.update` |
| 2 | `tmall.servicecenter.anomalyrecourse.search` |
| 3 | `tmall.servicecenter.servicestore.createservicestorecoverservice` |
| 4 | `tmall.servicecenter.servicestore.createservicestorecapacity` |
| 5 | `tmall.servicecenter.servicestore.updateservicestorecoverservice` |
| 6 | `tmall.servicecenter.servicestore.updateservicestorecapacity` |
| 7 | `tmall.servicecenter.servicestore.deleteservicestorecapacity` |
| 8 | `alibaba.service.settlement.query` |
| 9 | `tmall.servicecenter.workcard.refuse` |
| 10 | `tmall.servicecenter.workcard.delivery` |
| 11 | `tmall.servicecenter.workcard.logisticsinfo.create` |
| 12 | `tmall.servicecenter.workcard.serviceprogress.update` |
| 13 | `tmall.servicecenter.workcard.tpconfirm` |
| 14 | `tmall.servicecenter.workcard.logisticsinfo.update` |
| 15 | `tmall.servicecenter.anomalyrecourse.close` |
| 16 | `alibaba.servicecenter.workcard.servicesku.suggest` |
| 17 | `alibaba.servicecenter.workcard.relatedsku.query` |
| 18 | `alibaba.servicecenter.workcard.confirmedsku.query` |
| 19 | `alibaba.servicecenter.workcard.evaluate` |
| 20 | `alibaba.ssc.purchase.product.query` |
| 21 | `alibaba.ssc.purchase.servicedefinition.param.query` |
| 22 | `alibaba.ssc.business.serviceprice.query` |
| 23 | `tmall.serivcecenter.servicerorder.insurance.callback` |
| 24 | `tmall.serivcecenter.workcard.insurance.claim` |
| 25 | `tmall.servicecenter.anomalyrecourse.homedecoration.appeal` |
| 26 | `tmall.servicecenter.anomalyrecourse.homedecoration.admit` |
| 27 | `tmall.servicecenter.anomalyrecourse.homedecoration.close` |
| 28 | `tmall.servicecenter.anomalyrecourse.homedecoration.response` |
| 29 | `tmall.servicecenter.anomalyrecourse.homedecoration.questioncode.query` |
| 30 | `alibaba.msfservice.audits.update` |
| 31 | `alibaba.msfservice.worker.queryid` |
| 32 | `tmall.fuwu.rate.get` |
| 33 | `tmall.servicecenter.callrecord.query` |
| 34 | `alibaba.msfservice.identifytask.resendidentifycode` |
| 35 | `alibaba.msfservice.extrafee.queryextrafeeitemlist` |
| 36 | `alibaba.msfservice.identifytask.querydetail` |
| 37 | `alibaba.msfservice.extrafee.createextrafeerecord` |
| 38 | `alibaba.msfservice.identifytask.querycount` |
| 39 | `alibaba.msfservice.extrafee.queryextrafeerecorddetail` |
| 40 | `alibaba.msfservice.identifytask.suspend` |
| 41 | `alibaba.msfservice.identifytask.reject` |
| 42 | `alibaba.msfservice.identifytask.accept` |
| 43 | `alibaba.msfservice.extrafee.computrecordamount` |
| 44 | `alibaba.msfservice.identifytask.reserve` |
| 45 | `alibaba.msfservice.identifytask.identify` |
| 46 | `alibaba.msfservice.telephone.getprivatephonebyidentifytaskid` |
| 47 | `alibaba.msfservice.feedback.getfeedbackurl` |
| 48 | `alibaba.msfservice.identifytask.querywaveinfo` |
| 49 | `alibaba.msfservice.identifytask.updateserviceprogress` |
| 50 | `alibaba.msfservice.identifytask.signincheck` |
| 51 | `alibaba.msfservice.identifytask.querylist` |
| 52 | `alibaba.msfservice.identifytask.signin` |
| 53 | `alibaba.msfservice.identifytask.signinpre` |
| 54 | `alibaba.msfservice.identifytask.workersignin` |
| 55 | `alibaba.msfservice.identifytask.workersignincheck` |
| 56 | `alibaba.msfservice.worker.register` |
| 57 | `alibaba.msfservice.identifytask.queryidentifytaskidbyworkcardid` |
| 58 | `alibaba.msfservice.identifytask.verifyidentifycode` |
| 59 | `alibaba.msfservice.identifytask.upload` |
| 60 | `alibaba.msfservice.identifytask.queryidentifytaskinfobyworkcardid` |
| 61 | `alibaba.msfservice.workcard.reserve` |
| 62 | `alibaba.msfservice.workcard.signin` |
| 63 | `alibaba.msfservice.workcard.querywaveinfo` |
| 64 | `alibaba.msfservice.workcard.suspend` |
| 65 | `alibaba.msfservice.workcard.identify` |
| 66 | `alibaba.msfservice.workcard.reject` |
| 67 | `alibaba.msfservice.feedback.generatefeedbackurl` |
| 68 | `alibaba.yichao.insurance.updatestatus` |
| 69 | `alibaba.yichao.insurance.order.update` |
| 70 | `alibaba.yichao.insurance.order.query` |
| 71 | `alibaba.yichao.service.measures.query` |
| 72 | `alibaba.msfservice.telephone.getprivatephone` |
| 73 | `alibaba.ssc.homedecoration.customerservice.register` |
| 74 | `alibaba.ssc.homedecoration.customerservice.update` |
| 75 | `alibaba.ssc.homedecoration.customerservice.delete` |
| 76 | `alibaba.ssc.homedecoration.workcard.logistics.update` |
| 77 | `alibaba.yichao.report.confirm` |
| 78 | `alibaba.yichao.claim.confirm` |
| 79 | `alibaba.yichao.report.query` |
| 80 | `alibaba.ssc.yichao.insurer.claim.query` |
| 81 | `alibaba.ssc.homedecoration.purchase.getqrcodeurl` |

</details>

### 智能设备 (43 APIs)

<details>
<summary>展开查看全部 43 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.ailab.aicloud.top.device.authcode.get` |
| 2 | `taobao.ailab.aicloud.top.device.authresult.get` |
| 3 | `taobao.ailab.aicloud.top.auth.get` |
| 4 | `taobao.ailab.aicloud.top.device.unbind` |
| 5 | `taobao.ailab.aicloud.top.auth.logout` |
| 6 | `taobao.ailab.aicloud.top.message.send` |
| 7 | `taobao.ailab.aicloud.top.message.list` |
| 8 | `taobao.ailab.aicloud.top.message.get.unread.count` |
| 9 | `taobao.ailab.aicloud.top.device.control.custom` |
| 10 | `taobao.ailab.aicloud.top.device.control.lamp` |
| 11 | `taobao.ailab.aicloud.top.device.settings.reset` |
| 12 | `taobao.ailab.aicloud.top.device.control.pauseandresume` |
| 13 | `taobao.ailab.aicloud.top.device.control.volume` |
| 14 | `taobao.ailab.aicloud.top.device.control.playurl` |
| 15 | `taobao.ailab.aicloud.top.device.control.childlock` |
| 16 | `taobao.ailab.aicloud.top.device.control.hibernation` |
| 17 | `taobao.ailab.aicloud.top.like.list` |
| 18 | `taobao.ailab.aicloud.top.like.add` |
| 19 | `taobao.ailab.aicloud.top.feedlist.get` |
| 20 | `taobao.ailab.aicloud.top.like.delete` |
| 21 | `taobao.ailab.aicloud.top.device.getstatus` |
| 22 | `taobao.ailab.aicloud.top.feedlist.delete` |
| 23 | `taobao.ailab.aicloud.top.freelisten.childrenalbum` |
| 24 | `taobao.ailab.aicloud.top.message.addtext` |
| 25 | `taobao.ailab.aicloud.top.device.control.playbyid` |
| 26 | `taobao.ailab.aicloud.smarthome.top.genielink.reportdevice` |
| 27 | `alibaba.ailabs.aligenie.iot.device.control.result` |
| 28 | `tmall.device.store.followurl.get` |
| 29 | `taobao.ailab.aicloud.top.like.filter` |
| 30 | `alibaba.ailabs.aligenie.albums.search` |
| 31 | `alibaba.ailabs.aligenie.tracks.search` |
| 32 | `alibaba.ailabs.aligenie.albums.get` |
| 33 | `taobao.ailab.aicloud.top.device.openid.authresult.get` |
| 34 | `taobao.ailab.aicloud.top.device.openid.authcode.get` |
| 35 | `taobao.ailab.aicloud.top.device.openid.unbind` |
| 36 | `taobao.ailab.aicloud.top.device.deviceid.convert` |
| 37 | `taobao.ailab.aicloud.top.device.extinfo.get` |
| 38 | `taobao.ailab.aicloud.top.device.statusinfo.get` |
| 39 | `taobao.ailab.aicloud.top.device.detailinfo.get` |
| 40 | `alibaba.ailabs.iot.business.recipe.getdetail` |
| 41 | `alibaba.ailabs.iot.business.recipe.getpage` |
| 42 | `alibaba.ailabs.iot.business.recipe.insertorupdate` |
| 43 | `alibaba.ailabs.iot.business.recipestep.insertorupdate` |

</details>

### 百川 (30 APIs)

<details>
<summary>展开查看全部 30 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.baichuan.user.login` |
| 2 | `taobao.baichuan.user.logindoublecheck` |
| 3 | `taobao.baichuan.user.loginbytoken` |
| 4 | `taobao.baichuan.orderurl.get` |
| 5 | `taobao.baichuan.payresult.query` |
| 6 | `taobao.baichuan.taoke.trace` |
| 7 | `taobao.baichuan.openaccount.loginbytoken` |
| 8 | `taobao.baichuan.openaccount.login` |
| 9 | `taobao.baichuan.openaccount.resetcode.check` |
| 10 | `taobao.baichuan.openaccount.logindoublecheck` |
| 11 | `taobao.baichuan.openaccount.newlogindoublecheck` |
| 12 | `taobao.baichuan.openaccount.register` |
| 13 | `taobao.baichuan.openaccount.registercode.send` |
| 14 | `taobao.baichuan.openaccount.registercode.check` |
| 15 | `taobao.baichuan.openaccount.resetcode.send` |
| 16 | `taobao.baichuan.openaccount.password.reset` |
| 17 | `taobao.baichuan.item.subscribe.relation.query` |
| 18 | `taobao.baichuan.items.subscribe` |
| 19 | `taobao.baichuan.item.subscribe` |
| 20 | `taobao.baichuan.items.unsubscribe` |
| 21 | `taobao.baichuan.items.unsubscribe.by.condition` |
| 22 | `taobao.baichuan.item.subscribe.daily.left.query` |
| 23 | `alibaba.baichuan.ctg.content.get` |
| 24 | `alibaba.baichuan.ctg.video.upload` |
| 25 | `alibaba.baichuan.ctg.user.relation` |
| 26 | `alibaba.baichuan.taopassword.query` |
| 27 | `alibaba.baichuan.aso.query` |
| 28 | `alibaba.baichuan.aso.activate` |
| 29 | `alibaba.baichuan.taopassword.check` |
| 30 | `alibaba.baichuan.taopassword.config` |

</details>

### 百川推送

| # | API名称 |
|---|--------|
| 1 | `taobao.cloudpush.message.ios` |
| 2 | `taobao.cloudpush.message.android` |
| 3 | `taobao.cloudpush.notice.android` |
| 4 | `taobao.cloudpush.push` |
| 5 | `taobao.cloudpush.notice.ios` |

### 国际站商品API (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.category.attrvalue.get` |
| 2 | `alibaba.icbu.photobank.list` |
| 3 | `alibaba.icbu.photobank.upload` |
| 4 | `alibaba.icbu.product.group.get` |
| 5 | `alibaba.icbu.product.group.add` |
| 6 | `alibaba.icbu.product.add` |
| 7 | `alibaba.icbu.category.attribute.get` |
| 8 | `alibaba.icbu.category.get` |
| 9 | `alibaba.icbu.product.update` |
| 10 | `alibaba.wholesale.shippingline.template.list` |
| 11 | `alibaba.icbu.product.list` |
| 12 | `alibaba.icbu.product.get` |
| 13 | `alibaba.icbu.product.id.decrypt` |
| 14 | `alibaba.icbu.product.update.field` |
| 15 | `alibaba.icbu.photobank.group.list` |
| 16 | `alibaba.icbu.photobank.group.operate` |
| 17 | `alibaba.icbu.product.batch.update.display` |
| 18 | `alibaba.icbu.product.add.draft` |
| 19 | `alibaba.icbu.product.score.get` |
| 20 | `alibaba.icbu.category.level.attr.get` |
| 21 | `alibaba.icbu.product.schema.get` |
| 22 | `alibaba.icbu.category.get.new` |
| 23 | `alibaba.icbu.product.schema.render` |
| 24 | `alibaba.icbu.product.schema.update` |
| 25 | `alibaba.icbu.product.schema.render.draft` |
| 26 | `alibaba.icbu.category.schema.level.get` |
| 27 | `alibaba.icbu.category.id.mapping` |

</details>

### 淘宝游戏API

| # | API名称 |
|---|--------|
| 1 | `taobao.game.charge.zc.audit` |
| 2 | `taobao.game.charge.zc.updatesupplierorder` |
| 3 | `taobao.apple.olduser.charge.notify` |
| 4 | `taobao.apple.newuser.sign.notify` |
| 5 | `taobao.apple.newuser.activate.notify` |
| 6 | `taobao.apple.newuser.sign.notify.newversion` |
| 7 | `taobao.apple.card.active.apply.notify` |

### 聚安全API (42 APIs)

<details>
<summary>展开查看全部 42 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.security.jaq.spamregisterprevention.result.fetch` |
| 2 | `alibaba.security.jaq.spamregisterprevention.feedback` |
| 3 | `alibaba.security.jaq.app.risk.scan` |
| 4 | `alibaba.security.jaq.app.risksummary.get` |
| 5 | `alibaba.security.jaq.app.shield` |
| 6 | `alibaba.security.jaq.app.shieldresult.get` |
| 7 | `alibaba.security.jaq.app.riskdetail.get` |
| 8 | `alibaba.security.jaq.wsgriskdata.report` |
| 9 | `alibaba.security.jaq.app.risk.scanbatch` |
| 10 | `alibaba.security.jaq.app.riskdetailbatch.get` |
| 11 | `alibaba.security.jaq.loginprevention.result.fetch` |
| 12 | `alibaba.security.jaq.campaignprevention.result.fetch` |
| 13 | `alibaba.security.jaq.spamregisterprevention.result.fetch.new` |
| 14 | `alibaba.security.jaq.ocr.image.async.detect.results.fetch` |
| 15 | `alibaba.security.jaq.porn.image.sync.detect` |
| 16 | `alibaba.security.jaq.ocr.image.sync.detect` |
| 17 | `alibaba.security.jaq.resource.fetch` |
| 18 | `alibaba.security.jaq.url.scan` |
| 19 | `alibaba.security.jaq.captcha.send` |
| 20 | `alibaba.security.jaq.captcha.verify` |
| 21 | `alibaba.security.jaq.rp.getverifytoken` |
| 22 | `alibaba.security.jaq.captcha.verify.result.fetch` |
| 23 | `alibaba.security.jaq.rp.fetchmaterial` |
| 24 | `alibaba.security.jaq.rp.upload` |
| 25 | `alibaba.security.jaq.rp.query` |
| 26 | `alibaba.security.jaq.rp.submit` |
| 27 | `alibaba.security.jaq.rp.ocr` |
| 28 | `alibaba.security.jaq.rp.start` |
| 29 | `alibaba.security.jaq.rp.status` |
| 30 | `alibaba.security.jaq.afs.check` |
| 31 | `alibaba.security.jaq.rp.rphit` |
| 32 | `alibaba.security.jaq.app.official.verify` |
| 33 | `alibaba.security.jaq.app.official.apply` |
| 34 | `alibaba.security.jaq.rp.cloud.rphit` |
| 35 | `alibaba.security.jaq.rp.cloud.submit` |
| 36 | `alibaba.security.jaq.rp.cloud.start` |
| 37 | `alibaba.security.jaq.rp.cloud.upload` |
| 38 | `alibaba.security.jaq.rp.cloud.event` |
| 39 | `alibaba.security.jaq.rp.cloud.realname.check` |
| 40 | `alibaba.security.jaq.rp.cloud.ocr.check` |
| 41 | `alibaba.security.jaq.rp.ocr.check` |
| 42 | `alibaba.diafi.token.check` |

</details>

### 喵街API (41 APIs)

<details>
<summary>展开查看全部 41 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.mj.oc.writesaleslip` |
| 2 | `alibaba.mj.oc.getproductbyscancode` |
| 3 | `alibaba.mj.oc.pay` |
| 4 | `alibaba.mj.oc.confpickupgoods` |
| 5 | `alibaba.mj.oc.calldispatcher` |
| 6 | `alibaba.mj.presale.settlement.addlist` |
| 7 | `alibaba.mj.oc.outbound` |
| 8 | `alibaba.mj.presale.settlement.statistics` |
| 9 | `alibaba.mos.pos.alarm` |
| 10 | `alibaba.mos.store.getstorelist` |
| 11 | `alibaba.mos.store.getdefautitems` |
| 12 | `alibaba.mos.store.getcloudshelfversion` |
| 13 | `alibaba.mos.store.recordscreenpointinfo` |
| 14 | `alibaba.mj.mos.fund.createbill` |
| 15 | `alibaba.mj.mos.fund.modifybillbankaccount` |
| 16 | `alibaba.mj.mos.fund.cancelbill` |
| 17 | `alibaba.mos.onsite.trade.query` |
| 18 | `alibaba.mos.onsite.trade.pay` |
| 19 | `alibaba.mos.onsite.trade.isnewpayorder` |
| 20 | `alibaba.mos.onsite.trade.queryrefund` |
| 21 | `alibaba.mos.onsite.trade.refund` |
| 22 | `alibaba.mos.onsite.trade.oldrefund` |
| 23 | `alibaba.mosflow.work.startprocess` |
| 24 | `alibaba.mosflow.work.queryvariables` |
| 25 | `alibaba.mos.oc.trade.syncbanksale` |
| 26 | `alibaba.mj.oc.offline.maxticketno.get` |
| 27 | `alibaba.mj.oc.online.ticketno.get` |
| 28 | `alibaba.mj.oc.bigpos.banksale.adjustment.apply` |
| 29 | `alibaba.mj.oc.bigpos.banksale.query` |
| 30 | `alibaba.mos.finance.bankinfo.querybank` |
| 31 | `alibaba.mos.bunk.bunkinfo.querybunk` |
| 32 | `alibaba.mos.supplier.basis.getsupplierinfo` |
| 33 | `alibaba.mj.moscarnival.receivecoupon` |
| 34 | `alibaba.mj.moscarnival.receiveencrypt` |
| 35 | `alibaba.mj.member.bindmember` |
| 36 | `alibaba.mj.member.hasbind` |
| 37 | `alibaba.mos.tmc.sms.send` |
| 38 | `alibaba.mos.brand.coproduct.group.user.query` |
| 39 | `alibaba.mos.brand.coproduct.group.user.count` |
| 40 | `alibaba.mos.hr.background.report.notify` |
| 41 | `alibaba.mos.common.auth.operator.info` |

</details>

### 菜鸟仓配API (18 APIs)

<details>
<summary>展开查看全部 18 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.wlb.wms.stock.in.order.notify` |
| 2 | `taobao.wlb.wms.stock.out.order.notify` |
| 3 | `taobao.wlb.wms.order.cancel.notify` |
| 4 | `taobao.wlb.wms.sku.create` |
| 5 | `taobao.wlb.wms.sku.update` |
| 6 | `taobao.wlb.wms.sku.get` |
| 7 | `taobao.wlb.wms.return.order.notify` |
| 8 | `taobao.wlb.wms.cainiao.bill.query` |
| 9 | `taobao.wlb.wms.return.bill.get` |
| 10 | `taobao.wlb.wms.stock.in.bill.get` |
| 11 | `taobao.wlb.wms.stock.out.bill.get` |
| 12 | `taobao.wlb.wms.consign.bill.get` |
| 13 | `taobao.wlb.wms.inventory.profitloss.get` |
| 14 | `taobao.wlb.wms.inventory.query` |
| 15 | `cainiao.bim.tradeorder.consign` |
| 16 | `taobao.wlb.wms.sn.info.query` |
| 17 | `taobao.wlb.wms.item.combination.get` |
| 18 | `cainiao.crm.oms.rule.sync` |

</details>

### 网上法庭对外API

| # | API名称 |
|---|--------|
| 1 | `alibaba.infodept.lassen.casestatistics.get` |
| 2 | `alibaba.nazca.token.filesecret.get` |
| 3 | `alibaba.nazca.token.issuecertapply.get` |
| 4 | `alibaba.nazca.auth.issueauthapply.callback` |
| 5 | `alibaba.nazca.auth.changeauthapply.callback` |
| 6 | `alibaba.nazca.auth.authapply.callback` |
| 7 | `alibaba.nazca.token.changeauthapply.get` |
| 8 | `alibaba.nazca.token.authapply.get` |

### 五道口API (305 APIs)

<details>
<summary>展开查看全部 305 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.wdk.item.storesku.update` |
| 2 | `alibaba.wdk.merchant.item.query` |
| 3 | `alibaba.wdk.merchant.storeitem.query` |
| 4 | `alibaba.wdk.merchant.brand.query` |
| 5 | `alibaba.wdk.merchant.category.query` |
| 6 | `taobao.wdk.equipment.conveyor.info.upload` |
| 7 | `alibaba.wdk.stock.real.query` |
| 8 | `alibaba.wdk.order.list` |
| 9 | `taobao.wdk.equipment.conveyor.systemevent.get` |
| 10 | `taobao.wdk.equipment.conveyor.containerinfo.get` |
| 11 | `taobao.wdk.equipment.conveyor.hardwarestatuslog.get` |
| 12 | `taobao.wdk.equipment.conveyor.exceptionslidewaylog.get` |
| 13 | `taobao.wdk.equipment.conveyor.conveyorinfo.get` |
| 14 | `alibaba.wdk.ums.outbound.process.get` |
| 15 | `alibaba.wdk.ums.inbound` |
| 16 | `alibaba.wdk.ums.returnitems.get` |
| 17 | `alibaba.wdk.ums.outbound` |
| 18 | `alibaba.wdk.ums.inventory.adjust.get` |
| 19 | `alibaba.wdk.ums.inventory.check.get` |
| 20 | `alibaba.wdk.ums.order.get` |
| 21 | `alibaba.wdk.ums.handling.get` |
| 22 | `alibaba.wdk.order.get` |
| 23 | `alibaba.wdk.order.refund.get` |
| 24 | `alibaba.wdk.order.refund.list` |
| 25 | `taobao.wdk.equipment.conveyor.statusconfirm` |
| 26 | `taobao.wdk.equipment.conveyor.wcsbtoc.containerassignedtoconveyor` |
| 27 | `taobao.wdk.equipment.conveyor.wcsbtoc.containerscannedbyconveyor` |
| 28 | `alibaba.wdk.ums.retrieve.batch.confirm` |
| 29 | `alibaba.wdk.ums.shift.get` |
| 30 | `taobao.wdk.equipment.wcs.wcsinfo.upload` |
| 31 | `alibaba.wdk.marketing.itemdiscount.createactivity` |
| 32 | `alibaba.wdk.marketing.itemdiscount.deleteactivity` |
| 33 | `alibaba.wdk.marketing.itemdiscount.queryitems` |
| 34 | `taobao.wdk.equipment.conveyor.batchconfirm` |
| 35 | `alibaba.wdk.marketing.itemdiscount.removeitem` |
| 36 | `alibaba.wdk.marketing.itemdiscount.additem` |
| 37 | `alibaba.wdk.marketing.itempool.queryitems` |
| 38 | `alibaba.wdk.marketing.itembuygift.createactivity` |
| 39 | `alibaba.wdk.marketing.itembuygift.queryactivity` |
| 40 | `alibaba.wdk.marketing.itembuygift.deleteactivity` |
| 41 | `alibaba.wdk.marketing.itemdiscount.queryactivity` |
| 42 | `alibaba.wdk.marketing.itempool.removeitem` |
| 43 | `alibaba.wdk.marketing.itempool.additem` |
| 44 | `alibaba.wdk.marketing.itempool.deleteactivity` |
| 45 | `alibaba.wdk.marketing.itempool.queryactivity` |
| 46 | `alibaba.wdk.marketing.itempool.createactivity` |
| 47 | `alibaba.wdk.marketing.itembuygift.queryitems` |
| 48 | `alibaba.wdk.marketing.itembuygift.removeitem` |
| 49 | `alibaba.wdk.marketing.itembuygift.additem` |
| 50 | `alibaba.wdk.trace.url.get` |
| 51 | `alibaba.wdk.marketing.price` |
| 52 | `alibaba.wdk.item.category.update` |
| 53 | `alibaba.wdk.item.trace.url.get` |
| 54 | `alibaba.wdk.stock.publish` |
| 55 | `alibaba.wdk.marketing.itempool.stair.removeitem` |
| 56 | `alibaba.wdk.marketing.itempool.stair.additem` |
| 57 | `alibaba.wdk.marketing.itempool.stair.queryitem` |
| 58 | `taobao.wdk.iot.deviceadmin.mqtt.token.get` |
| 59 | `taobao.wdk.iot.deviceadmin.mqtt.device.getwithtoken` |
| 60 | `alibaba.wdk.fulfill.batch.on.task.status.changed` |
| 61 | `alibaba.wdk.fulfill.batch.query.by.batchids` |
| 62 | `alibaba.wdk.item.serviceitem.query` |
| 63 | `alibaba.wdk.marketing.coupon.queryitems` |
| 64 | `alibaba.wdk.marketing.coupon.additem` |
| 65 | `alibaba.wdk.marketing.coupon.endactivity` |
| 66 | `alibaba.wdk.marketing.coupon.queryactivity` |
| 67 | `alibaba.wdk.time.get` |
| 68 | `alibaba.wdk.marketing.coupon.createactivity` |
| 69 | `alibaba.wdk.trade.order.balance.bill.query` |
| 70 | `alibaba.wdk.wholesale.inboundorder.commit` |
| 71 | `alibaba.wdk.wholesale.outboundorder.commit` |
| 72 | `alibaba.wdk.wholesale.order.commit` |
| 73 | `alibaba.price.promotion.activity.delete` |
| 74 | `alibaba.price.promotion.item.delete` |
| 75 | `alibaba.price.promotion.item.add` |
| 76 | `alibaba.price.promotion.create` |
| 77 | `alibaba.price.promotion.activity.query` |
| 78 | `alibaba.wdk.sku.query` |
| 79 | `alibaba.wdk.sku.update` |
| 80 | `alibaba.wdk.sku.channelsku.update` |
| 81 | `alibaba.wdk.sku.channelsku.add` |
| 82 | `alibaba.wdk.sku.add` |
| 83 | `alibaba.wdk.sku.channelsku.query` |
| 84 | `wdk.meal.pos.getfetchmealcode` |
| 85 | `alibaba.wdk.order.aggregate` |
| 86 | `alibaba.wdk.marketing.version.generate` |
| 87 | `alibaba.wdk.marketing.itempool.activity.create` |
| 88 | `alibaba.wdk.marketing.itempool.item.add.async` |
| 89 | `alibaba.wdk.marketing.itempool.item.remove.async` |
| 90 | `alibaba.wdk.marketing.discount.item.add.async` |
| 91 | `alibaba.wdk.marketing.discount.item.remove.async` |
| 92 | `alibaba.wdk.marketing.buygift.item.add.async` |
| 93 | `alibaba.wdk.marketing.buygift.item.remove.async` |
| 94 | `alibaba.wdk.refund.aggregate` |
| 95 | `alibaba.wdk.member.qrcode.identify` |
| 96 | `alibaba.wdk.order.sync` |
| 97 | `alibaba.wdk.shop.query` |
| 98 | `alibaba.wdk.sku.category.delete` |
| 99 | `alibaba.wdk.sku.category.update` |
| 100 | `alibaba.wdk.sku.category.add` |
| 101 | `alibaba.wdk.supplier.refund.list` |
| 102 | `alibaba.wdk.supplier.order.list` |
| 103 | `alibaba.wdk.marketing.fullrange.removeitem` |
| 104 | `alibaba.wdk.marketing.fullrange.queryitem` |
| 105 | `alibaba.wdk.marketing.fullrange.queryactivity` |
| 106 | `alibaba.wdk.marketing.fullrange.deleteactivity` |
| 107 | `alibaba.wdk.marketing.fullrange.createactivity` |
| 108 | `alibaba.wdk.marketing.fullrange.addexchangeitem` |
| 109 | `alibaba.wdk.supplier.refund.get` |
| 110 | `alibaba.wdk.supplier.order.get` |
| 111 | `taobao.wdk.equipment.deviceadmin.deviceinfo.get` |
| 112 | `alibaba.wdk.marketing.expire.promotion.delete` |
| 113 | `alibaba.wdk.marketing.expire.promotion.create` |
| 114 | `alibaba.wdk.marketing.expire.promotion.query` |
| 115 | `alibaba.wdk.sku.category.query` |
| 116 | `alibaba.wdk.oldpos.refund.create` |
| 117 | `alibaba.wdk.oldpos.order.create` |
| 118 | `alibaba.wdk.sku.combinesku.query` |
| 119 | `alibaba.wdk.sku.combinesku.update` |
| 120 | `alibaba.wdk.sku.combinesku.add` |
| 121 | `taobao.wdk.iot.conveyor.conveyorconfig.get` |
| 122 | `alibaba.wdk.member.card.get` |
| 123 | `alibaba.wdk.marketing.version.commit` |
| 124 | `alibaba.wdk.fulfill.config.read.limit.order` |
| 125 | `alibaba.wdk.ums.inventory.publish` |
| 126 | `alibaba.wdk.sku.warehousesku.query` |
| 127 | `alibaba.wdk.sku.warehousesku.scroll.query` |
| 128 | `alibaba.wdk.reverse.refund` |
| 129 | `alibaba.wdk.marketing.itempool.addcategory` |
| 130 | `alibaba.wdk.marketing.itempool.excludeskucode` |
| 131 | `alibaba.wdk.finance.order.backflow` |
| 132 | `alibaba.wdk.marketing.open.data.relation.query` |
| 133 | `alibaba.wdk.marketing.open.version.count` |
| 134 | `alibaba.wdk.marketing.open.version.apply` |
| 135 | `alibaba.wdk.marketing.open.darunfa.activity.sku.sync` |
| 136 | `alibaba.wdk.marketing.open.darunfa.activity.sync` |
| 137 | `alibaba.wdk.order.finance.bill.query` |
| 138 | `alibaba.wdk.item.merchant.category.query` |
| 139 | `alibaba.wdk.merchant.routing.register` |
| 140 | `wdk.wms.pick.medicine.query` |
| 141 | `wdk.wms.pick.medicine.checksell` |
| 142 | `alibaba.wdk.marketing.open.heartbeat` |
| 143 | `alibaba.wdk.sku.merchantsku.scroll.query` |
| 144 | `alibaba.wdk.sku.storesku.scroll.query` |
| 145 | `alibaba.wdk.channel.order.create` |
| 146 | `alibaba.wdk.channel.user.sync` |
| 147 | `alibaba.wdk.channel.order.refund.confirm` |
| 148 | `alibaba.wdk.channel.comment.create` |
| 149 | `alibaba.wdk.purchase.price` |
| 150 | `alibaba.wdk.eleme.bill.detail.get` |
| 151 | `alibaba.wdk.eleme.bill.get` |
| 152 | `alibaba.wdk.sku.barcode.query` |
| 153 | `alibaba.wdk.series.sku.add` |
| 154 | `alibaba.wdk.series.sku.remove` |
| 155 | `alibaba.wdk.series.create` |
| 156 | `alibaba.wdk.series.defaultsku.reset` |
| 157 | `alibaba.wdk.sopo.push.trigger` |
| 158 | `alibaba.wdk.syncedorder.query` |
| 159 | `alibaba.wdk.fulfill.box.post.back.box` |
| 160 | `alibaba.wdk.hrworkbench.moka.entry.receipt.write` |
| 161 | `alibaba.wdk.series.sort` |
| 162 | `alibaba.wdk.fulfill.warehouse.work.order.callback` |
| 163 | `alibaba.wdk.sku.scroll.query` |
| 164 | `alibaba.wdk.merchantproduct.edit` |
| 165 | `alibaba.wdk.fulfill.dms.ebeecake.work.order.callback` |
| 166 | `alibaba.wdk.fulfill.missfresh.warehouse.work.order.callback` |
| 167 | `alibaba.wdk.fulfill.rt.btoc.warehouse.work.order.callback` |
| 168 | `alibaba.wdk.sku.feature` |
| 169 | `alibaba.wdkorder.sharestock.fulfill.get` |
| 170 | `alibaba.wdkorder.sharestock.order.get` |
| 171 | `alibaba.wdkopen.order.get` |
| 172 | `alibaba.wdkopen.cateorder.pull` |
| 173 | `alibaba.pos.fund.cashier.shift.summary` |
| 174 | `alibaba.wdkorder.sharestock.insurance.getorder` |
| 175 | `alibaba.wdkorder.sharestock.insurance.callback` |
| 176 | `alibaba.wdkorder.sharestock.insurance.refundget` |
| 177 | `alibaba.newretail.purchase.price.save` |
| 178 | `alibaba.wdk.fulfill.sf.btoc.fms.wms.work.order.callback` |
| 179 | `alibaba.newretail.purchase.price.delete` |
| 180 | `alibaba.wdk.coupon.contract.create` |
| 181 | `alibaba.ifp.fulfill.warehouse.token.query` |
| 182 | `tmall.cityretail.fulfill.abnormal.center.abnormal.status.change` |
| 183 | `alibaba.wdk.coupon.template.queryumpactid` |
| 184 | `alibaba.wdk.reverse.reversedetail` |
| 185 | `alibaba.wdk.reverse.creatrefund` |
| 186 | `alibaba.wdk.reverse.applyrefund` |
| 187 | `alibaba.tcls.aelophy.refund.disagree` |
| 188 | `alibaba.tcls.aelophy.refund.agree` |
| 189 | `alibaba.tcls.aelophy.refund.fetchgoods` |
| 190 | `alibaba.wdk.fulfill.warehouse.work.order.sealbox` |
| 191 | `alibaba.tcls.aelophy.refund.csapply` |
| 192 | `alibaba.wdk.reverse.createfeatch` |
| 193 | `alibaba.wdk.reverse.timeslice` |
| 194 | `alibaba.wdk.fulfill.dms.delivery.work.order.callback` |
| 195 | `alibaba.wdk.bill.list` |
| 196 | `alibaba.tcls.aelophy.merchant.user.upload` |
| 197 | `alibaba.tcls.aelophy.merchant.order.upload` |
| 198 | `alibaba.tcls.aelophy.bill.verificate.callback` |
| 199 | `alibaba.wdk.reverse.load.featchorder` |
| 200 | `alibaba.tcls.aelophy.merchant.id.mix` |
| 201 | `alibaba.tcls.aelophy.merchant.order.batch.upload` |
| 202 | `tmall.cityretail.txd.fulfill.order.virtualnumber` |
| 203 | `tmall.cityretail.txd.fulfill.order.unbindnum` |
| 204 | `alibaba.ax.channel.sku.status.update` |
| 205 | `alibaba.retail.marketing.itemdiscount.sku.query` |
| 206 | `alibaba.retail.marketing.itempool.sku.query` |
| 207 | `alibaba.retail.marketing.buygift.sku.query` |
| 208 | `alibaba.tcls.aelophy.bill.detail.query` |
| 209 | `wdk.ums.outbound.sorting.cancleararea` |
| 210 | `wdk.ums.outbound.sorting.callbackforpulltask` |
| 211 | `alibaba.tcls.aelophy.bill.daily.query` |
| 212 | `wdk.ums.outbound.sorting.callback.taskdetail` |
| 213 | `wdk.ums.sorting.full.container` |
| 214 | `wdk.ums.outbound.sorting.scancontainer` |
| 215 | `alibaba.tcls.aelophy.refund.csapply.new` |
| 216 | `alibaba.wdk.ax.store.update` |
| 217 | `alibaba.wdk.ax.store.create` |
| 218 | `alibaba.wdk.ax.store.query` |
| 219 | `alibaba.wdkorder.sharestock.cpsorder.list` |
| 220 | `wdk.ums.outbound.sorting.userquery` |
| 221 | `alibaba.tcls.aelophy.order.receipt.query` |
| 222 | `alibaba.wdk.trade.order.success.create` |
| 223 | `alibaba.wdk.trade.refund.success.create` |
| 224 | `alibaba.wdk.marketing.open.pos.discount.code.create` |
| 225 | `alibaba.tcls.aelophy.merchant.channel.order.sliceget` |
| 226 | `alibaba.tcls.aelophy.merchant.channel.order.precheck` |
| 227 | `alibaba.ax.warehouse.outbound.callback` |
| 228 | `alibaba.ax.warehouse.inbound.callback` |
| 229 | `alibaba.tc.compass.warehousenetwork.query` |
| 230 | `alibaba.aelophy.order.deliverer.change` |
| 231 | `alibaba.aelophy.order.work.callback` |
| 232 | `alibaba.aelophy.order.get` |
| 233 | `alibaba.aelophy.order.logistics.trace.callback` |
| 234 | `alibaba.aelophy.shop.updatestatus` |
| 235 | `alibaba.aelophy.shop.updaterange` |
| 236 | `alibaba.aelophy.shop.updateinfo` |
| 237 | `alibaba.hm.marketing.itempool.createactivity` |
| 238 | `alibaba.hm.marketing.itempool.activity.create` |
| 239 | `alibaba.hm.marketing.itempool.deleteactivity` |
| 240 | `alibaba.hm.marketing.itempool.queryactivity` |
| 241 | `alibaba.hm.marketing.itempool.additem` |
| 242 | `alibaba.hm.marketing.itempool.queryitems` |
| 243 | `alibaba.hm.marketing.itempool.removeitem` |
| 244 | `alibaba.hm.marketing.itemdiscount.createactivity` |
| 245 | `alibaba.hm.marketing.fullrange.removeitem` |
| 246 | `alibaba.hm.marketing.fullrange.addexchangeitem` |
| 247 | `alibaba.hm.marketing.coupon.queryitems` |
| 248 | `alibaba.hm.marketing.itemdiscount.deleteactivity` |
| 249 | `alibaba.hm.marketing.itemdiscount.removeitem` |
| 250 | `alibaba.hm.marketing.itemdiscount.queryactivity` |
| 251 | `alibaba.hm.marketing.itemdiscount.queryitems` |
| 252 | `alibaba.hm.marketing.itemdiscount.additem` |
| 253 | `alibaba.hm.marketing.buygift.item.add.async` |
| 254 | `alibaba.hm.marketing.buygift.item.remove.async` |
| 255 | `alibaba.hm.marketing.coupon.createactivity` |
| 256 | `alibaba.hm.marketing.coupon.endactivity` |
| 257 | `alibaba.hm.marketing.coupon.sendma` |
| 258 | `alibaba.hm.marketing.discount.item.add.async` |
| 259 | `alibaba.hm.marketing.discount.item.remove.async` |
| 260 | `alibaba.hm.marketing.expire.promotion.query` |
| 261 | `alibaba.hm.marketing.fullrange.createactivity` |
| 262 | `alibaba.hm.marketing.fullrange.deleteactivity` |
| 263 | `alibaba.hm.marketing.fullrange.queryitem` |
| 264 | `alibaba.hm.marketing.itembuygift.deleteactivity` |
| 265 | `alibaba.hm.marketing.itembuygift.queryactivity` |
| 266 | `alibaba.hm.marketing.itembuygift.queryitems` |
| 267 | `alibaba.hm.marketing.itempool.addcategory` |
| 268 | `alibaba.hm.marketing.itempool.excludeskucode` |
| 269 | `alibaba.hm.marketing.itempool.item.add.async` |
| 270 | `alibaba.hm.marketing.itempool.item.remove.async` |
| 271 | `alibaba.hm.marketing.itempool.stair.additem` |
| 272 | `alibaba.hm.marketing.itempool.stair.queryitem` |
| 273 | `alibaba.hm.marketing.itempool.stair.removeitem` |
| 274 | `alibaba.hm.marketing.version.commit` |
| 275 | `alibaba.hm.marketing.version.generate` |
| 276 | `alibaba.hm.marketing.itembuygift.createactivity` |
| 277 | `alibaba.hm.marketing.fullrange.queryactivity` |
| 278 | `alibaba.hm.marketing.expire.promotion.create` |
| 279 | `alibaba.hm.marketing.expire.promotion.delete` |
| 280 | `alibaba.hm.marketing.itembuygift.additem` |
| 281 | `alibaba.hm.marketing.itembuygift.removeitem` |
| 282 | `alibaba.aelophy.order.desensitizephone.get` |
| 283 | `alibaba.tcls.aelophy.warehouse.order.get` |
| 284 | `alibaba.hema.maintenance.external.order.push` |
| 285 | `alibaba.txd.voucher.verification.cancel` |
| 286 | `alibaba.txd.voucher.get` |
| 287 | `alibaba.txd.voucher.verificate` |
| 288 | `alibaba.txd.voucher.list` |
| 289 | `wdk.wes.device.collect.photoelectric.report` |
| 290 | `wdk.wes.device.collect.bcr.report` |
| 291 | `alibaba.hema.maintenance.external.order.close` |
| 292 | `wdk.wes.device.event.report` |
| 293 | `wdk.wes.device.task.ack.response` |
| 294 | `wdk.wes.device.task.query` |
| 295 | `alibaba.hema.maintenance.external.order.quotation` |
| 296 | `alibaba.hema.maintenance.external.order.settlement` |
| 297 | `wdk.mall.laundryorder.query` |
| 298 | `wdk.ums.mes.flow.callback` |
| 299 | `wdk.ums.mes.purchase.query` |
| 300 | `wdk.ums.mes.flow.repackage` |
| 301 | `wdk.ums.mes.flow.confirmpull` |
| 302 | `alibaba.aelophy.order.delivery.query` |
| 303 | `alibaba.aelophy.order.delivery.refund.query` |
| 304 | `alibaba.aelophy.order.delivery.recall` |
| 305 | `alibaba.hema.maintenance.external.order.giveup` |

</details>

### 阿里大于API (20 APIs)

<details>
<summary>展开查看全部 20 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.aliqin.fc.voice.num.doublecall` |
| 2 | `alibaba.aliqin.fc.tts.num.singlecall` |
| 3 | `alibaba.aliqin.fc.voice.num.singlecall` |
| 4 | `alibaba.aliqin.fc.sms.num.send` |
| 5 | `alibaba.aliqin.fc.sms.num.query` |
| 6 | `alibaba.aliqin.fc.ivr.num.call` |
| 7 | `alibaba.aliqin.fc.iot.qrycard` |
| 8 | `alibaba.aliqin.fc.iot.rechargeCard` |
| 9 | `alibaba.aliqin.fc.iot.modbind` |
| 10 | `alibaba.aliqin.fc.iot.qry.personinfo` |
| 11 | `alibaba.aliqin.fc.iot.cardStatus` |
| 12 | `alibaba.aliqin.fc.iot.cardInfo` |
| 13 | `alibaba.aliqin.fc.iot.device.post` |
| 14 | `alibaba.aliqin.fc.iot.device.isexist` |
| 15 | `alibaba.aliqin.fc.iot.sms.send` |
| 16 | `alibaba.aliqin.fc.iot.cardoffer` |
| 17 | `alibaba.aliqin.fc.iot.useroscontrol` |
| 18 | `alibaba.aliqin.fc.digitalsms.createtemplate` |
| 19 | `alibaba.isv.digitalsms.createtemplate` |
| 20 | `alibaba.aliyunindep.digitalsms.createtemplate` |

</details>

### 淘宝内容API

| # | API名称 |
|---|--------|
| 1 | `taobao.beehive.item.cps.url` |

### 旅行用车API

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.car.order.confirm` |
| 2 | `taobao.alitrip.car.order.complete` |
| 3 | `taobao.alitrip.car.order.accept` |
| 4 | `taobao.alitrip.car.rent.order.cancel` |
| 5 | `taobao.alitrip.car.order.status` |
| 6 | `taobao.alitrip.car.driver.status.update` |
| 7 | `taobao.alitrip.car.order.query` |
| 8 | `taobao.alitrip.domestic.rent.car.status.update` |
| 9 | `alitrip.travel.crsdriver.arrange` |
| 10 | `alitrip.travel.crsorder.complete` |
| 11 | `alitrip.travel.crsorder.search` |
| 12 | `alitrip.rentcar.order.detail.query` |
| 13 | `alitrip.transfer.order.detail` |
| 14 | `alitrip.transfer.realname.auth` |
| 15 | `alitrip.rentcar.seller.refund.submit` |

### 门票-商品管理API

| # | API名称 |
|---|--------|
| 1 | `alitrip.ticket.scenic.query` |
| 2 | `alitrip.ticket.rule.query` |
| 3 | `alitrip.ticket.product.query` |
| 4 | `alitrip.ticket.scenic.bind` |
| 5 | `alitrip.ticket.skus.upload` |
| 6 | `alitrip.ticket.rule.upload` |
| 7 | `alitrip.ticket.product.upload` |
| 8 | `alitrip.ticket.skus.batch.upload` |

### 菜鸟无线API

| # | API名称 |
|---|--------|
| 1 | `cainiao.guoguo.backup.graborder.submitmailno` |
| 2 | `cainiao.guoguo.backup.graborder.takepackage` |
| 3 | `cainiao.guoguo.cp.backup.assigncourierbyid` |

### 奇门仓储API (63 APIs)

<details>
<summary>展开查看全部 63 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.qimen.deliveryorder.query` |
| 2 | `taobao.qimen.entryorder.query` |
| 3 | `taobao.qimen.returnorder.create` |
| 4 | `taobao.qimen.entryorder.create` |
| 5 | `taobao.qimen.stockout.create` |
| 6 | `taobao.qimen.deliveryorder.batchconfirm` |
| 7 | `taobao.qimen.deliveryorder.batchcreate` |
| 8 | `taobao.qimen.entryorder.confirm` |
| 9 | `taobao.qimen.stockchange.report` |
| 10 | `taobao.qimen.returnorder.confirm` |
| 11 | `taobao.qimen.singleitem.synchronize` |
| 12 | `taobao.qimen.inventory.query` |
| 13 | `taobao.qimen.order.cancel` |
| 14 | `taobao.qimen.deliveryorder.confirm` |
| 15 | `taobao.qimen.deliveryorder.create` |
| 16 | `taobao.qimen.orderprocess.report` |
| 17 | `taobao.qimen.store.update` |
| 18 | `taobao.qimen.store.create` |
| 19 | `taobao.qimen.store.delete` |
| 20 | `taobao.qimen.store.query` |
| 21 | `taobao.qimen.storecategory.get` |
| 22 | `taobao.qimen.itemstore.banding` |
| 23 | `taobao.qimen.itemstore.query` |
| 24 | `taobao.qimen.storeitem.query` |
| 25 | `taobao.qimen.sn.report` |
| 26 | `taobao.qimen.stockout.confirm` |
| 27 | `taobao.qimen.wavenum.report` |
| 28 | `taobao.qimen.inventory.report` |
| 29 | `taobao.qimen.items.synchronize` |
| 30 | `taobao.qimen.combineitem.synchronize` |
| 31 | `taobao.qimen.deliveryorder.batchcreate.answer` |
| 32 | `taobao.qimen.storeprocess.create` |
| 33 | `taobao.qimen.storeprocess.confirm` |
| 34 | `taobao.qimen.stock.query` |
| 35 | `taobao.qimen.orderprocess.query` |
| 36 | `taobao.qimen.itemlack.report` |
| 37 | `taobao.qimen.order.pending` |
| 38 | `taobao.qimen.orderexception.report` |
| 39 | `taobao.qimen.inventoryreserve.cancel` |
| 40 | `taobao.qimen.expressinfo.query` |
| 41 | `taobao.qimen.warehouseinfo.query` |
| 42 | `taobao.qimen.combineitem.query` |
| 43 | `taobao.qimen.order.sn.report` |
| 44 | `taobao.qimen.order.callback` |
| 45 | `taobao.qimen.transferorder.query` |
| 46 | `taobao.qimen.transferorder.create` |
| 47 | `taobao.qimen.transferorder.report` |
| 48 | `taobao.qimen.itemmapping.create` |
| 49 | `taobao.qimen.singleitem.query` |
| 50 | `taobao.qimen.combineitem.delete` |
| 51 | `taobao.qimen.inventoryrule.create` |
| 52 | `taobao.qimen.channelinventory.query` |
| 53 | `taobao.qimen.shop.synchronize` |
| 54 | `taobao.qimen.returnpackage.report` |
| 55 | `taobao.qimen.warehouseinfo.synchronize` |
| 56 | `taobao.qimen.itemmapping.query` |
| 57 | `taobao.qimen.supplier.synchronize` |
| 58 | `taobao.qimen.receiverinfo.query` |
| 59 | `taobao.qimen.order.query` |
| 60 | `taobao.qimen.inventorybatch.query` |
| 61 | `taobao.qimen.inventory.synchronize.report` |
| 62 | `taobao.qimen.inventory.synchronize` |
| 63 | `taobao.qimen.presalespackage.consign` |

</details>

### yunos推送服务api

| # | API名称 |
|---|--------|
| 1 | `yunos.service.cmns.coa.push` |
| 2 | `yunos.service.cmns.coa.messageresult.get` |
| 3 | `yunos.service.cmns.coa.message.ack` |
| 4 | `yunos.service.cmns.coa.message.cancel` |
| 5 | `yunos.service.cmns.coa.message.push` |
| 6 | `yunos.service.cmns.coa.device.isonline` |
| 7 | `yunos.service.cmns.coa.message.get` |
| 8 | `yunos.service.cmns.coa.device.get` |
| 9 | `yunos.service.cmns.coa.message.acks.list` |

### 生活汇API

| # | API名称 |
|---|--------|
| 1 | `taobao.elife.lifecard.consume` |
| 2 | `taobao.elife.lifecard.query` |
| 3 | `taobao.elife.lifecard.recon` |

### tv支付

| # | API名称 |
|---|--------|
| 1 | `taobao.tvpay.access.data.get` |
| 2 | `taobao.tvpay.appinfo.get` |
| 3 | `taobao.tvpay.order.query` |
| 4 | `taobao.tvpay.auth.apply` |
| 5 | `taobao.tvpay.promotion.info.get` |
| 6 | `taobao.tvpay.order.precreate` |
| 7 | `taobao.tvpay.order.partnerpay` |
| 8 | `taobao.tvpay.partner.order.query` |

### 菜鸟集货API (19 APIs)

<details>
<summary>展开查看全部 19 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.wlb.imports.resource.get` |
| 2 | `taobao.wlb.imports.resource.transferstore.get` |
| 3 | `taobao.wlb.imports.waybill.get` |
| 4 | `taobao.wlb.imports.order.get` |
| 5 | `taobao.wlb.imports.general.consign` |
| 6 | `taobao.wlb.imports.order.cancel` |
| 7 | `taobao.wlb.crossborder.waybill.get` |
| 8 | `taobao.wlb.imports.vas.identity.result` |
| 9 | `cainiao.global.im.pickup.bigbag.info` |
| 10 | `cainiao.global.im.pickup.stores.get` |
| 11 | `cainiao.global.im.pickup.bigbag.content.create` |
| 12 | `cainiao.global.im.pickup.bigbag.content.cancel` |
| 13 | `cainiao.global.im.pickup.bigbag.logistics.trajectory` |
| 14 | `cainiao.global.im.pickup.bigbag.express.prequery` |
| 15 | `cainiao.global.im.pickup.appointment.order.cancel` |
| 16 | `cainiao.global.im.pickup.appointment.order.info.create` |
| 17 | `cainiao.global.im.pickup.appointment.order.status` |
| 18 | `cainiao.global.im.pickup.bigbag.waybill.info` |
| 19 | `cainiao.global.im.pickup.appointment.order.difference.detail` |

</details>

### 地动仪

| # | API名称 |
|---|--------|
| 1 | `taobao.lbs.message.upload` |

### 阿里健康药API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.nr.trade.order.get` |
| 2 | `alibaba.alihealth.nr.trade.medical.insurance.get` |
| 3 | `alibaba.health.nr.logistics.deliveryno.update` |
| 4 | `alibaba.alihealth.nr.spu.query` |
| 5 | `alibaba.alihealth.nr.rx.queryimage` |
| 6 | `alibaba.alihealth.nr.trade.order.getorderdetail` |

### 法务诉讼对外API (16 APIs)

<details>
<summary>展开查看全部 16 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.legal.suit.file.upload` |
| 2 | `alibaba.legal.case.entrust.get` |
| 3 | `alibaba.legal.case.common.notice` |
| 4 | `alibaba.legal.case.entrust.callback` |
| 5 | `alibaba.legal.case.court.time.update` |
| 6 | `alibaba.legal.case.mediate.record.save` |
| 7 | `alibaba.legal.case.common.enumdata` |
| 8 | `alibaba.legal.case.standpoint.feedback` |
| 9 | `alibaba.legal.case.standpoint.savestandpoint` |
| 10 | `alibaba.legal.case.standpoint.queryref` |
| 11 | `alibaba.legal.case.standpoint.querystandpoint` |
| 12 | `alibaba.legal.case.querystandpoint.save` |
| 13 | `alibaba.suit.case.prelitigationmediation` |
| 14 | `alibaba.suit.case.receivepolicyinformation` |
| 15 | `alibaba.suit.case.filegetsts` |
| 16 | `alibaba.suit.idp.get` |

</details>

### 度假-商品管理API (28 APIs)

<details>
<summary>展开查看全部 28 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.travel.item.sku.override` |
| 2 | `taobao.alitrip.travel.baseinfo.cities.get` |
| 3 | `taobao.alitrip.travel.item.shelve` |
| 4 | `taobao.alitrip.travel.item.single.query` |
| 5 | `taobao.alitrip.travel.baseinfo.scenics.get` |
| 6 | `taobao.alitrip.travel.item.sku.price.modify` |
| 7 | `taobao.alitrip.travel.item.sku.package.modify` |
| 8 | `taobao.alitrip.travel.baseinfo.cruise.get` |
| 9 | `taobao.alitrip.travel.item.element.manage` |
| 10 | `taobao.alitrip.travel.item.element.query` |
| 11 | `alitrip.daytours.product.upload` |
| 12 | `alitrip.grouptours.product.upload` |
| 13 | `alitrip.travel.gereralsku.update` |
| 14 | `alitrip.travel.poi.search` |
| 15 | `alitrip.travel.gereralitem.update` |
| 16 | `alitrip.localplay.product.upload` |
| 17 | `alitrip.freetour.product.upload` |
| 18 | `alitrip.grouptour.product.upload` |
| 19 | `taobao.alitrip.travel.product.base.add` |
| 20 | `taobao.alitrip.travel.product.base.modify` |
| 21 | `taobao.alitrip.travel.product.sku.override` |
| 22 | `alitrip.travel.gereralproduct.update` |
| 23 | `alitrip.travel.product.gereralsku.update` |
| 24 | `taobao.alitrip.travel.item.new.query` |
| 25 | `alitrip.item.schema.add` |
| 26 | `alitrip.item.update.schema.get` |
| 27 | `alitrip.item.schema.update` |
| 28 | `alitrip.item.add.schema.get` |

</details>

### 酒店商品API (83 APIs)

<details>
<summary>展开查看全部 83 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.roomtype.get` |
| 2 | `taobao.xhotel.roomtype.update` |
| 3 | `taobao.xhotel.roomtype.add` |
| 4 | `taobao.xhotel.get` |
| 5 | `taobao.xhotel.update` |
| 6 | `taobao.xhotel.add` |
| 7 | `taobao.xhotel.room.get` |
| 8 | `taobao.xhotel.rateplan.get` |
| 9 | `taobao.xhotel.rooms.update` |
| 10 | `taobao.xhotel.room.update` |
| 11 | `taobao.xhotel.rates.update` |
| 12 | `taobao.xhotel.rate.update` |
| 13 | `taobao.xhotel.rate.get` |
| 14 | `taobao.xhotel.rate.add` |
| 15 | `taobao.xhotel.rateplan.update` |
| 16 | `taobao.xhotel.rateplan.add` |
| 17 | `taobao.xhotel.rates.increment` |
| 18 | `taobao.xhotel.rooms.increment` |
| 19 | `taobao.xhotel.rate.relationshipwithrp.get` |
| 20 | `taobao.xhotel.rate.relationshipwithroom.get` |
| 21 | `taobao.xhotel.increment.info.get` |
| 22 | `taobao.xhotel.multiplerate.get` |
| 23 | `taobao.xhotel.multiplerates.update` |
| 24 | `taobao.xhotel.multiplerate.update` |
| 25 | `taobao.xhotel.multiplerates.increment` |
| 26 | `taobao.xhotel.baseinfo.get` |
| 27 | `taobao.xhotel.rateplan.delete` |
| 28 | `taobao.xhotel.rate.delete` |
| 29 | `taobao.xhotel.multiplerate.delete` |
| 30 | `taobao.xhotel.baseinfo.room.get` |
| 31 | `taobao.xhotel.city.coordinates.batch.upload` |
| 32 | `taobao.xhotel.city.coordinates.batch.download` |
| 33 | `taobao.xhotel.entity.config` |
| 34 | `taobao.xhotel.house.add` |
| 35 | `taobao.xhotel.house.roomtype.add` |
| 36 | `taobao.xhotel.servicetime.update` |
| 37 | `taobao.xhotel.servicetime.get` |
| 38 | `taobao.xhotel.delete` |
| 39 | `taobao.xhotel.roomtype.delete.public` |
| 40 | `taobao.xhotel.quota.update` |
| 41 | `taobao.xhotel.rates.lite.incr.update` |
| 42 | `taobao.xhotel.item.selection.seller.stat.summary` |
| 43 | `taobao.xhotel.item.selection.seller.stat.exposure` |
| 44 | `taobao.xhotel.item.selection.seller.stat.hotshid` |
| 45 | `taobao.xhotel.roomtype.conflict.data` |
| 46 | `taobao.xhotel.get.entity.by.tag` |
| 47 | `taobao.xhotel.bnbroomtype.add` |
| 48 | `taobao.xhotel.bnbhouse.add` |
| 49 | `taobao.xhotel.bnbowner.add` |
| 50 | `taobao.xhotel.bnbowner.delete` |
| 51 | `taobao.xhotel.bnbhouse.delete` |
| 52 | `taobao.xhotel.bnbroomtype.delete` |
| 53 | `taobao.xhotel.bnbpromo.delete` |
| 54 | `taobao.xhotel.bnbpromo.get` |
| 55 | `taobao.xhotel.bnbpromo.add` |
| 56 | `taobao.xhotel.bnbpromo.bind` |
| 57 | `taobao.xhotel.bnbpromo.unbind` |
| 58 | `taobao.xhotel.bnbreview.add` |
| 59 | `taobao.xhotel.bnbcommon.add` |
| 60 | `taobao.xhotel.xitem.delete` |
| 61 | `taobao.xhotel.xitem.query` |
| 62 | `taobao.xhotel.status.update` |
| 63 | `taobao.roomtype.status.update` |
| 64 | `taobao.xhotel.distribution.feed.hotel.query` |
| 65 | `taobao.xhotel.distribution.ari.availability` |
| 66 | `taobao.xhotel.bnbreview.reply` |
| 67 | `taobao.xhotel.bnbstatusxbot.send` |
| 68 | `taobao.xhotel.bnbhotel.data.sync` |
| 69 | `taobao.xhotel.bnb.agg.sync` |
| 70 | `taobao.xhotel.agg.increment.rp.sync` |
| 71 | `taobao.xhotel.bnbllm.query` |
| 72 | `taobao.xhotel.bnbllm.poll.query` |
| 73 | `taobao.xhotel.bnbpoi.get` |
| 74 | `taobao.xhotel.bnbxbot.record` |
| 75 | `taobao.xhotel.bnbprice.get` |
| 76 | `taobao.xhotel.bnb.promo.get` |
| 77 | `taobao.xhotel.bnb.ai.customer.message` |
| 78 | `taobao.xhotel.bnbxbot.callback` |
| 79 | `taobao.xhotel.bnbaicheck.notice` |
| 80 | `taobao.xhotel.bnbhotelprice.track` |
| 81 | `taobao.xhotel.bnbhotel.match` |
| 82 | `taobao.xhotel.bnb.combohotel.callback` |
| 83 | `taobao.xhotel.bnb.combohotel` |

</details>

### 酒店在线预订API (22 APIs)

<details>
<summary>展开查看全部 22 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.order.search` |
| 2 | `taobao.xhotel.order.alipayface.cancelsettle` |
| 3 | `taobao.xhotel.order.alipayface.settle` |
| 4 | `taobao.xhotel.order.alipayface.update` |
| 5 | `taobao.xhotel.order.update` |
| 6 | `taobao.xhotel.memberright.update` |
| 7 | `taobao.xhotel.order.statement.get` |
| 8 | `taobao.xhotel.order.future.info.get` |
| 9 | `taobao.xhotel.order.future.facescan.put` |
| 10 | `taobao.xhotel.fastinvoice.request` |
| 11 | `taobao.xhotel.fastinvoice.complete` |
| 12 | `taobao.xhotel.commoninvoice.remove` |
| 13 | `taobao.xhotel.commoninvoice.update` |
| 14 | `taobao.xhotel.order.detail.search` |
| 15 | `taobao.xhotel.future.softmodify` |
| 16 | `taobao.xhotel.order.update.confirmcode` |
| 17 | `taobao.xhotel.pms.guestbill.get.vtwo` |
| 18 | `taobao.xhotel.commoninvoice.list.vtwo` |
| 19 | `alitrip.xhotel.channel.notify` |
| 20 | `alitrip.xhotel.channel.order.create` |
| 21 | `taobao.xhotel.intl.rate.update` |
| 22 | `alitrip.xhotel.channel.order.membertype.sync` |

</details>

### 酒店官网信用住API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.order.official.settle.cancel` |
| 2 | `taobao.xhotel.order.official.settle.put` |
| 3 | `taobao.xhotel.order.official.cancel` |
| 4 | `taobao.xhotel.order.official.precheck` |

### 酒店线下信用住API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.order.alipayface.create` |
| 2 | `taobao.xhotel.order.alipayface.check` |
| 3 | `taobao.xhotel.order.alipayface.extend` |
| 4 | `taobao.xhotel.order.alipayface.cancel` |
| 5 | `taobao.xhotel.order.offline.settle.put` |

### 全渠道API (44 APIs)

<details>
<summary>展开查看全部 44 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.qimen.tag.items.query` |
| 2 | `taobao.qimen.items.marking` |
| 3 | `taobao.qimen.items.tag.query` |
| 4 | `taobao.omniorder.allocatedinfo.sync` |
| 5 | `taobao.omniorder.store.accpeted` |
| 6 | `taobao.omniorder.store.refused` |
| 7 | `taobao.omniorder.store.consigned` |
| 8 | `taobao.omniorder.print.sale.judge` |
| 9 | `taobao.omniorder.store.sdtquerystation` |
| 10 | `taobao.omniorder.storecollect.query` |
| 11 | `taobao.omniorder.storecollect.consume` |
| 12 | `taobao.omniorder.store.reallocate` |
| 13 | `taobao.omniorder.store.switchstatus.update` |
| 14 | `taobao.omniitem.item.publish` |
| 15 | `taobao.omniitem.category.get` |
| 16 | `taobao.omniitem.item.fullupdate` |
| 17 | `taobao.omniitem.item.delete` |
| 18 | `taobao.omniorder.dtd.resend` |
| 19 | `taobao.omniorder.dtd.consign` |
| 20 | `taobao.omniorder.dtd.query` |
| 21 | `taobao.omniitem.item.get` |
| 22 | `taobao.omniitem.sku.get` |
| 23 | `taobao.omniorder.store.deliverconfig.update` |
| 24 | `taobao.omniorder.store.collectconfig.update` |
| 25 | `taobao.omniorder.store.deliverconfig.get` |
| 26 | `taobao.omniorder.item.tag.operate` |
| 27 | `taobao.jst.astrolabe.storeinventory.iteminitial` |
| 28 | `taobao.jst.astrolabe.storeinventory.itemquery` |
| 29 | `taobao.jst.astrolabe.storeinventory.itemupdate` |
| 30 | `taobao.jst.astrolabe.orderstatus.sync` |
| 31 | `taobao.jst.astrolabe.storeinventory.update` |
| 32 | `taobao.omniorder.guide.data.get` |
| 33 | `alibaba.retail.commission.order.sync` |
| 34 | `alibaba.retail.commission.status.change` |
| 35 | `alibaba.retail.commission.order.query` |
| 36 | `alibaba.retail.commission.result.query` |
| 37 | `taobao.omni.dealer.oders.list` |
| 38 | `taobao.omni.dealer.oders.refund.address` |
| 39 | `taobao.omni.order.goods.ready` |
| 40 | `taobao.omni.order.detail` |
| 41 | `tmall.nr.fn.order.cancel` |
| 42 | `taobao.shangou.storecollect.accept` |
| 43 | `taobao.shangou.fulfillinfo.update` |
| 44 | `alibaba.xsd.item.nr.price.query` |

</details>

### 珠宝认证数据导入

| # | API名称 |
|---|--------|
| 1 | `taobao.ricare.jewelry.certificate.callback` |
| 2 | `taobao.ricare.jewelry.certificate.remove` |

### 国际机票政策API

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.it.fare.get` |
| 2 | `taobao.alitrip.it.fare.addow` |
| 3 | `taobao.alitrip.it.fare.querytask` |
| 4 | `taobao.alitrip.it.fare.delete` |
| 5 | `taobao.alitrip.it.fare.addrt` |
| 6 | `taobao.alitrip.it.fare.batchdelete` |
| 7 | `taobao.alitrip.it.fare.batchadd` |
| 8 | `taobao.alitrip.it.fare.update` |
| 9 | `taobao.alitrip.it.policy.delete` |
| 10 | `taobao.alitrip.it.policy.get` |
| 11 | `taobao.alitrip.it.policy.batchdelete` |
| 12 | `taobao.alitrip.it.policy.add` |
| 13 | `taobao.alitrip.it.policy.update` |

### 国际机票订单API

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.ie.agent.ticket.issue` |
| 2 | `taobao.alitrip.ie.agent.order.hk` |
| 3 | `taobao.alitrip.ie.agent.order.search` |
| 4 | `taobao.alitrip.ie.agent.order.get` |
| 5 | `alitrip.ie.buyer.order.bookpay` |
| 6 | `taobao.alitrip.ie.agent.refund.search` |
| 7 | `taobao.alitrip.ie.agent.change.querychangelist` |
| 8 | `alitrip.tripvp.agent.order.search` |

### 国内机票订单API

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.seller.refundorderlist.fetch` |
| 2 | `taobao.alitrip.seller.refund.confirmreturn` |
| 3 | `taobao.alitrip.seller.refund.get` |
| 4 | `taobao.alitrip.seller.refund.fillfee` |
| 5 | `taobao.alitrip.seller.refund.refusereturn` |
| 6 | `taobao.alitrip.seller.refund.search` |
| 7 | `taobao.alitrip.buyer.get` |
| 8 | `taobao.jipiao.agent.order.bdetail` |
| 9 | `taobao.alitrip.seller.refundmoney.confirm` |
| 10 | `taobao.alitrip.seller.modify.list` |

### 度假&门票-交易管理API (20 APIs)

<details>
<summary>展开查看全部 20 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.travel.trade.memo.add` |
| 2 | `taobao.alitrip.travel.trade.memo.update` |
| 3 | `alitrip.travel.trade.close` |
| 4 | `alitrip.travel.trade.deliver` |
| 5 | `alitrip.travel.trades.search` |
| 6 | `alitrip.travel.trade.query` |
| 7 | `alitrip.travel.trade.template.query` |
| 8 | `alitrip.travel.trade.serviceinfo.write` |
| 9 | `alitrip.travel.visa.applicant.update` |
| 10 | `taobao.travel.ticket.order.verify` |
| 11 | `taobao.travel.ticket.order.refund` |
| 12 | `alitrip.travel.bookinfos.search` |
| 13 | `alitrip.travel.bookinfo.query` |
| 14 | `alitrip.travel.hotelticket.order.create` |
| 15 | `alitrip.travel.hotelticket.order.refund` |
| 16 | `alitrip.travel.hotelticket.order.verify` |
| 17 | `alitrip.travel.hotelticket.product.productupdate` |
| 18 | `alitrip.travel.hotelticket.product.productupdatepush` |
| 19 | `alitrip.travel.recharge.jtp.ordercancel.callback` |
| 20 | `alitrip.travel.phonecard.esim.status.sync` |

</details>

### 阿里体育API (18 APIs)

<details>
<summary>展开查看全部 18 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alisports.passport.account.tokenvalidate` |
| 2 | `alibaba.alisports.passport.account.getaccountinfo` |
| 3 | `alibaba.alisports.passport.oauth.tokenvalidate` |
| 4 | `alibaba.alisports.passport.account.ssotokenvalidate` |
| 5 | `alibaba.alisports.passport.account.ssotokenrefresh` |
| 6 | `alibaba.alisports.passport.parter.synccard` |
| 7 | `alibaba.alisports.passport.account.checkmobile` |
| 8 | `alibaba.alisports.passport.account.delrelation` |
| 9 | `alibaba.alisports.passport.oauth.alipaygrant` |
| 10 | `alibaba.alisports.data.sports.syncstatdata` |
| 11 | `alibaba.alisports.data.sports.syncsportsdata` |
| 12 | `alibaba.alisports.data.sports.syncuserdata` |
| 13 | `alibaba.alisports.data.sports.syncsleepdata` |
| 14 | `alibaba.alisports.passport.account.bindthirdid` |
| 15 | `alibaba.alisports.datacenter.datasync.treadmill` |
| 16 | `alibaba.alisports.passport.auth.accountinfo` |
| 17 | `alibaba.alisports.passport.auth.unbind` |
| 18 | `alibaba.alisports.passport.auth.bind` |

</details>

### 电子发票 (41 APIs)

<details>
<summary>展开查看全部 41 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.einvoice.createreq` |
| 2 | `alibaba.einvoice.create.result.get` |
| 3 | `alibaba.einvoice.create.results.increment.get` |
| 4 | `alibaba.einvoice.partner.return` |
| 5 | `alibaba.einvoice.apply.get` |
| 6 | `alibaba.einvoice.serialno.generate` |
| 7 | `alibaba.einvoice.serialno.batch.generate` |
| 8 | `alibaba.einvoice.amount.check` |
| 9 | `alibaba.einvoice.unitorder.check` |
| 10 | `alibaba.einvoice.invoiceapply.get` |
| 11 | `alibaba.einvoice.invoiceapply.update` |
| 12 | `alibaba.einvoice.merchant.createreq` |
| 13 | `alibaba.einvoice.merchant.result.get` |
| 14 | `alibaba.einvoice.closereq` |
| 15 | `alibaba.einvoice.deduct.get` |
| 16 | `alibaba.einvoice.item.update` |
| 17 | `alibaba.einvoice.red.createreq` |
| 18 | `alibaba.einvoice.prod.result.fileurl.get` |
| 19 | `alibaba.einvoice.device.order.update` |
| 20 | `alibaba.einvoice.device.order.query` |
| 21 | `alibaba.einvoice.prod.apply` |
| 22 | `alibaba.einvoice.core.inv.upload` |
| 23 | `alibaba.einvoice.merchant.bindcompany` |
| 24 | `alibaba.einvoice.merchant.delete` |
| 25 | `alibaba.einvoice.merchant.add` |
| 26 | `alibaba.einvoice.order.refund.update` |
| 27 | `alibaba.einvoice.tax.opt.salaryrequest.singleaccept` |
| 28 | `alibaba.einvoice.tax.opt.salaryaccount.query` |
| 29 | `alibaba.einvoice.tax.opt.salarybill.commitbill` |
| 30 | `alibaba.einvoice.tax.opt.salaryrequest.acceptpayment` |
| 31 | `alibaba.einvoice.tax.opt.esignresult.query` |
| 32 | `alibaba.einvoice.tax.opt.salaryaccount.update` |
| 33 | `alibaba.einvoice.tax.opt.salaryresult.query` |
| 34 | `alibaba.einvoice.flow.tax.get` |
| 35 | `alibaba.einvoice.flow.tax.create` |
| 36 | `alibaba.einvoice.prod.apply.get` |
| 37 | `alibaba.einvoice.flow.renew` |
| 38 | `alibaba.einvoice.flow.refund` |
| 39 | `alibaba.einvoice.tax.opt.billdownloadurl.query` |
| 40 | `alibaba.einvoice.tax.auth.query` |
| 41 | `alibaba.einvoice.payout.get` |

</details>

### SCM_五道口API

| # | API名称 |
|---|--------|
| 1 | `wdk.ums.outbound.sorting.scan.arrival.container` |

### 阿里翻译API

| # | API名称 |
|---|--------|
| 1 | `alibaba.seaking.servicepack` |
| 2 | `alibaba.seaking.imagetranslate.result` |
| 3 | `alibaba.seaking.titlerewrite.submit` |
| 4 | `alibaba.seaking.imagetranslate.submit` |
| 5 | `alibaba.seaking.titlerewrite.result` |
| 6 | `alibaba.seaking.task.report` |
| 7 | `alibaba.seaking.authmachineapi` |
| 8 | `alibaba.seaking.diagnosistitle` |
| 9 | `alibaba.seaking.feedback` |

### 国际站数据管家

| # | API名称 |
|---|--------|
| 1 | `alibaba.mydata.overview.date.get` |
| 2 | `alibaba.mydata.overview.industry.get` |
| 3 | `alibaba.mydata.overview.indicator.basic.get` |
| 4 | `alibaba.mydata.self.product.date.get` |
| 5 | `alibaba.mydata.self.product.get` |

### Yunos Account API

| # | API名称 |
|---|--------|
| 1 | `yunos.account.callapi` |

### 菜鸟裹裹API

| # | API名称 |
|---|--------|
| 1 | `cainiao.nborderfront.user.outside.queryoutsideuser` |
| 2 | `cainiao.nbadd.appointdeliver.feedbackcodes` |
| 3 | `cainiao.endpoint.locker.top.order.withhold` |
| 4 | `cainiao.endpoint.locker.top.withhold.query` |
| 5 | `cainiao.endpoint.locker.top.station.addorupdate` |
| 6 | `cainiao.endpoint.locker.top.order.tracking.new` |
| 7 | `cainiao.endpoint.locker.top.order.noticesend.query` |
| 8 | `cainiao.endpoint.locker.top.order.notice` |
| 9 | `cainiao.guoguo.waybill.get` |
| 10 | `taobao.refund.send.bill.unsettle.query` |

### 淘宝直播API

| # | API名称 |
|---|--------|
| 1 | `taobao.live.game.interact.detail.get` |
| 2 | `taobao.live.game.fund.detail.get` |
| 3 | `taobao.live.game.token.heartbeat` |
| 4 | `taobao.live.game.live.detail.get` |

### 度假-签证管理API

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.travel.normalvisa.storeuser` |
| 2 | `taobao.alitrip.travel.normalvisa.uploadfile` |
| 3 | `taobao.alitrip.travel.normalvisa.updatepersonstauts` |
| 4 | `taobao.alitrip.travel.normalvisa.get` |
| 5 | `taobao.alitrip.travel.normalvisa.getdetail` |
| 6 | `taobao.alitrip.travel.normalvisa.getcompany` |
| 7 | `alitrip.travel.visa.applicant.query` |
| 8 | `alitrip.travel.visa.sign.send` |
| 9 | `alitrip.travel.visa.applicant.import` |

### 服务API

| # | API名称 |
|---|--------|
| 1 | `alibaba.shuqi.original.getclasslist` |

### 体检机构API (26 APIs)

<details>
<summary>展开查看全部 26 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.examination.reserve.confirm` |
| 2 | `alibaba.alihealth.examination.reserve.report` |
| 3 | `alibaba.alihealth.examination.reserve.state` |
| 4 | `alibaba.alihealth.examination.reserve.cancel` |
| 5 | `alibaba.alihealth.examination.hospital.publish` |
| 6 | `alibaba.alihealth.examination.goods.onoffline` |
| 7 | `alibaba.alihealth.examination.goods.publish` |
| 8 | `alibaba.alihealth.examination.agreement.list` |
| 9 | `alibaba.alihealth.examination.items.publish` |
| 10 | `alibaba.alihealth.examination.hospital.special.tag` |
| 11 | `alibaba.alihealth.examination.servicearea.check` |
| 12 | `alibaba.alihealth.examination.reserve.modify.notify` |
| 13 | `alibaba.alihealth.examination.reserve.state.notify` |
| 14 | `alibaba.alihealth.examination.reserve.isv.modify` |
| 15 | `alibaba.alihealth.examination.todoor.serviceinfo.sync` |
| 16 | `alibaba.alihealth.examination.invoice.info.notify` |
| 17 | `alibaba.alihealth.examination.reserve.report.nofify` |
| 18 | `alibaba.alihealth.examination.report.diagnose.order.submit` |
| 19 | `alibaba.alihealth.examination.report.diagnose.order.summary` |
| 20 | `alibaba.alihealth.examination.report.diagnose.order.status` |
| 21 | `alibaba.alihealth.examination.report.diagnose.tempmessage.receive` |
| 22 | `alibaba.alihealth.examination.report.diagnose.file.code.get` |
| 23 | `alibaba.alihealth.examination.report.diagnose.order.doctor.refund` |
| 24 | `alibaba.alihealth.examination.report.diagnose.order.diagnoseurl.get` |
| 25 | `alibaba.alihealth.examination.report.diagnose.order.verify` |
| 26 | `alibaba.alihealth.medical.order.refund` |

</details>

### 1688推客API

| # | API名称 |
|---|--------|
| 1 | `alibaba.tuike.offer.get` |
| 2 | `alibaba.tuike.offer.zhitoken` |

### 商户API

| # | API名称 |
|---|--------|
| 1 | `taobao.place.storegroup.create` |
| 2 | `taobao.place.storerelatesub.delete` |
| 3 | `taobao.place.storerelatesub.add` |
| 4 | `taobao.place.storegroup.update` |
| 5 | `taobao.place.storegroup.delete` |
| 6 | `taobao.place.storerelatesub.get` |
| 7 | `taobao.place.store.query` |
| 8 | `taobao.place.store.extend.update` |
| 9 | `taobao.place.store.update.label` |
| 10 | `taobao.place.store.relation.query` |

### 桌面API

| # | API名称 |
|---|--------|
| 1 | `yunos.tvscreen.launcher.get` |
| 2 | `youku.ott.playservice.getplayurl` |
| 3 | `youku.ott.alicb.facadeservice.getdata` |
| 4 | `yunos.tvscreen.lge.launcher.get` |

### 电动车API

| # | API名称 |
|---|--------|
| 1 | `cainiao.vms.service.vehicleinfo.upload` |

### 淘宝在线教育

| # | API名称 |
|---|--------|
| 1 | `taobao.edu.charge.zc.updatesupplierorder` |
| 2 | `taobao.edu.charge.zc.audit` |

### 新零售API

| # | API名称 |
|---|--------|
| 1 | `alibaba.it.ap.address.set` |
| 2 | `alibaba.it.ap.address.get` |

### SCM API

| # | API名称 |
|---|--------|
| 1 | `alibaba.ascm.settlement.invoice.synchronization.im` |

### 百川-ctg

| # | API名称 |
|---|--------|
| 1 | `alibaba.baichuan.ctg.toutiao.content` |

### 汇金API

| # | API名称 |
|---|--------|
| 1 | `alibaba.fundplatform.cardorders.status.make.finish` |
| 2 | `alibaba.fundplatform.cardorders.status.sended` |
| 3 | `alibaba.fundplatform.cardorder.make` |
| 4 | `alibaba.fundplatform.cardorder.status.query` |
| 5 | `alibaba.fundplatform.cardorders.info.query` |
| 6 | `alibaba.fundplatform.card.template.new` |
| 7 | `alibaba.fundplatform.cardorder.make.success` |
| 8 | `alibaba.fundplatform.account.charge` |
| 9 | `alibaba.fundplatform.account.query.info` |
| 10 | `alibaba.tax.invoice.sync.ledger` |
| 11 | `alibaba.cfo.incoming.invoice.ledger.fullysync` |
| 12 | `alibaba.cfo.incoming.invoice.redconfirmation.syn` |
| 13 | `alibaba.cfo.incoming.invoice.redconfirmation.actionresult` |
| 14 | `alibaba.cfo.incoming.invoice.ledger.pyt.sync` |

### 数娱媒资输出

| # | API名称 |
|---|--------|
| 1 | `youku.wenyuvideo.persion.search` |
| 2 | `youku.wenyuvideo.persion.get` |
| 3 | `youku.wenyuvideo.seeta.get` |

### 商旅API (124 APIs)

<details>
<summary>展开查看全部 124 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alitrip.btrip.approval.update` |
| 2 | `alitrip.btrip.approval.new` |
| 3 | `alitrip.btrip.cost.center.get` |
| 4 | `alitrip.btrip.invoice.search` |
| 5 | `alitrip.btrip.invoice.get` |
| 6 | `alitrip.btrip.hotel.order.search` |
| 7 | `alitrip.btrip.apply.search` |
| 8 | `alitrip.btrip.apply.get` |
| 9 | `alitrip.btrip.flight.order.search` |
| 10 | `alitrip.btrip.train.order.search` |
| 11 | `alitrip.btrip.train.city.suggest` |
| 12 | `alitrip.btrip.flight.city.suggest` |
| 13 | `alitrip.btrip.cost.center.delete` |
| 14 | `alitrip.btrip.cost.center.entity.add` |
| 15 | `alitrip.btrip.cost.center.new` |
| 16 | `alitrip.btrip.cost.center.modify` |
| 17 | `alitrip.btrip.cost.center.entity.set` |
| 18 | `alitrip.btrip.cost.center.entity.delete` |
| 19 | `alitrip.btip.cost.center.query` |
| 20 | `alitrip.btrip.vehicle.order.search` |
| 21 | `alitrip.btrip.cost.center.transfer` |
| 22 | `alitrip.btrip.approval.modify` |
| 23 | `alitrip.btrip.openplatform.address.get` |
| 24 | `alitrip.btrip.corpop.user.sync` |
| 25 | `alitrip.btrip.corpop.depart.sync` |
| 26 | `alitrip.btrip.corpop.apply.add` |
| 27 | `alitrip.btrip.corpop.apply.approve` |
| 28 | `alitrip.btrip.supplychain.vehicle.search` |
| 29 | `alitrip.btrip.supplychain.hotel.search` |
| 30 | `alitrip.btrip.supplychain.train.search` |
| 31 | `alitrip.btrip.supplychain.flight.search` |
| 32 | `alitrip.btrip.corpop.apply.get` |
| 33 | `alitrip.btrip.corpop.apply.search` |
| 34 | `alitrip.btrip.corpop.apply.modify` |
| 35 | `alitrip.btrip.open.cost.center.new` |
| 36 | `alitrip.btrip.monthbill.url.get` |
| 37 | `alitrip.btrip.project.add` |
| 38 | `alitrip.btrip.project.delete` |
| 39 | `alitrip.btrip.invoice.setting.modify` |
| 40 | `alitrip.btrip.supplychain.flight.city` |
| 41 | `alitrip.btrip.project.modify` |
| 42 | `alitrip.btrip.invoice.setting.add` |
| 43 | `alitrip.btrip.invoice.setting.delete` |
| 44 | `alitrip.btrip.invoice.setting.rule` |
| 45 | `alitrip.btrip.open.cost.center.modify` |
| 46 | `alitrip.btrip.open.cost.center.delete` |
| 47 | `alitrip.btrip.open.cost.center.query` |
| 48 | `alitrip.btrip.open.cost.center.entity.set` |
| 49 | `alitrip.btrip.open.cost.center.entity.add` |
| 50 | `alitrip.btrip.open.cost.center.entity.delete` |
| 51 | `alitrip.btrip.open.cost.center.transfer` |
| 52 | `alitrip.btrip.supplychain.train.city` |
| 53 | `alitrip.btrip.open.invoice.search` |
| 54 | `alitrip.btrip.city.car.apply.add` |
| 55 | `alitrip.btrip.city.car.apply.query` |
| 56 | `alitrip.btrip.city.car.apply.approve` |
| 57 | `alitrip.btrip.open.supplychain.flight.trade` |
| 58 | `alitrip.btrip.open.supplychain.hotel.trade` |
| 59 | `alitrip.btrip.open.supplychain.train.trade` |
| 60 | `alitrip.btrip.open.supplychain.vehicle.trade` |
| 61 | `alitrip.btrip.hotel.distribution.search.static` |
| 62 | `alitrip.btrip.hotel.distribution.search.low.price` |
| 63 | `alitrip.btrip.hotel.distribution.search.detail` |
| 64 | `alitrip.btrip.hotel.distribution.order.cancel` |
| 65 | `alitrip.btrip.hotel.distribution.order.pay` |
| 66 | `alitrip.btrip.hotel.distribution.order.create` |
| 67 | `alitrip.btrip.hotel.distribution.order.validate` |
| 68 | `alitrip.btrip.hotel.distribution.order.detail` |
| 69 | `alitrip.btrip.supplychain.train.industry.search` |
| 70 | `alitrip.btrip.supplychain.bus.industry.search` |
| 71 | `alitrip.btrip.supplychain.flight.industry.search` |
| 72 | `alitrip.btrip.employee.query` |
| 73 | `alitrip.btrip.corpop.exceedapply.sync` |
| 74 | `alitrip.btrip.flight.distribution.flightlist` |
| 75 | `alitrip.btrip.flight.distribution.order.create` |
| 76 | `alitrip.btrip.flight.distribution.order.detail` |
| 77 | `alitrip.btrip.flight.distribution.change.detail` |
| 78 | `alitrip.btrip.flight.distribution.order.cancel` |
| 79 | `alitrip.btrip.flight.distribution.order.pay` |
| 80 | `alitrip.btrip.corpop.flight.exceedapply.get` |
| 81 | `alitrip.btrip.flight.distribution.change.apply` |
| 82 | `alitrip.btrip.flight.distribution.change.pay` |
| 83 | `alitrip.btrip.flight.distribution.change.query` |
| 84 | `alitrip.btrip.flight.distribution.refund.precal` |
| 85 | `alitrip.btrip.flight.distribution.refund.detail` |
| 86 | `alitrip.btrip.flight.distribution.refund.apply` |
| 87 | `alitrip.btrip.flight.distribution.modify.flightsearch` |
| 88 | `alitrip.btrip.corpop.train.exceedapply.get` |
| 89 | `alitrip.btrip.corpop.hotel.exceedapply.get` |
| 90 | `alitrip.btrip.corpop.car.billsettlement.query` |
| 91 | `alitrip.btrip.corpop.flight.billsettlement.query` |
| 92 | `alitrip.btrip.corpop.hotel.billsettlement.query` |
| 93 | `alitrip.btrip.corpop.btriptrain.billsettlement.query` |
| 94 | `alitrip.btrip.flight.distribution.change.cancel` |
| 95 | `alitrip.btrip.corpop.commonapply.get` |
| 96 | `alitrip.btrip.flight.distribution.account` |
| 97 | `alitrip.btrip.supplychain.train.detail.search` |
| 98 | `alitrip.btrip.supplychain.flight.detail.search` |
| 99 | `alitrip.btrip.flight.distribution.modify.newflightsearch` |
| 100 | `alitrip.btrip.flight.distribution.newflightlist` |
| 101 | `alitrip.btrip.flight.distribution.order.newcreate` |
| 102 | `alitrip.btrip.flight.distribution.order.newpay` |
| 103 | `alitrip.btrip.flight.distribution.change.newquery` |
| 104 | `alitrip.btrip.flight.distribution.change.newapply` |
| 105 | `alitrip.btrip.flight.distribution.change.newpay` |
| 106 | `alitrip.btrip.flight.distribution.change.newdetail` |
| 107 | `alitrip.btrip.flight.distribution.change.newcancel` |
| 108 | `alitrip.btrip.flight.distribution.refund.newprecal` |
| 109 | `alitrip.btrip.flight.distribution.refund.newapply` |
| 110 | `alitrip.btrip.flight.distribution.refund.newdetail` |
| 111 | `alitrip.btrip.supplychain.train.detail.search.vtwo` |
| 112 | `alitrip.btrip.hotel.distribution.search.hot.hotel` |
| 113 | `alitrip.btrip.supplychain.vacation.user.tokenuser.get` |
| 114 | `alitrip.btrip.supplychain.vacation.order.query` |
| 115 | `alitrip.btrip.supplychain.vacation.order.cancel` |
| 116 | `alitrip.btrip.supplychain.vacation.order.payment.address` |
| 117 | `alitrip.btrip.supplychain.vacation.order.precreate` |
| 118 | `alitrip.btrip.supplychain.vacation.order.notify` |
| 119 | `alitrip.btrip.supplychain.vacation.order.create` |
| 120 | `alitrip.btrip.supplychain.vacation.order.refundtouser` |
| 121 | `alitrip.btrip.supplychain.vacation.suborder.create` |
| 122 | `alitrip.btrip.supplychain.vacation.suborder.notify` |
| 123 | `alitrip.btrip.supplychain.vacation.suborder.refundtouser` |
| 124 | `alitrip.btrip.supplychain.vacation.suborder.cancel` |

</details>

### 零售plus

| # | API名称 |
|---|--------|
| 1 | `alibaba.nlife.b2c.trade.cancel` |
| 2 | `alibaba.nlife.b2c.trade.refund` |
| 3 | `alibaba.nlife.b2c.trade.pay` |
| 4 | `alibaba.nlife.b2c.trade.get` |
| 5 | `alibaba.nlife.b2c.trade.download` |
| 6 | `alibaba.nlife.b2c.item.detail.get` |
| 7 | `alibaba.nlife.b2c.code.convert` |
| 8 | `alibaba.nlife.b2c.member.discountrule.get` |
| 9 | `alibaba.nlife.b2c.tradestatus.drive` |

### 天猫门店API

| # | API名称 |
|---|--------|
| 1 | `tmall.store.order.create` |
| 2 | `alibaba.retail.electronic.certificate.confirm` |
| 3 | `alibaba.retail.electronic.certificate.pre.confirm` |

### AILAB图像算法API

| # | API名称 |
|---|--------|
| 1 | `alibaba.ai.ar.service.detect` |
| 2 | `alibaba.ai.ar.tmjl.app.detect` |
| 3 | `alibaba.ai.ar.open.platform.detect` |

### 天猫供应链 (65 APIs)

<details>
<summary>展开查看全部 65 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.ascp.pricing.scm.tof` |
| 2 | `alibaba.dchain.aoxiang.channel.inventory.batch.upload` |
| 3 | `alibaba.dchain.aoxiang.scitem.batch.create` |
| 4 | `alibaba.dchain.aoxiang.scitem.batch.update` |
| 5 | `alibaba.dchain.aoxiang.combinescitem.batch.create` |
| 6 | `alibaba.dchain.aoxiang.combinescitem.batch.update` |
| 7 | `alibaba.dchain.aoxiang.itemmapping.batch.create` |
| 8 | `alibaba.dchain.aoxiang.consignorder.batch.query` |
| 9 | `alibaba.dchain.aoxiang.receiverinfo.query` |
| 10 | `alibaba.dchain.aoxiang.item.distribution.create` |
| 11 | `alibaba.dchain.aoxiang.item.distribution.update` |
| 12 | `alibaba.dchain.aoxiang.item.distribution.batch.cancel` |
| 13 | `alibaba.dchain.aoxiang.cooperate.distributor.query` |
| 14 | `alibaba.dchain.aoxiang.item.distribution.describe` |
| 15 | `alibaba.dchain.aoxiang.wms.deliveryorder.create` |
| 16 | `alibaba.dchain.aoxiang.wms.deliveryorder.confirm` |
| 17 | `alibaba.dchain.aoxiang.wms.orderprocess.report` |
| 18 | `alibaba.dchain.aoxiang.wms.order.cancel` |
| 19 | `alibaba.dchain.aoxiang.warehouse.create.update` |
| 20 | `alibaba.dchain.aoxiang.warehouse.status.update` |
| 21 | `alibaba.dchain.aoxiang.delivery.create.update` |
| 22 | `alibaba.dchain.aoxiang.delivery.status.update` |
| 23 | `alibaba.dchain.aoxiang.item.batch.update.async` |
| 24 | `alibaba.dchain.aoxiang.combineitem.batch.update.async` |
| 25 | `alibaba.dchain.aoxiang.item.batch.delete.async` |
| 26 | `alibaba.dchain.aoxiang.itemmapping.update.async` |
| 27 | `alibaba.dchain.aoxiang.itemmapping.delete` |
| 28 | `alibaba.dchain.aoxiang.physics.inventory.batch.upload.async` |
| 29 | `alibaba.dchain.isv.wms.orderprocess.report` |
| 30 | `alibaba.dchain.aoxiang.scitem.query` |
| 31 | `alibaba.dchain.aoxiang.inventory.batch.query` |
| 32 | `alibaba.dchain.aoxiang.itemmapping.unbundle` |
| 33 | `alibaba.dchain.aoxiang.delivery.decision.query` |
| 34 | `alibaba.ascp.industry.anomaly.recourse.status.modify` |
| 35 | `alibaba.ascp.suborder.estcontime.modify` |
| 36 | `taobao.logistics.express.delivery.resource.create` |
| 37 | `taobao.logistics.express.delivery.send.ability.async` |
| 38 | `alibaba.ascp.industry.inquiry.extracharge.cancel` |
| 39 | `taobao.logistics.warehouse.resource.update` |
| 40 | `taobao.logistics.warehouse.cooperation.batch.confirm` |
| 41 | `taobao.logistics.warehouse.cooperation.query` |
| 42 | `taobao.logistics.warehouse.cooperation.update` |
| 43 | `taobao.logistics.warehouse.operation.update` |
| 44 | `taobao.logistics.warehouse.capacity.rule.update` |
| 45 | `taobao.logistics.delivery.line.batch.update` |
| 46 | `taobao.logistics.delivery.line.batch.delete` |
| 47 | `taobao.logistics.express.collect.resource.tms.async` |
| 48 | `taobao.logistics.express.site.tms.sync` |
| 49 | `taobao.logistics.media.resources.upload` |
| 50 | `taobao.logistics.express.address.blacklist.tms.delete` |
| 51 | `taobao.logistics.express.address.blacklist.tms.async` |
| 52 | `taobao.logistics.express.user.blacklist.tms.sync` |
| 53 | `taobao.logistics.express.collect.resource.tms.delete` |
| 54 | `taobao.logistics.address.query` |
| 55 | `taobao.logistics.station.tms.async` |
| 56 | `taobao.logistics.address.ability.tms.async` |
| 57 | `taobao.logistics.station.ability.tms.async` |
| 58 | `taobao.logistics.express.delivery.shsm.call.request` |
| 59 | `taobao.tmhk.jingya.thirdpartwarehouse.inventory.sync` |
| 60 | `taobao.logistics.express.courier.region.async` |
| 61 | `taobao.logistics.express.courier.region.code.async` |
| 62 | `taobao.logistics.express.courier.region.delete` |
| 63 | `taobao.logistics.package.exception.query` |
| 64 | `taobao.logistics.package.exception.config.query` |
| 65 | `taobao.sn.manage.consign.report` |

</details>

### 欢行开发平台API (24 APIs)

<details>
<summary>展开查看全部 24 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.happytrip.taxi.order.confirm` |
| 2 | `alibaba.happytrip.taxi.order.get` |
| 3 | `alibaba.happytrip.taxi.order.create` |
| 4 | `alibaba.happytrip.taxi.price.get` |
| 5 | `alibaba.happytrip.taxi.id.get` |
| 6 | `alibaba.happytrip.taxi.order.complain` |
| 7 | `alibaba.happytrip.taxi.order.cancel` |
| 8 | `alibaba.happytrip.taxi.order.notify` |
| 9 | `alibaba.happytrip.taxi.order.score` |
| 10 | `alibaba.happytrip.taxi.servicestatus.get` |
| 11 | `alibaba.happytrip.order.get` |
| 12 | `alibaba.happytrip.taxi.provider.account.balance` |
| 13 | `alibaba.happytrip.freelogin.getusercontext` |
| 14 | `alibaba.happytrip.taxi.order.destination.modify` |
| 15 | `alibaba.htorder.hotel.sync.config` |
| 16 | `alibaba.htorder.hotel.sync.booking` |
| 17 | `alibaba.happytrip.taxi.order.complaint.get` |
| 18 | `alibaba.happytrip.taxi.order.assign` |
| 19 | `alibaba.happytrip.taxi.driver.location.get` |
| 20 | `alibaba.happytrip.taxi.driver.blacklist.remove` |
| 21 | `alibaba.happytrip.taxi.driver.blacklist.add` |
| 22 | `alibaba.htcoupon.fulu.phonecharge.callback` |
| 23 | `alibaba.happytrip.taxi.order.passingpoints.modify` |
| 24 | `alibaba.happytrip.bank.bill.notify` |

</details>

### 迎客松牌照审核接口 (92 APIs)

<details>
<summary>展开查看全部 92 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `yunos.tvpubadmin.device.models` |
| 2 | `yunos.tvpubadmin.device.brands` |
| 3 | `yunos.tvpubadmin.device.stats` |
| 4 | `yunos.tvpubadmin.device.apkinfo` |
| 5 | `yunos.tvpubadmin.diccontroltask.update` |
| 6 | `yunos.tvpubadmin.content.channel.query` |
| 7 | `yunos.tvpubadmin.diccontroltask.add` |
| 8 | `yunos.tvpubadmin.diccontroltask.getinfo` |
| 9 | `yunos.tvpubadmin.content.channel.offline` |
| 10 | `yunos.tvpubadmin.device.tvid` |
| 11 | `yunos.tvpubadmin.content.topic.querytopic` |
| 12 | `yunos.tvpubadmin.device.updateosstatus` |
| 13 | `yunos.tvpubadmin.device.updateappstatus` |
| 14 | `yunos.tvpubadmin.content.tableaudit.querymetaitem` |
| 15 | `yunos.tvpubadmin.content.device.getterminaltypemap` |
| 16 | `yunos.tvpubadmin.content.show.setexemptaudit` |
| 17 | `yunos.tvpubadmin.content.show.getshowexemptauditmap` |
| 18 | `yunos.tvpubadmin.content.topic.offline` |
| 19 | `yunos.tvpubadmin.content.show.getbyshowlongid` |
| 20 | `yunos.tvpubadmin.content.show.getbyshowid` |
| 21 | `yunos.tvpubadmin.content.advert.queryschedule` |
| 22 | `yunos.tvpubadmin.content.advert.manageschedule` |
| 23 | `yunos.tvpubadmin.content.video.submitauditresult` |
| 24 | `yunos.tvpubadmin.content.tableaudit.querylauncher` |
| 25 | `yunos.tvpubadmin.content.video.getauditlist` |
| 26 | `yunos.tvpubadmin.content.tableaudit.offlinelauncheritem` |
| 27 | `yunos.tvpubadmin.content.device.getvendor` |
| 28 | `yunos.tvpubadmin.content.advert.gettypes` |
| 29 | `yunos.tvpubadmin.content.tableaudit.querychilddesktop` |
| 30 | `yunos.tvpubadmin.content.app.onoffappbylicense` |
| 31 | `yunos.tvpubadmin.content.app.queryapp` |
| 32 | `yunos.tvpubadmin.content.app.querybylicence` |
| 33 | `yunos.tvpubadmin.user.orderlist` |
| 34 | `yunos.tvpubadmin.user.rights` |
| 35 | `yunos.tvpubadmin.device.osupgradequery` |
| 36 | `yunos.tvpubadmin.device.query` |
| 37 | `yunos.tvpubadmin.device.appupgradedetail` |
| 38 | `yunos.tvpubadmin.device.osupgradedetail` |
| 39 | `yunos.tvpubadmin.user.suggest` |
| 40 | `yunos.tvpubadmin.device.appupgradequery` |
| 41 | `yunos.tvpubadmin.device.apks` |
| 42 | `yunos.tvpubadmin.diccontroltask.query` |
| 43 | `yunos.tvpubadmin.content.single.video.submitauditresult` |
| 44 | `yunos.tvpubadmin.content.single.video.getlist` |
| 45 | `yunos.tvpubadmin.content.show.getlist` |
| 46 | `yunos.tvpubadmin.content.child.leafnode.get` |
| 47 | `yunos.tvpubadmin.content.child.rootnode.get` |
| 48 | `yunos.tvpubadmin.content.child.nodeitem.offline` |
| 49 | `yunos.tvpubadmin.content.child.recoitem.query` |
| 50 | `yunos.tvpubadmin.content.child.recoitem.offline` |
| 51 | `yunos.tvpubadmin.content.child.nodeitem.query` |
| 52 | `yunos.tvpubadmin.data.query` |
| 53 | `yunos.tvpubadmin.epg.desktop.operation` |
| 54 | `yunos.tvpubadmin.manage.topic.contentdelete` |
| 55 | `yunos.tvpubadmin.manage.dialog.delete` |
| 56 | `yunos.tvpubadmin.manage.dialog.findbyid` |
| 57 | `yunos.tvpubadmin.manage.dialog.edit` |
| 58 | `yunos.tvpubadmin.manage.dialog.add` |
| 59 | `yunos.tvpubadmin.manage.dialog.list` |
| 60 | `yunos.tvpubadmin.manage.topic.findbyid` |
| 61 | `yunos.tvpubadmin.manage.topic.list` |
| 62 | `yunos.tvpubadmin.manage.topic.contentadd` |
| 63 | `yunos.tvpubadmin.manage.topic.contentlist` |
| 64 | `yunos.tvpubadmin.manage.topic.edit` |
| 65 | `yunos.tvpubadmin.manage.topic.add` |
| 66 | `yunos.tvpubadmin.common.file.upload` |
| 67 | `yunos.osupdate.appversion.query` |
| 68 | `yunos.osupdate.versionstatus.update` |
| 69 | `yunos.osupdate.appversion.create` |
| 70 | `yunos.osupdate.appversion.update` |
| 71 | `yunos.osupdate.model.search` |
| 72 | `yunos.osupdate.appversion.info` |
| 73 | `yunos.osupdate.osfota.query` |
| 74 | `yunos.osupdate.osfota.add` |
| 75 | `yunos.osupdate.osfota.publish` |
| 76 | `yunos.osupdate.appversion.publish` |
| 77 | `yunos.osupdate.deviceservice.searchmodels` |
| 78 | `yunos.tvpubadmin.adm.ott.audit` |
| 79 | `yunos.tvpubadmin.adm.ott.query` |
| 80 | `yunos.trade.admin.common.operation` |
| 81 | `yunos.tvpubadmin.content.show.edit` |
| 82 | `yunos.tvmbos.common.operation` |
| 83 | `yunos.tvpubadmin.manage.topic.contentedit` |
| 84 | `yunos.pubadmin.common.operation` |
| 85 | `yunos.tvscreen.admin.common.operation` |
| 86 | `yunos.tvpubadmin.device.yks.skill.online` |
| 87 | `yunos.tvpubadmin.device.yks.skill.add` |
| 88 | `yunos.tvpubadmin.device.yks.skill.offline` |
| 89 | `yunos.tvpubadmin.device.yks.skill.delete` |
| 90 | `yunos.tvpubadmin.device.yks.skill.modify` |
| 91 | `yunos.tvpubadmin.device.yks.skills` |
| 92 | `yunos.tvpubadmin.device.yks.bots` |

</details>

### IoTI API

| # | API名称 |
|---|--------|
| 1 | `alibaba.it.esl.eslimage.sendimage` |
| 2 | `alibaba.it.esl.sendota` |
| 3 | `alibaba.it.esl.sendled` |
| 4 | `alibaba.it.album.device.sendimage` |
| 5 | `alibaba.it.esl.eslimage.showimagecommon` |
| 6 | `alibaba.it.esl.eslinfo.geteslinfo` |

### 淘宝卡券平台

| # | API名称 |
|---|--------|
| 1 | `taobao.game.deliveryvoucher.sendvoucher` |
| 2 | `taobao.game.deliveryvoucher.sendgoods` |
| 3 | `taobao.game.deliveryvoucher.cancelvoucher` |
| 4 | `taobao.game.deliveryvoucher.rollbackvoucher` |
| 5 | `taobao.game.deliveryvoucher.ordervoucher` |
| 6 | `taobao.game.deliveryvoucher.watch` |
| 7 | `taobao.game.deliveryvoucher.evaluate` |

### 智慧门店

| # | API名称 |
|---|--------|
| 1 | `tmall.popupstore.activity.query` |
| 2 | `tmall.popupstore.activity.device.query` |
| 3 | `taobao.istore.areas.get` |

### 淘宝定制行业API

| # | API名称 |
|---|--------|
| 1 | `taobao.market.picture.getuserpictures` |
| 2 | `tmall.industry.baby.authprofile.backflow` |
| 3 | `taobao.industry.dajian.rp.pickup.result` |
| 4 | `taobao.industry.dajian.rp.appoint.modify` |
| 5 | `tmall.servicecenter.inspect.order.item.info.query` |
| 6 | `tmall.servicecenter.inspect.result.sync` |
| 7 | `taobao.industry.unite.goods.logistics.detail` |
| 8 | `taobao.industry.yp.warehouse.defect.identify.result` |

### 闲鱼 (157 APIs)

<details>
<summary>展开查看全部 157 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.recycle.order.fulfillment` |
| 2 | `alibaba.idle.recycle.spu.template.modify` |
| 3 | `alibaba.idle.recycle.inspection.report` |
| 4 | `alibaba.idle.recycle.order.query` |
| 5 | `alibaba.idle.recycle.order.perform` |
| 6 | `taobao.idle.recycle.refund.detail` |
| 7 | `alibaba.idle.consignment.order.get` |
| 8 | `alibaba.idle.consignment.order.perform` |
| 9 | `alibaba.idle.consignment.spu.statistics` |
| 10 | `alibaba.idle.rent.item.add` |
| 11 | `alibaba.idle.rent.item.edit` |
| 12 | `alibaba.idle.rent.media.upload` |
| 13 | `alibaba.idle.rent.item.sku.update` |
| 14 | `alibaba.idle.rent.item.query` |
| 15 | `alibaba.idle.rent.order.logistics.deliver` |
| 16 | `alibaba.idle.rent.order.package` |
| 17 | `alibaba.idle.rent.order.query` |
| 18 | `alibaba.idle.rent.order.senditem` |
| 19 | `alibaba.idle.rent.order.receiveitem` |
| 20 | `alibaba.idle.rent.order.checkstatus.upload` |
| 21 | `alibaba.idle.agreement.pay` |
| 22 | `alibaba.idle.agreement.pay.query` |
| 23 | `alibaba.idle.pay.plan.create` |
| 24 | `alibaba.idle.recycle.order.show` |
| 25 | `alibaba.idle.appraise.order.query` |
| 26 | `alibaba.idle.appraise.order.perform` |
| 27 | `alibaba.idle.appraise.spu.register.modify` |
| 28 | `alibaba.idle.transferpay.query` |
| 29 | `alibaba.idle.spu.register.modify` |
| 30 | `alibaba.idle.isv.order.dealrefund` |
| 31 | `alibaba.idle.consignmentii.order.perform` |
| 32 | `alibaba.idle.consignmentii.order.get` |
| 33 | `alibaba.idle.user.permit` |
| 34 | `alibaba.idle.order.dummy.send` |
| 35 | `alibaba.idle.tender.order.get` |
| 36 | `alibaba.idle.tender.upload.report` |
| 37 | `alibaba.xianyu.tender.order.perform` |
| 38 | `alibaba.idle.tender.btob.item.upload` |
| 39 | `alibaba.idle.tender.btob.item.delete` |
| 40 | `alibaba.idle.tender.btob.item.query` |
| 41 | `alibaba.idle.template.ques.get` |
| 42 | `alibaba.idle.template.ques.online` |
| 43 | `alibaba.idle.tender.aftersale.order.perform` |
| 44 | `alibaba.idle.tender.aftersale.order.get` |
| 45 | `alibaba.idle.car.order.query` |
| 46 | `alibaba.idle.report.media.upload` |
| 47 | `alibaba.idle.report.result.upload` |
| 48 | `alibaba.idle.onespu.register.update` |
| 49 | `alibaba.idle.autotrade.isv.order.state.process` |
| 50 | `alibaba.idle.isv.item.recharge.batch.remove` |
| 51 | `alibaba.idle.isv.item.recharge.edit` |
| 52 | `alibaba.idle.adv.material.upload` |
| 53 | `alibaba.idle.isv.goosefish.order.create` |
| 54 | `alibaba.idle.goosefish.user.info.query` |
| 55 | `alibaba.idle.goosefish.promotion.activity.info.query` |
| 56 | `alibaba.idle.quote.record.query` |
| 57 | `alibaba.idle.consignment.other.channels.upload` |
| 58 | `alibaba.idle.isv.order.after.send.refund` |
| 59 | `alibaba.idle.isv.order.part.refund` |
| 60 | `alibaba.idle.isv.goosefish.order.sellercreate` |
| 61 | `alibaba.idle.isv.goosefish.order.confirmdisburse` |
| 62 | `alibaba.idle.isv.order.buyer.refund` |
| 63 | `alibaba.idle.isv.goosefish.virtual.delivery` |
| 64 | `alibaba.idle.goosefish.trade.extra.data.query` |
| 65 | `alibaba.idle.market.recycle.order.show` |
| 66 | `alibaba.idle.market.recycle.order.fulfillment` |
| 67 | `alibaba.idle.interact.loan.score.query` |
| 68 | `alibaba.idle.interact.loan.user.query` |
| 69 | `alibaba.idle.interact.loan.user.put` |
| 70 | `alibaba.idle.interact.loan.phone.query` |
| 71 | `alibaba.idle.interact.loan.sms.code.send` |
| 72 | `alibaba.idle.interact.loan.sms.code.check` |
| 73 | `alibaba.idle.open.play.zdm.game.complete` |
| 74 | `alibaba.idle.tender.btob.item.cancel` |
| 75 | `alibaba.idle.open.play.minigame.data` |
| 76 | `alibaba.idle.trendy.good.value.change.submit` |
| 77 | `alibaba.idle.coin.task.trigger` |
| 78 | `alibaba.idle.tender.aftersale.order.query` |
| 79 | `alibaba.idle.isv.trendy.presale.balance.initiate` |
| 80 | `alibaba.idle.isv.trendy.presale.seller.order.close` |
| 81 | `alibaba.idle.sechandcar.isv.seller.membership.query` |
| 82 | `alibaba.idle.isv.user.phone.query` |
| 83 | `alibaba.idle.yushi.btob.tongshou.auction.end` |
| 84 | `alibaba.idle.local.storegroup.store.info.query` |
| 85 | `alibaba.idle.local.storegroup.store.group.query` |
| 86 | `alibaba.idle.yushi.tongshou.first.bid.upload` |
| 87 | `alibaba.idle.yushi.tongshou.buyer.bid.upload` |
| 88 | `alibaba.idle.yushi.tongshou.item.upload` |
| 89 | `alibaba.idle.yushi.aftersale.tongshou.order.perform` |
| 90 | `alibaba.idle.yushi.tongshou.order.perform` |
| 91 | `alibaba.idle.yushi.tongshou.aftersale.order.start` |
| 92 | `alibaba.idle.yushi.btob.tongshou.auction.batch.end` |
| 93 | `alibaba.idle.sn.report.save` |
| 94 | `alibaba.idle.interact.loan.callback` |
| 95 | `alibaba.idle.fishmarket.buyer.order.get` |
| 96 | `alibaba.idle.fishmarket.fixed.order.perform` |
| 97 | `alibaba.idle.interact.loan.push` |
| 98 | `alibaba.idle.open.task.trigger` |
| 99 | `alibaba.idle.open.isv.recycle.order.status.query` |
| 100 | `alibaba.idle.open.task.callback` |
| 101 | `alibaba.idle.isv.open.user.age.info.query` |
| 102 | `alibaba.idle.isv.open.user.bind.account.query` |
| 103 | `alibaba.idle.trendy.game.item.query` |
| 104 | `alibaba.idle.interact.loan.user.realname.info` |
| 105 | `alibaba.idle.trendy.game.item.down.shelf` |
| 106 | `alibaba.idle.trendy.game.item.edit` |
| 107 | `alibaba.idle.trendy.game.item.batch.query` |
| 108 | `alibaba.idle.trendy.game.order.query` |
| 109 | `alibaba.idle.trendy.game.order.delivery` |
| 110 | `alibaba.idle.trendy.game.order.refund` |
| 111 | `alibaba.idle.trendy.game.item.publish` |
| 112 | `alibaba.idle.trendy.game.boosting.order.perform` |
| 113 | `alibaba.idle.trendy.handbook.update` |
| 114 | `alibaba.idle.trendy.handbook.image.upload` |
| 115 | `alibaba.idle.trendy.handbook.market.sync` |
| 116 | `alibaba.idle.trendy.handbook.insert` |
| 117 | `alibaba.idle.recycle.order.extend.event` |
| 118 | `alibaba.idle.isv.fishmarket.item.publish` |
| 119 | `alibaba.idle.isv.fishmarket.auction.query` |
| 120 | `alibaba.idle.isv.fishmarket.bid.write` |
| 121 | `alibaba.idle.isv.fishmarket.seller.query` |
| 122 | `alibaba.idle.isv.fishmarket.order.query` |
| 123 | `alibaba.idle.isv.fishmarket.order.perform` |
| 124 | `alibaba.idle.recycle.inspect.autotool.report.save` |
| 125 | `alibaba.idle.isv.item.qrcode.generate` |
| 126 | `alibaba.idle.recycle.inspect.machine.report.save` |
| 127 | `alibaba.idle.isv.fishmarket.item.query` |
| 128 | `alibaba.idle.bid.after.sale.cancle` |
| 129 | `alibaba.idle.fishmarket.after.sale.responsible.perform` |
| 130 | `alibaba.idle.fishmarket.after.sale.start` |
| 131 | `alibaba.idle.fishmarket.after.sale.query` |
| 132 | `alibaba.idle.fishmarket.after.sale.arbplatform.perform` |
| 133 | `alibaba.idle.open.game.order.query` |
| 134 | `alibaba.idle.open.game.virtual.delivery` |
| 135 | `alibaba.idle.game.boost.metadata.get` |
| 136 | `alibaba.idle.game.boost.auth.grant` |
| 137 | `alibaba.idle.game.boost.order.reason.get` |
| 138 | `alibaba.idle.game.boost.auth.get` |
| 139 | `alibaba.idle.game.boost.workbench.get` |
| 140 | `alibaba.idle.game.boost.club.online.update` |
| 141 | `alibaba.idle.game.boostclub.capacity.update` |
| 142 | `alibaba.idle.game.boost.order.query` |
| 143 | `alibaba.idle.game.boost.compensate.query` |
| 144 | `alibaba.idle.game.boost.refund.query` |
| 145 | `alibaba.idle.game.boost.club.boosttype.list` |
| 146 | `alibaba.idle.game.boost.refund.deal` |
| 147 | `alibaba.idle.game.boost.delay.apply` |
| 148 | `alibaba.idle.game.boost.compensate.deal` |
| 149 | `alibaba.idle.game.boost.order.remark.get` |
| 150 | `alibaba.idle.game.boost.order.remark.update` |
| 151 | `alibaba.idle.game.boost.club.tier.update` |
| 152 | `alibaba.idle.game.boost.order.cancel` |
| 153 | `alibaba.idle.game.boost.club.boosttype.submit` |
| 154 | `alibaba.idle.game.boost.order.perform` |
| 155 | `alibaba.idle.game.boost.club.boosttype.unsigned.list` |
| 156 | `alibaba.idle.game.boost.tier.list` |
| 157 | `alibaba.idle.open.game.auth.check` |

</details>

### 库存API

| # | API名称 |
|---|--------|
| 1 | `taobao.inventory.merchant.adjust` |
| 2 | `taobao.inventory.mode.query` |
| 3 | `taobao.shop.coverage.manage` |
| 4 | `taobao.shop.coverage.query` |
| 5 | `taobao.inventory.plan.front.precheck` |
| 6 | `taobao.inventory.plan.front.query` |
| 7 | `taobao.inventory.plan.front.operate` |
| 8 | `taobao.inventory.shopinv.adjust` |
| 9 | `taobao.inventory.shopinv.delete` |

### aliExpress

| # | API名称 |
|---|--------|
| 1 | `aliexpress.social.ins.directresult.update` |
| 2 | `aliexpress.feed.post.publish` |
| 3 | `aliexpress.logistics.abnormalorder.query` |

### 来疯API

| # | API名称 |
|---|--------|
| 1 | `taobao.laifeng.flagship.coins.buy` |
| 2 | `taobao.laifeng.flagship.coins.query` |
| 3 | `taobao.laifeng.flagship.order.query` |

### YunOS-广告

| # | API名称 |
|---|--------|
| 1 | `yunos.ad.audit.creative.getlist` |
| 2 | `yunos.ad.audit.creative.get` |
| 3 | `yunos.ad.audit.creative.add` |

### 司法开放平台 (30 APIs)

<details>
<summary>展开查看全部 30 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.legal.suit.case.get` |
| 2 | `alibaba.legal.suit.court.lawyer.push` |
| 3 | `alibaba.legal.suit.domination.push` |
| 4 | `alibaba.legal.suit.domination.get` |
| 5 | `alibaba.legal.suit.court.before.push` |
| 6 | `alibaba.legal.suit.court.entrust.get` |
| 7 | `alibaba.legal.suit.court.after.push` |
| 8 | `alibaba.legal.suit.judgement.get` |
| 9 | `alibaba.legal.suit.judgement.push` |
| 10 | `alibaba.legal.suit.court.open.push` |
| 11 | `alibaba.legal.suit.seal.push` |
| 12 | `alibaba.legal.suit.payment.push` |
| 13 | `alibaba.legal.standpoint.insertdraft` |
| 14 | `alibaba.legal.standpoint.delete` |
| 15 | `alibaba.standpoint.historykey.get` |
| 16 | `alibaba.legal.standpoint.getref` |
| 17 | `alibaba.legal.standpoint.query` |
| 18 | `alibaba.legal.stanpoint.accept` |
| 19 | `alibaba.legal.suit.courttime.push` |
| 20 | `alibaba.legal.newdraftstandpoint.query` |
| 21 | `alibaba.legal.standpoint.standpoint.collection` |
| 22 | `alibaba.legal.standpoint.derivestandpoint.query` |
| 23 | `alibaba.legal.standpoint.draftstandpoint.insert` |
| 24 | `alibaba.legal.standpoint.collectionstandpoint.query` |
| 25 | `alibaba.legal.standpoint.standpoint.query` |
| 26 | `alibaba.legal.standpoint.standpointtree.query` |
| 27 | `alibaba.legal.standpoint.scene.query` |
| 28 | `alibaba.legal.standpoint.standpoint.queryall` |
| 29 | `alibaba.legal.standpoint.query.versiontwo` |
| 30 | `alibaba.legal.suit.entrust.lawyer.push` |

</details>

### 全球速卖通

| # | API名称 |
|---|--------|
| 1 | `aliexpress.trade.order.open.check` |
| 2 | `aliexpress.trade.order.open.query` |
| 3 | `aliexpress.taxation.platform.open.get` |
| 4 | `aliexpress.taxation.calculate.open.query` |

### 阿里健康追溯码 (405 APIs)

<details>
<summary>展开查看全部 405 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.tracecodeplatform.code.active` |
| 2 | `alibaba.alihealth.tracecodeseller.code.active` |
| 3 | `alibaba.alihealth.tracecodeseller.bill.rootcode.get` |
| 4 | `alibaba.alihealth.drug.download.fileacceptret` |
| 5 | `alibaba.alihealth.drug.download.entlist` |
| 6 | `alibaba.alihealth.drug.getbarcode.bytraccode` |
| 7 | `alibaba.alihealth.drug.updatebarcode.bytraccode` |
| 8 | `alibaba.alihealth.drug.kyt.uploadb2cbill` |
| 9 | `alibaba.alihealth.drug.kyt.uploadcircubill` |
| 10 | `alibaba.alihealth.drug.kyt.searchstatus` |
| 11 | `alibaba.alihealth.drug.kyt.uploadretail` |
| 12 | `alibaba.alihealth.drug.kyt.getbyentid` |
| 13 | `alibaba.alihealth.drug.kyt.getbyrefentid` |
| 14 | `alibaba.alihealth.drug.kyt.listparts` |
| 15 | `alibaba.alihealth.drug.kyt.drugcodes` |
| 16 | `alibaba.alihealth.drug.kyt.synonymauths` |
| 17 | `alibaba.alihealth.drug.kyt.drugtable` |
| 18 | `alibaba.alihealth.drug.kyt.listauths` |
| 19 | `alibaba.alihealth.drug.kyt.listupout` |
| 20 | `alibaba.alihealth.drug.kyt.uploadrelation` |
| 21 | `alibaba.alihealth.drug.kyt.uploadinoutbill` |
| 22 | `alibaba.alihealth.drug.kyt.getcodebillinfo` |
| 23 | `alibaba.alihealth.drug.kyt.singlerelation` |
| 24 | `alibaba.alihealth.drug.kyt.relationdetail` |
| 25 | `alibaba.alihealth.drug.kyt.codeprocess` |
| 26 | `alibaba.alihealth.drug.kyt.upinoutfile` |
| 27 | `alibaba.alihealth.drug.kyt.upstorebillfile` |
| 28 | `alibaba.alihealth.drug.kyt.drugdetail` |
| 29 | `alibaba.alihealth.drug.code.common.list.codeinfo` |
| 30 | `alibaba.alihealth.drug.kyt.getcodebaseinfo` |
| 31 | `alibaba.alihealth.drug.kyt.querydruginfo` |
| 32 | `alibaba.alihealth.drug.kyt.recordinfo` |
| 33 | `alibaba.alihealth.trace.code.search.get.drugresourcetop` |
| 34 | `alibaba.alihealth.drug.kyt.filedownload` |
| 35 | `alibaba.alihealth.drug.kyt.updatebillinfo` |
| 36 | `alibaba.alihealth.drug.kyt.updatebillcode` |
| 37 | `alibaba.alihealth.drug.kyt.storebilldelete` |
| 38 | `alibaba.alihealth.drug.kyt.storebilllist` |
| 39 | `alibaba.alihealth.drug.code.advance.bill.flow.direction` |
| 40 | `alibaba.alihealth.drug.bill.upbill.detail.withcode` |
| 41 | `alibaba.alihealth.drug.kyt.codetobill` |
| 42 | `alibaba.alihealth.drug.kyt.uploadinsign` |
| 43 | `alibaba.alihealth.drug.code.code.check.hospital` |
| 44 | `alibaba.alihealth.drug.code.list.code.alkali` |
| 45 | `alibaba.alihealth.drug.code.list.code.medical.insurance` |
| 46 | `alibaba.alihealth.drug.code.code.check.medical.insurance` |
| 47 | `alibaba.alihealth.drug.kyt.getentinfo` |
| 48 | `alibaba.alihealth.drug.kyt.idgenerate` |
| 49 | `alibaba.alihealth.tracecodeseller.product.attr.search` |
| 50 | `alibaba.alihealth.drug.code.list.code.supervise` |
| 51 | `alibaba.alihealth.tracecodeseller.milk.trace.tosource.add.data` |
| 52 | `alibaba.alihealth.drug.kyt.searchbill` |
| 53 | `alibaba.alihealth.drug.kyt.druploadretail` |
| 54 | `alibaba.alihealth.drug.kyt.query.druginfo.from.billcode` |
| 55 | `alibaba.alihealth.drug.kyt.query.code.relation.from.billcode` |
| 56 | `alibaba.alihealth.drug.kyt.dr.singlerelation` |
| 57 | `alibaba.alihealth.drug.kyt.querycodeactive` |
| 58 | `alibaba.alihealth.drug.kyt.dr.uploadinoutbill` |
| 59 | `alibaba.alihealth.drug.kyt.dr.searchstatus` |
| 60 | `alibaba.alihealth.drug.kyt.dr.getbyentid` |
| 61 | `alibaba.alihealth.drug.kyt.dr.getbyrefentid` |
| 62 | `alibaba.alihealth.drug.kyt.dr.getentinfo` |
| 63 | `alibaba.alihealth.drug.kyt.dr.listparts` |
| 64 | `alibaba.alihealth.drug.code.kyt.dr.querycode` |
| 65 | `alibaba.alihealth.drug.code.kyt.querycode` |
| 66 | `alibaba.alihealth.drug.kyt.dr.billcheck` |
| 67 | `alibaba.alihealth.drug.kyt.dr.drugrecal` |
| 68 | `alibaba.alihealth.drug.kyt.dr.getproteminfo` |
| 69 | `alibaba.alihealth.drug.kyt.dr.transportupload` |
| 70 | `alibaba.alihealth.drug.kyt.dr.storageupload` |
| 71 | `alibaba.alihealth.drug.kyt.dr.associateequi` |
| 72 | `alibaba.alihealth.drug.kyt.getentlicense` |
| 73 | `alibaba.alihealth.drug.kyt.getdruglicense` |
| 74 | `alibaba.alihealth.tracecodesearc.getinfomation.vivo` |
| 75 | `alibaba.alihealth.drug.kyt.listparts.byagent` |
| 76 | `alibaba.alihealth.drug.code.kyt.yy.querycode` |
| 77 | `alibaba.alihealth.drug.kyt.yy.querysubcodes` |
| 78 | `alibaba.alihealth.drug.kyt.queryactivetime` |
| 79 | `alibaba.alihealth.drug.kyt.querybatchprod` |
| 80 | `alibaba.alihealth.drug.kyt.yb.getcoderelation` |
| 81 | `alibaba.alihealth.drug.kyt.dr.queryupbillcode` |
| 82 | `alibaba.alihealth.drug.kyt.yy.uploadretail` |
| 83 | `alibaba.alihealth.drug.kyt.yy.drugcodes` |
| 84 | `alibaba.alihealth.drug.kyt.yy.uploadinoutbill` |
| 85 | `alibaba.cfda.xtpt.app.accept.info` |
| 86 | `alibaba.alihealth.drug.kyt.dr.getupteminfo` |
| 87 | `alibaba.alihealth.drug.kyt.dr.vaequipment.list` |
| 88 | `alibaba.alihealth.drug.code.kyt.yd.querycode` |
| 89 | `alibaba.alihealth.drug.code.kyt.yy.applycode` |
| 90 | `alibaba.alihealth.drug.code.kyt.yq.querycode` |
| 91 | `alibaba.alihealth.drug.kyt.va.uploadretail` |
| 92 | `alibaba.alihealth.drug.code.kyt.va.querycode` |
| 93 | `alibaba.alihealth.drug.kyt.yy.listparts` |
| 94 | `alibaba.alihealth.drug.kyt.smyx.getentinfo` |
| 95 | `alibaba.alihealth.drug.code.kyt.smyx.querycode` |
| 96 | `alibaba.alihealth.drug.kyt.smyx.uploadinoutbill` |
| 97 | `alibaba.alihealth.drug.kyt.drugrescode` |
| 98 | `alibaba.alihealth.drugcode.applycert` |
| 99 | `alibaba.alihealth.drugcode.drugfactory.getencrptypk` |
| 100 | `alibaba.alihealth.drugcode.drugfactory.exportcategory` |
| 101 | `alibaba.alihealth.drug.kyt.destbill.check` |
| 102 | `alibaba.alihealth.drug.kyt.destbill.list` |
| 103 | `alibaba.alihealth.drugcode.drugfactory.getblindresult` |
| 104 | `alibaba.alihealth.drugcode.center.receive.bound.status` |
| 105 | `alibaba.alihealth.drug.kyt.smyx.listparts` |
| 106 | `alibaba.alihealth.drugtrace.top.yljg.uploadretail` |
| 107 | `alibaba.alihealth.drugtrace.top.lsyd.uploadretail` |
| 108 | `alibaba.alihealth.drugtrace.top.lsyd.uploadinoutbill` |
| 109 | `alibaba.alihealth.drugtrace.top.yljg.uploadinoutbill` |
| 110 | `alibaba.alihealth.drugtrace.top.lsyd.query.billstatus` |
| 111 | `alibaba.alihealth.drugtrace.top.yljg.query.billstatus` |
| 112 | `alibaba.alihealth.drugtrace.top.yljg.query.upbillcode` |
| 113 | `alibaba.alihealth.drugtrace.top.lsyd.query.upbillcode` |
| 114 | `alibaba.alihealth.drugtrace.top.lsyd.query.upbilldetail` |
| 115 | `alibaba.alihealth.drugtrace.top.yljg.query.upbilldetail` |
| 116 | `alibaba.alihealth.drugtrace.top.lsyd.query.relation` |
| 117 | `alibaba.alihealth.drugtrace.top.yljg.query.relation` |
| 118 | `alibaba.alihealth.drugtrace.top.yljg.query.getentinfo` |
| 119 | `alibaba.alihealth.drugtrace.top.lsyd.query.codedetail` |
| 120 | `alibaba.alihealth.drugtrace.top.yljg.query.codedetail` |
| 121 | `alibaba.alihealth.drugtrace.top.lsyd.query.getentinfo` |
| 122 | `alibaba.alihealth.drug.upload.extinfo` |
| 123 | `alibaba.alihealth.drugtrace.top.yljg.listupout` |
| 124 | `alibaba.alihealth.drugtrace.top.lsyd.listupout` |
| 125 | `alibaba.alihealth.zy.uploadrelation` |
| 126 | `alibaba.alihealth.drugcode.user.data` |
| 127 | `alibaba.alihealth.drugtrace.top.yljg.listupout.detail` |
| 128 | `alibaba.alihealth.drugtrace.top.lsyd.listupout.detail` |
| 129 | `alibaba.alihealth.drug.kyt.remnantbill.upload` |
| 130 | `alibaba.alihealth.drugtrace.top.lsyd.query.listparts` |
| 131 | `alibaba.alihealth.drugtrace.top.yljg.query.listparts` |
| 132 | `alibaba.alihealth.drug.kyt.saveent` |
| 133 | `alibaba.alihealth.drug.lsyd.saveent` |
| 134 | `alibaba.alihealth.drug.code.kyt.querycodeflow` |
| 135 | `alibaba.alihealth.drug.code.error.report` |
| 136 | `alibaba.alihealth.secondard.node.code.showurl` |
| 137 | `alibaba.alihealth.drugcode.listentparbyrefentid` |
| 138 | `alibaba.alihealth.drug.download.getproductxml` |
| 139 | `alibaba.alihealth.drug.kyt.query.upbillcode` |
| 140 | `alibaba.alihealth.drugtrace.top.lsyd.query.getbyrefentid` |
| 141 | `alibaba.alihealth.drugtrace.top.yljg.query.getbyrefentid` |
| 142 | `alibaba.alihealth.drug.kyt.searchbill.detail` |
| 143 | `alibaba.alihealth.drug.kyt.specia.vaccin.uploadretail` |
| 144 | `alibaba.alihealth.drug.code.kyt.specia.vaccin.querycode` |
| 145 | `alibaba.alihealth.drug.kyt.specia.vaccin.getentinfo` |
| 146 | `alibaba.alihealth.drug.kyt.query.specia.vaccin.billcode` |
| 147 | `alibaba.alihealth.drug.kyt.specia.vaccin.getbyrefentid` |
| 148 | `alibaba.alihealth.drug.kyt.getdruginfo.downloadurl` |
| 149 | `alibaba.alihealth.drug.code.list.code.gov` |
| 150 | `alibaba.alihealth.drug.kyt.codereplacelog` |
| 151 | `alibaba.alihealth.drug.kyt.codereplace` |
| 152 | `alibaba.alihealth.drug.download.getentdailytaskdtolist` |
| 153 | `alibaba.alihealth.drug.kyt.scqy.delbillinfo` |
| 154 | `alibaba.alihealth.drug.kyt.scqy.codeprocess` |
| 155 | `alibaba.alihealth.drug.kyt.scqy.uploadrelation` |
| 156 | `alibaba.alihealth.drug.kyt.scqy.singlerelation` |
| 157 | `alibaba.alihealth.drug.kyt.scqy.uploadcircubill` |
| 158 | `alibaba.alihealth.drug.kyt.scqy.putpackage` |
| 159 | `alibaba.alihealth.drug.download.dataerrordiagnosis` |
| 160 | `alibaba.alihealth.code.getcodeinfo` |
| 161 | `alibaba.alihealth.drugtrace.top.yljg.drugtable` |
| 162 | `alibaba.alihealth.drug.code.kyt.hospitalsenddrugmachine` |
| 163 | `alibaba.alihealth.drug.code.kyt.wes.querycode` |
| 164 | `alibaba.alihealth.drug.code.kyt.wes.getlicense` |
| 165 | `alibaba.alihealth.drug.code.kyt.wes.checkcoderelation` |
| 166 | `alibaba.alihealth.drug.kyt.wes.searchbill.detail` |
| 167 | `alibaba.alihealth.drug.kyt.wes.listupout` |
| 168 | `alibaba.alihealth.drug.kyt.scqy.putpackageunbind` |
| 169 | `alibaba.alihealth.drug.kyt.scqy.putpackagebind` |
| 170 | `alibaba.alihealth.drug.code.kyt.wes.querycoderelation` |
| 171 | `alibaba.alihealth.drug.kyt.wes.uploadcircubill` |
| 172 | `alibaba.alihealth.drug.kyt.wes.synonymauths` |
| 173 | `alibaba.alihealth.drug.kyt.wes.listparts` |
| 174 | `alibaba.alihealth.drug.kyt.wes.uploadinoutbill` |
| 175 | `alibaba.alihealth.drug.kyt.wes.upbill.detailwithcode` |
| 176 | `alibaba.alihealth.drug.kyt.wes.searchstatus` |
| 177 | `alibaba.alihealth.drug.kyt.wes.drugrescode` |
| 178 | `alibaba.alihealth.drug.kyt.wes.searchbill` |
| 179 | `alibaba.alihealth.drug.kyt.wes.getbyentid` |
| 180 | `alibaba.alihealth.drug.kyt.wes.getbyrefentid` |
| 181 | `alibaba.alihealth.drug.kyt.wes.getentinfo` |
| 182 | `alibaba.alihealth.drug.kyt.getkeyflagdruginfo.downloadurl` |
| 183 | `alibaba.alihealth.drug.kyt.service.getenddate` |
| 184 | `alibaba.alihealth.drugtrace.top.yljg.service.getenddate` |
| 185 | `alibaba.alihealth.drugtrace.top.lsyd.service.getenddate` |
| 186 | `alibaba.alihealth.drugtrace.top.lsyd.getkeyflagdruginfo.downloadurl` |
| 187 | `alibaba.alihealth.drugtrace.top.yljg.getkeyflagdruginfo.downloadurl` |
| 188 | `alibaba.alihealth.drug.kyt.wes.getdruginfo.downloadurl` |
| 189 | `alibaba.alihealth.drug.kyt.wes.listparts.byagent` |
| 190 | `alibaba.alihealth.drug.kyt.wes.query.upbillcode` |
| 191 | `alibaba.alihealth.drug.kyt.wes.saveent` |
| 192 | `alibaba.alihealth.drug.kyt.wes.querycodeactive` |
| 193 | `alibaba.alihealth.drug.kyt.wes.remnantbill.upload` |
| 194 | `alibaba.alihealth.drugcheckcode.checklastfour` |
| 195 | `alibaba.alihealth.drug.kyt.scqy.listcodefullinfodtomedicaldevice` |
| 196 | `alibaba.alihealth.drugtrace.top.bill.query.billdetail` |
| 197 | `alibaba.alihealth.drugtrace.top.code.query.relation` |
| 198 | `alibaba.alihealth.drug.msc.uploadcircubill` |
| 199 | `alibaba.alihealth.drug.down.listupout` |
| 200 | `alibaba.alihealth.drug.down.queryupoutbilllog` |
| 201 | `alibaba.alihealth.drug.msc.searchbill` |
| 202 | `alibaba.alihealth.drug.msc.searchbill.detail` |
| 203 | `alibaba.alihealth.drug.msc.remnantbill.upload` |
| 204 | `alibaba.alihealth.drug.msc.bill.searchstatus` |
| 205 | `alibaba.alihealth.drug.msc.getentinfo` |
| 206 | `alibaba.alihealth.drug.msc.listparts` |
| 207 | `alibaba.alihealth.drug.msc.synonymauths` |
| 208 | `alibaba.alihealth.drug.msc.getbyrefentid` |
| 209 | `alibaba.alihealth.drug.msc.getbyentid` |
| 210 | `alibaba.alihealth.drug.down.querycoderelation` |
| 211 | `alibaba.alihealth.drug.down.upbill.detailwithcode` |
| 212 | `alibaba.alihealth.drug.msc.drugtable` |
| 213 | `alibaba.alihealth.drug.code.kyt.wes.querycodebillinfo` |
| 214 | `alibaba.alihealth.drugtrace.top.alipay.query.codedetail` |
| 215 | `alibaba.alihealth.drug.code.codequery.codeflowquerymedicalfacility` |
| 216 | `alibaba.alihealth.drug.code.kyt.zfquerycodeflow` |
| 217 | `alibaba.alihealth.drug.msc.uploadinoutbill` |
| 218 | `alibaba.alihealth.drugtrace.top.zdsm.uploadinoutbill` |
| 219 | `alibaba.alihealth.drugtrace.top.zdsm.query.codedetail` |
| 220 | `alibaba.alihealth.drugtrace.top.zdsm.query.listparts` |
| 221 | `alibaba.alihealth.drugtrace.top.zdsm.query.getbyrefentid` |
| 222 | `alibaba.alihealth.drugtrace.top.zdsm.query.billstatus` |
| 223 | `alibaba.alihealth.drugtrace.top.zdsm.uploadretail` |
| 224 | `alibaba.alihealth.drug.code.codequery.codeflowquerywithisv` |
| 225 | `alibaba.alihealth.drugtrace.top.zdsm.listupout` |
| 226 | `alibaba.alihealth.drugtrace.top.zdsm.listupout.detail` |
| 227 | `alibaba.alihealth.drug.code.codequery.querychildrencodewithisv` |
| 228 | `alibaba.alihealth.drug.code.codequery.querybarcodebycode` |
| 229 | `alibaba.alihealth.drugtrace.top.lsyd.querycodeactive` |
| 230 | `alibaba.alihealth.drug.code.codequery.addbarcodeinfo` |
| 231 | `alibaba.alihealth.drugtrace.top.bill.query.listreturninbills` |
| 232 | `alibaba.alihealth.drug.kyt.wes.getbyorgcode` |
| 233 | `alibaba.alihealth.drug.kyt.wes.queryupoutbilllog` |
| 234 | `alibaba.alihealth.synergy.yzw.savedrugreportwithocr` |
| 235 | `alibaba.alihealth.synergy.yzw.querysealdrugreport` |
| 236 | `alibaba.alihealth.synergy.yzw.drugreport.seal` |
| 237 | `alibaba.alihealth.synergy.yzw.querydrugreport` |
| 238 | `alibaba.alihealth.synergy.yzw.drugreport.get` |
| 239 | `alibaba.alihealth.synergy.yzw.drugreport.opt` |
| 240 | `alibaba.alihealth.drugtrace.top.zfkb.prodkeydruglist` |
| 241 | `alibaba.alihealth.synergy.yzw.getdrugreportwithocrstatus` |
| 242 | `alibaba.alihealth.drugtrace.top.zfkb.prodtracesituationlist` |
| 243 | `alibaba.alihealth.synergy.yzw.getdrugreportwithhttpstatus` |
| 244 | `alibaba.alihealth.drugtrace.top.zfkb.prodtracesituationdetaillist` |
| 245 | `alibaba.alihealth.drugtrace.top.zfkb.managekeydruglist` |
| 246 | `alibaba.alihealth.drugtrace.top.zfkb.managekeydrugsummarylist` |
| 247 | `alibaba.alihealth.drugtrace.top.zfkb.medicalkeydruglist` |
| 248 | `alibaba.alihealth.drugtrace.top.zfkb.medicalkeydrugdetaillist` |
| 249 | `alibaba.alihealth.synergy.yzw.querydrugbatchreport` |
| 250 | `alibaba.alihealth.synergy.yzw.deletedrugreport` |
| 251 | `alibaba.alihealth.synergy.yzw.signednotstampedbill.query` |
| 252 | `alibaba.alihealth.drug.msc.billin.detailwithcode` |
| 253 | `alibaba.alihealth.synergy.yzw.drugreport.opt.history.all` |
| 254 | `alibaba.alihealth.synergy.yzw.bill.signed.query` |
| 255 | `alibaba.alihealth.drug.myj.codewarn.codewarninglist` |
| 256 | `alibaba.alihealth.drug.myj.codewarn.codewarninginfodetaillist` |
| 257 | `alibaba.alihealth.drug.myj.codewarn.createcodewarntask` |
| 258 | `alibaba.alihealth.synergy.yzw.querydrugreportass` |
| 259 | `alibaba.alihealth.synergy.yzw.drugreport.opt.byagent` |
| 260 | `alibaba.alihealth.drug.query.ent.auth.progress` |
| 261 | `alibaba.alihealth.synergy.yzw.queryreportbycode` |
| 262 | `alibaba.alihealth.synergy.yzw.druginfo.query` |
| 263 | `alibaba.alihealth.synergy.yzw.drugreport.byfile.save` |
| 264 | `alibaba.alihealth.synergy.yzw.drugreport.ass.seal` |
| 265 | `alibaba.alihealth.synergy.yzw.queryassdrugreportinfo` |
| 266 | `alibaba.alihealth.drug.code.kyt.wes.delbillinfo` |
| 267 | `alibaba.alihealth.drug.yzw.drugtable` |
| 268 | `alibaba.alihealth.drug.msc.billout.detailwithcodes` |
| 269 | `alibaba.alihealth.synergy.yzw.drugreport.byfile.save.self` |
| 270 | `alibaba.alihealth.drug.scc.uploadsccbillinfo` |
| 271 | `alibaba.alihealth.drug.scc.material.upload` |
| 272 | `alibaba.alihealth.drug.scc.material.send` |
| 273 | `alibaba.alihealth.drug.scc.bill.search` |
| 274 | `alibaba.alihealth.drug.yljg.getentinfonew` |
| 275 | `alibaba.alihealth.drug.msc.getentinfonew` |
| 276 | `alibaba.alihealth.drug.kytsole.getentinfonew` |
| 277 | `alibaba.alihealth.drug.lsyd.getentinfonew` |
| 278 | `alibaba.alihealth.drug.wes.getentinfonew` |
| 279 | `alibaba.alihealth.drug.scc.bill.detail` |
| 280 | `alibaba.alihealth.drug.scc.uploadscctransportorderinfo` |
| 281 | `alibaba.alihealth.drug.scc.bill.detail.material` |
| 282 | `alibaba.alihealth.drug.scc.bill.search.up` |
| 283 | `alibaba.alihealth.synergy.sy.qualification.list` |
| 284 | `alibaba.alihealth.synergy.sy.ent.resource.save` |
| 285 | `alibaba.alihealth.synergy.sy.product.resource.save` |
| 286 | `alibaba.alihealth.synergy.sy.product.save` |
| 287 | `alibaba.alihealth.synergy.sy.resource.result` |
| 288 | `alibaba.alihealth.synergy.sy.agentperson.save` |
| 289 | `alibaba.alihealth.synergy.sy.product.resource.list` |
| 290 | `alibaba.alihealth.synergy.sy.agentperson.query` |
| 291 | `alibaba.alihealth.synergy.sy.agentperson.resource.list` |
| 292 | `alibaba.alihealth.synergy.sy.agentperson.resource.save` |
| 293 | `alibaba.alihealth.synergy.sy.ent.resource.list` |
| 294 | `alibaba.alihealth.synergy.sy.product.list` |
| 295 | `alibaba.alihealth.drug.scc.material.sign` |
| 296 | `alibaba.alihealth.synergy.scc.qualification.list` |
| 297 | `alibaba.alihealth.drug.scc.material.upload.result` |
| 298 | `alibaba.alihealth.drug.scc.bill.assrefuserid.search` |
| 299 | `alibaba.alihealth.drug.scc.bill.search.assrefuserid.bill` |
| 300 | `alibaba.alihealth.drug.scc.bill.search.up.bytoassrefuserid` |
| 301 | `alibaba.alihealth.drug.scc.queryscctransportorderlist` |
| 302 | `alibaba.alihealth.drug.scc.queryscctransportorderdetail` |
| 303 | `alibaba.alihealth.synergy.scsy.savematerial` |
| 304 | `alibaba.alihealth.synergy.sy.createrequest` |
| 305 | `alibaba.alihealth.synergy.sy.listreceiverequest` |
| 306 | `alibaba.alihealth.drug.code.scc.query.upbillcode` |
| 307 | `alibaba.alihealth.drug.code.scc.checkcoderelation` |
| 308 | `alibaba.alihealth.drug.code.scc.querycode` |
| 309 | `alibaba.alihealth.drug.code.scc.querycoderelation` |
| 310 | `alibaba.alihealth.drug.code.scc.querycodeactive` |
| 311 | `alibaba.alihealth.drug.yljg.saveent` |
| 312 | `alibaba.alihealth.drug.msc.saveent` |
| 313 | `alibaba.alihealth.drug.scc.listparts` |
| 314 | `alibaba.alihealth.drug.scc.ent.getbyentid` |
| 315 | `alibaba.alihealth.drug.scc.ent.getentinfonew` |
| 316 | `alibaba.alihealth.drug.scc.ent.getbyrefentid` |
| 317 | `alibaba.alihealth.drug.scc.ent.saveent` |
| 318 | `alibaba.alihealth.drug.scc.getlicense` |
| 319 | `alibaba.alihealth.drug.scc.bill.rejection` |
| 320 | `alibaba.alihealth.synergy.sy.signature.create` |
| 321 | `alibaba.alihealth.synergy.sy.signature.detail.get` |
| 322 | `alibaba.alihealth.synergy.sy.signature.resource.seal` |
| 323 | `alibaba.alihealth.synergy.sy.resource.opt.archive` |
| 324 | `alibaba.alihealth.synergy.sy.inbox.list` |
| 325 | `alibaba.alihealth.synergy.sy.inbox.check` |
| 326 | `alibaba.alihealth.synergy.sy.inbox.detail` |
| 327 | `alibaba.alihealth.drug.kyt.wes.billpartialreject` |
| 328 | `alibaba.alihealth.drug.kyt.dr.vaequipment.save` |
| 329 | `alibaba.alihealth.drug.kyt.dr.vaequipment.update` |
| 330 | `alibaba.alihealth.drug.scc.material.reject` |
| 331 | `alibaba.alihealth.drug.myj.codewarn.getwarninfo` |
| 332 | `alibaba.alihealth.drug.msc.listbillprocesspartsuccess` |
| 333 | `alibaba.alihealth.drug.kyt.wes.listbillprocesspartsuccess` |
| 334 | `alibaba.alihealth.drugtrace.top.yljg.listbillprocesspartsuccess` |
| 335 | `alibaba.alihealth.drugtrace.top.lsyd.listbillprocesspartsuccess` |
| 336 | `alibaba.alihealth.drug.kyt.listbillprocesspartsuccess` |
| 337 | `alibaba.alihealth.drug.scc.uploadsccretailbillinfo` |
| 338 | `alibaba.alihealth.synergy.sy.refuserequest` |
| 339 | `alibaba.alihealth.synergy.sy.outbox.detail` |
| 340 | `alibaba.alihealth.synergy.sy.outbox.list` |
| 341 | `alibaba.alihealth.drug.kyt.dr.billininfobycodes` |
| 342 | `alibaba.alihealth.drug.code.djgl.delbillinfo` |
| 343 | `alibaba.alihealth.synergy.sy.outbox.withdraw` |
| 344 | `alibaba.alihealth.synergy.syht.resource.send` |
| 345 | `alibaba.alihealth.synergy.syht.resource.send.result` |
| 346 | `alibaba.alihealth.drug.wes.getentinfolist` |
| 347 | `alibaba.alihealth.drug.vaccine.getentinfolist` |
| 348 | `alibaba.alihealth.drug.lsyd.getentinfolist` |
| 349 | `alibaba.alihealth.drug.kytsole.getentinfolist` |
| 350 | `alibaba.alihealth.drug.yljg.getentinfolist` |
| 351 | `alibaba.alihealth.drug.msc.getentinfolist` |
| 352 | `alibaba.alihealth.drug.scc.ent.getentinfolist` |
| 353 | `alibaba.alihealth.drug.sy.getentinfolist` |
| 354 | `alibaba.alihealth.drug.zdsm.getentinfolist` |
| 355 | `alibaba.alihealth.drug.vaccine.onesub.getentinfolist` |
| 356 | `alibaba.alihealth.drug.kyt.smyx.getentinfolist` |
| 357 | `alibaba.alihealth.synergy.sy.receiverequest.detail` |
| 358 | `alibaba.alihealth.synergy.sy.contract.list` |
| 359 | `alibaba.alihealth.ent.yzw.auth.getdruginfo` |
| 360 | `alibaba.alihealth.synergy.sy.contract.detail` |
| 361 | `alibaba.alihealth.synergy.sy.contract.revoke` |
| 362 | `alibaba.alihealth.drug.scc.bill.detail.codes` |
| 363 | `alibaba.alihealth.synergy.sy.contract.create` |
| 364 | `alibaba.alihealth.drug.scc.license.token.get` |
| 365 | `alibaba.alihealth.drug.code.kyt.wes.license.token.get` |
| 366 | `alibaba.alihealth.synergy.sy.contract.refuse` |
| 367 | `alibaba.alihealth.synergy.sy.contract.seal` |
| 368 | `alibaba.alihealth.drug.scc.bill.disref.search` |
| 369 | `alibaba.alihealth.synergy.sy.listrequestdetail` |
| 370 | `alibaba.alihealth.synergy.sy.listrequest` |
| 371 | `alibaba.alihealth.drug.kyt.dr.updatebilltime` |
| 372 | `alibaba.alihealth.drug.lsyd.searchbill` |
| 373 | `alibaba.alihealth.drug.yljg.searchbill` |
| 374 | `alibaba.alihealth.drug.kyt.scc.synonymauths` |
| 375 | `alibaba.alihealth.synergy.sy.entpartner.page` |
| 376 | `alibaba.alihealth.synergy.sy.entpartner.resource.list` |
| 377 | `alibaba.alihealth.drug.msc.query.upoutbillcount` |
| 378 | `alibaba.alihealth.drug.msc.query.billcount` |
| 379 | `alibaba.alihealth.synergy.yzw.getentinfolist` |
| 380 | `alibaba.alihealth.drug.scc.query.billcount` |
| 381 | `alibaba.alihealth.drug.scc.query.upoutbillcount` |
| 382 | `alibaba.alihealth.drug.wes.query.billcount` |
| 383 | `alibaba.alihealth.drug.wes.query.upoutbillcount` |
| 384 | `alibaba.alihealth.drug.lsyd.query.billcount` |
| 385 | `alibaba.alihealth.drug.yljg.query.billcount` |
| 386 | `alibaba.alihealth.drug.yljg.query.upoutbillcount` |
| 387 | `alibaba.alihealth.drug.lsyd.query.upoutbillcount` |
| 388 | `alibaba.alihealth.synergy.sy.partneragentperson.query` |
| 389 | `alibaba.alihealth.synergy.yzw.drugreport.byfile.save.scc` |
| 390 | `alibaba.alihealth.drug.msc.listauths` |
| 391 | `alibaba.alihealth.drug.scc.listauths` |
| 392 | `alibaba.alihealth.drug.wes.listauths` |
| 393 | `alibaba.alihealth.drug.kyt.sole.listauths` |
| 394 | `alibaba.alihealth.drug.code.kyt.wes.checkcoderelationall` |
| 395 | `alibaba.alihealth.drug.kyt.dr.storagequery` |
| 396 | `alibaba.alihealth.drug.code.kyt.scc.querycodebillinfo` |
| 397 | `alibaba.alihealth.drug.kyt.dr.transportquery` |
| 398 | `alibaba.alihealth.drug.download.provacceptret` |
| 399 | `alibaba.alihealth.drug.lsyd.searchbill.detail` |
| 400 | `alibaba.alihealth.drug.yljg.searchbill.detail` |
| 401 | `alibaba.alihealth.drug.scc.listparts.byagent` |
| 402 | `alibaba.alihealth.drug.kyt.wes.retail.searchbill` |
| 403 | `alibaba.alihealth.drug.msc.retail.searchbill` |
| 404 | `alibaba.alihealth.drug.lsyd.retail.searchbill` |
| 405 | `alibaba.alihealth.drug.yljg.retail.searchbill` |

</details>

### 会员中心API

| # | API名称 |
|---|--------|
| 1 | `alibaba.interact.vip.get` |
| 2 | `taobao.vipshop.blackvip.content.publish` |

### 阿里健康-会员管理

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.pregnancy.data.sync` |
| 2 | `alibaba.alihealth.pregnancy.product.get` |
| 3 | `alibaba.alihealth.pregnancy.navigateinfo.query` |
| 4 | `alibaba.fmhealth.weight.lossplan.synclossplan` |
| 5 | `alibaba.fmhealth.butler.energy.sync` |
| 6 | `alibaba.alihealth.uic.userinfo.healthid.get` |
| 7 | `alibaba.alihealth.medicalbase.hospital.sync` |
| 8 | `alibaba.alihealth.baby.baseinfo.order.sync` |
| 9 | `alibaba.alihealth.baby.remind.batch.send` |
| 10 | `alibaba.alihealth.alipaypfm.diet.record` |
| 11 | `alibaba.alihealth.alipaypfm.order.sync` |

### 店小蜜API

| # | API名称 |
|---|--------|
| 1 | `taobao.alimi.workorder.permission.notify` |
| 2 | `taobao.alimi.workorder.progress.notify` |

### 品效API

| # | API名称 |
|---|--------|
| 1 | `taobao.brand.startshop.rpt.adgroup.get` |
| 2 | `taobao.brandhub.specialshow.rpt.adgroup.get` |

### 小蜜API

| # | API名称 |
|---|--------|
| 1 | `taobao.alime.user.token.get` |
| 2 | `taobao.alime.user.token.advance.get` |

### 阿里供应链中台API

| # | API名称 |
|---|--------|
| 1 | `alibaba.dchain.ascp.call.upload` |
| 2 | `alibaba.dchain.ascp.text.upload` |

### 大麦票务云分销API (30 APIs)

<details>
<summary>展开查看全部 30 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.damai.maitix.order.query` |
| 2 | `alibaba.damai.maitix.order.confirm` |
| 3 | `alibaba.damai.maitix.order.cancel` |
| 4 | `alibaba.damai.maitix.order.directrefund` |
| 5 | `alibaba.damai.maitix.order.distribution.create` |
| 6 | `alibaba.damai.maitix.project.distribution.query` |
| 7 | `alibaba.damai.maitix.project.distribution.querylist` |
| 8 | `alibaba.damai.maitix.eticket.distribution.query` |
| 9 | `alibaba.damai.maitix.project.distribution.querybypage` |
| 10 | `alibaba.damai.maitix.project.distribution.detail.query` |
| 11 | `alibaba.damai.maitix.opengateway.project.status.query` |
| 12 | `alibaba.damai.maitix.opengateway.ticketItem.status.query` |
| 13 | `alibaba.damai.maitix.opengateway.perform.status.query` |
| 14 | `alibaba.damai.maitix.seat.info.query` |
| 15 | `alibaba.damai.maitix.seat.token.query` |
| 16 | `alibaba.damai.maitix.distribution.delivery.calculate` |
| 17 | `alibaba.damai.maitix.distribution.delivery.query` |
| 18 | `alibaba.damai.maitix.distribution.exchangepoint.query` |
| 19 | `alibaba.damai.maitix.distribution.cmb.paramencrypt` |
| 20 | `alibaba.damai.maitix.distribution.cmb.querypayresult` |
| 21 | `alibaba.damai.maitix.distribution.refund.submit` |
| 22 | `alibaba.damai.maitix.sponsor.distribution.queryreserveseats` |
| 23 | `alibaba.damai.maitix.sponsor.distribution.countreserveseats` |
| 24 | `alibaba.damai.maitix.sponsor.distribution.asynccreateorder` |
| 25 | `alibaba.damai.maitix.sponsor.distribution.getcreatingorderstatus` |
| 26 | `alibaba.damai.maitix.sponsor.distribution.listpricebyperformid` |
| 27 | `alibaba.damai.maitix.sponsor.distribution.submitrefundaudit` |
| 28 | `alibaba.damai.maitix.sponsor.distribution.agreerefundaudit` |
| 29 | `alibaba.damai.maitix.sponsor.distribution.refuserefundaudit` |
| 30 | `alibaba.damai.maitix.distribution.refund.refundamountdetail` |

</details>

### 淘票票数据平台

| # | API名称 |
|---|--------|
| 1 | `taobao.film.open.show.nowandsoon.get` |
| 2 | `taobao.film.open.show.nowandsoon.get.vii` |
| 3 | `taobao.film.open.show.nowandsoon.yidong.get.vii` |

### 天猫精灵开放API (56 APIs)

<details>
<summary>展开查看全部 56 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.tmallgenie.hotelplayerpause` |
| 2 | `taobao.tmallgenie.hotelwelcome` |
| 3 | `alibaba.ailabs.aligenie.opencontent.push` |
| 4 | `taobao.ailab.aicloud.top.message.sendaudio` |
| 5 | `alibaba.ailabs.bots.skils.list` |
| 6 | `alibaba.ai.user.quick.register` |
| 7 | `alibaba.ai.user.quick.bind` |
| 8 | `taobao.ailab.aicloud.top.memo.alarm.list` |
| 9 | `taobao.ailab.aicloud.top.memo.alarm.delete` |
| 10 | `taobao.ailab.aicloud.top.memo.meeting.list` |
| 11 | `taobao.ailab.aicloud.top.memo.meeting.delete` |
| 12 | `taobao.ailab.aicloud.top.memo.note.list` |
| 13 | `taobao.ailab.aicloud.top.memo.note.delete` |
| 14 | `taobao.ailab.aicloud.top.message.sendtext` |
| 15 | `taobao.ailab.aicloud.top.music.search` |
| 16 | `alibaba.ai.user.quick.token.bind` |
| 17 | `alibaba.ailabs.aligenie.device.register` |
| 18 | `taobao.ailab.aicloud.top.skils.list` |
| 19 | `taobao.ailab.aicloud.top.memo.alarm.create` |
| 20 | `alibaba.ailabs.iot.device.list.get` |
| 21 | `taobao.ailab.aicloud.top.earthquake.send` |
| 22 | `alibaba.ailabs.aligenie.videoalbum.push` |
| 23 | `alibaba.ailabs.aligenie.openvideo.push` |
| 24 | `alibaba.ailabs.iot.device.control.notify` |
| 25 | `alibaba.ailabs.aligenie.skill.entity.import` |
| 26 | `alibaba.ailabs.aligenie.skill.message.push` |
| 27 | `alibaba.ailabs.tmallgenie.auth.device.withshort.qrcode.get` |
| 28 | `alibaba.ailabs.tmallgenie.auth.device.withmac.qrcode.get` |
| 29 | `alibaba.ailabs.iot.cloud.device.report` |
| 30 | `tmall.tmjlapp.sap.serviceorder.cancel` |
| 31 | `alibaba.iot.device.corpus.get` |
| 32 | `taobao.ailab.aicloud.top.message.push` |
| 33 | `alibaba.ailabs.aligenie.opencontent.scenepush` |
| 34 | `alibaba.ailabs.aligenie.openvideoalbum.scenepush` |
| 35 | `alibaba.ailabs.aligenie.openvideo.scenepush` |
| 36 | `taobao.ailab.aicloud.top.message.push.unicast` |
| 37 | `alibaba.aliyun.aicloud.iot.vision.saas.ctcc.jiangsu.cloud.watcher.status.update` |
| 38 | `alibaba.aliyun.aicloud.iot.vision.saas.ctcc.jiangsu.key.secret.update` |
| 39 | `alibaba.ailabs.tmallgenie.auth.device.getcode` |
| 40 | `alibaba.ailabs.tmallgenie.auth.device.validauthcode` |
| 41 | `alibaba.ailabs.tmallgenie.auth.device.qrcode.staticbind` |
| 42 | `alibaba.ai.content.business.send.plan.query` |
| 43 | `alibaba.ai.content.business.send.plan.receive` |
| 44 | `alibaba.ailabs.tmallgenie.third.unicom.shenyan.oper` |
| 45 | `alibaba.ailabs.tmallgenie.third.telecom.pushrender` |
| 46 | `alibaba.ai.content.business.supply.charge` |
| 47 | `alibaba.ailabs.iot.device.mesh.event.invoke` |
| 48 | `alibaba.ailabs.tmallgenie.third.telecom.autoauth` |
| 49 | `taobao.ailab.aicloud.top.id.list.converter` |
| 50 | `alibaba.ailabs.tmallgenie.sdk.device.issupportsdk` |
| 51 | `alibaba.ai.content.business.get.third.cycle.vip.status` |
| 52 | `alibaba.ailabs.tmallgenie.sdk.device.setusersettingelem` |
| 53 | `alibaba.ailabs.tmallgenie.sdk.device.getusersettingelem` |
| 54 | `alibaba.ailabs.tmallgenie.sdk.device.ct.getcteibyuuid` |
| 55 | `alibaba.genie.device.operator.sync` |
| 56 | `alibaba.genie.material.operator.sync` |

</details>

### ICBU卖家API

| # | API名称 |
|---|--------|
| 1 | `alibaba.seller.vendor.order.detail` |
| 2 | `alibaba.seller.vendor.order.list` |
| 3 | `alibaba.seller.coupon.auth.verify` |
| 4 | `alibaba.seller.vendor.service.process` |
| 5 | `alibaba.seller.vendor.service.vendorprocess` |
| 6 | `alibaba.seller.vendor.trade.purchase` |
| 7 | `alibaba.icbu.shopclone.icbuproductrights.query` |
| 8 | `alibaba.icbu.shopclone.externalshopinfo.write` |
| 9 | `alibaba.icbu.shopclone.externalproductinfo.write` |
| 10 | `alibaba.icbu.shopclone.icbushopinfo.query` |

### 智慧园区API (88 APIs)

<details>
<summary>展开查看全部 88 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.campus.topology.getall` |
| 2 | `alibaba.iwork.core.hrs.getperson` |
| 3 | `alibaba.iwork.mc.msg.senddefault` |
| 4 | `alibaba.iwork.mc.msg.sendmobile` |
| 5 | `alibaba.campus.space.group.getbyid` |
| 6 | `alibaba.campus.space.group.getlist` |
| 7 | `alibaba.campus.space.unit.getbyid` |
| 8 | `alibaba.campus.space.unit.getlistbygroupid` |
| 9 | `alibaba.campus.space.unit.getlistmapbygroupid` |
| 10 | `alibaba.campus.space.unit.getlist` |
| 11 | `alibaba.campus.space.group.getlistbycampusandtype` |
| 12 | `alibaba.campus.space.unit.getlistbycampusandtype` |
| 13 | `alibaba.campus.space.floor.getbybuildingid` |
| 14 | `alibaba.campus.space.building.getbycampusid` |
| 15 | `alibaba.campus.device.openapi.operatedevice` |
| 16 | `alibaba.campus.device.openapi.getdevicelist` |
| 17 | `alibaba.campus.device.openapi.getdevicerealtimelog` |
| 18 | `alibaba.campus.device.openapi.getuniquedevice` |
| 19 | `alibaba.campus.device.openapi.getdevicerealtimedata` |
| 20 | `alibaba.campus.acl.queryallemppermiitem` |
| 21 | `alibaba.campus.acl.insertrole` |
| 22 | `alibaba.campus.acl.grantpermiitemtorole` |
| 23 | `alibaba.campus.acl.cancelpermiitemfromrole` |
| 24 | `alibaba.campus.acl.updategrantroletouser` |
| 25 | `alibaba.campus.acl.queryallrole` |
| 26 | `alibaba.campus.acl.getpermissionbyroleid` |
| 27 | `alibaba.campus.acl.grantpermiitemstouser` |
| 28 | `alibaba.campus.acl.getrolebyempid` |
| 29 | `alibaba.campus.acl.checkemprole` |
| 30 | `alibaba.campus.acl.cancelrolesfromuser` |
| 31 | `alibaba.campus.space.campus.getbyid` |
| 32 | `alibaba.campus.device.getdeviceforquery` |
| 33 | `alibaba.campus.acl.getmenubyempid` |
| 34 | `alibaba.campus.space.unit.getlistwithattrbygroupid` |
| 35 | `alibaba.campus.space.unit.getspaceunitlistwithattr` |
| 36 | `alibaba.campus.space.unit.getspaceunitwithattr` |
| 37 | `alibaba.campus.space.attr.setattr` |
| 38 | `alibaba.campus.space.group.getspacegrouplistwithattr` |
| 39 | `alibaba.campus.space.group.getspacegroupwithattr` |
| 40 | `alibaba.campus.adminmap.userlocationinfo.getuserlocationinfologs` |
| 41 | `alibaba.campus.adminmap.userlocationinfo.getactualuserlocationinfobyids` |
| 42 | `alibaba.campus.adminmap.userlocationinfo.insertactualuserlocationinfo` |
| 43 | `alibaba.campus.device.openapi.gethistorydata` |
| 44 | `alibaba.campus.device.openapi.feedbackeventinfo` |
| 45 | `alibaba.campus.device.openapi.saveeventinfoforibos` |
| 46 | `alibaba.campus.adminmap.poiinfo.getlistbygroup` |
| 47 | `alibaba.campus.space.floor.getbyid` |
| 48 | `alibaba.campus.acl.new.checkuserrole` |
| 49 | `alibaba.campus.acl.new.checkuserpermission` |
| 50 | `alibaba.campus.acl.new.getappmenutree` |
| 51 | `alibaba.campus.acl.new.listusermenu` |
| 52 | `alibaba.campus.acl.new.removerole` |
| 53 | `alibaba.campus.acl.new.getrolewithmenutreenodes` |
| 54 | `alibaba.campus.acl.new.saverolewithmenu` |
| 55 | `alibaba.campus.acl.new.listuserroles` |
| 56 | `alibaba.campus.acl.new.freezerole` |
| 57 | `alibaba.campus.acl.new.unfreezerole` |
| 58 | `alibaba.campus.acl.new.deleteuserrole` |
| 59 | `alibaba.campus.acl.new.listroles` |
| 60 | `alibaba.campus.acl.new.pageuserrole` |
| 61 | `alibaba.campus.device.openapi.getsimpledevicelist` |
| 62 | `alibaba.campus.device.openapi.getsimpledevice` |
| 63 | `alibaba.campus.space.type.getbycode` |
| 64 | `alibaba.campus.core.companycampus.getcombycamid` |
| 65 | `alibaba.campus.device.openapi.gettemplatelist` |
| 66 | `alibaba.campus.core.app.getappusages` |
| 67 | `alibaba.campus.space.type.getpageresult` |
| 68 | `alibaba.campus.acl.new.checkusermenu` |
| 69 | `alibaba.campus.guard.data.sync` |
| 70 | `alibaba.campus.acl.new.listuserbymenu` |
| 71 | `alibaba.campus.device.historydata.get` |
| 72 | `alibaba.campus.core.employee.modifyemployee` |
| 73 | `alibaba.campus.devicehub.openapi.reportdata` |
| 74 | `alibaba.guard.access.auth` |
| 75 | `alibaba.visitor.getidsbyqrcode` |
| 76 | `alibaba.campus.space.getbyids` |
| 77 | `alibaba.campus.guardant.data.sync` |
| 78 | `alibaba.campus.guardant.gate.sync` |
| 79 | `alibaba.campus.guardant.gateway.callback` |
| 80 | `alibaba.campus.visitor.image.upload` |
| 81 | `alibaba.campus.guard.controller.configsync` |
| 82 | `alibaba.campus.guard.controller.offlinelog` |
| 83 | `alibaba.campus.guard.controller.offlinedata` |
| 84 | `alibaba.unit.campus.space.bookinfo.query` |
| 85 | `alibaba.campus.guard.timeperiod.listdatetemplate` |
| 86 | `alibaba.campus.guard.timeperiod.listtimerule` |
| 87 | `alibaba.campus.safeguard.arglasses.plate.recognize` |
| 88 | `alibaba.campus.safeguard.arglasses.face.recognize` |

</details>

### 酒店会员API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.potential.member.bind` |
| 2 | `taobao.xhotel.member.derby.state.sync` |
| 3 | `taobao.xhotel.member.derby.coupon.send` |
| 4 | `taobao.xhotel.member.alipay.query` |

### 大麦API (50 APIs)

<details>
<summary>展开查看全部 50 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.damai.ec.search.project.search` |
| 2 | `alibaba.damai.mev.open.pushvenue` |
| 3 | `alibaba.damai.mev.open.deletevenue` |
| 4 | `alibaba.damai.mev.open.batchpushticket` |
| 5 | `alibaba.damai.mev.open.lockticket` |
| 6 | `alibaba.damai.mev.open.resetticket` |
| 7 | `alibaba.damai.mev.open.unlockticket` |
| 8 | `alibaba.damai.mev.open.withdrawticket` |
| 9 | `alibaba.damai.mev.open.changeticket` |
| 10 | `alibaba.damai.mev.open.invalidticket` |
| 11 | `alibaba.damai.mev.open.pushitem` |
| 12 | `alibaba.damai.mev.open.delete.faceelement` |
| 13 | `alibaba.damai.mev.open.deletefloor` |
| 14 | `alibaba.damai.mev.open.pushfaceelement` |
| 15 | `alibaba.damai.mev.open.delete.paperformat` |
| 16 | `alibaba.damai.mev.open.deleteperform` |
| 17 | `alibaba.damai.mev.open.deleteproject` |
| 18 | `alibaba.damai.mev.open.deletestand` |
| 19 | `alibaba.damai.mev.open.deleteface` |
| 20 | `alibaba.damai.mev.open.deleteitem` |
| 21 | `alibaba.damai.mev.open.pushfloor` |
| 22 | `alibaba.damai.mev.open.push.paperformat` |
| 23 | `alibaba.damai.mev.open.pushproject` |
| 24 | `alibaba.damai.mev.open.pushperform` |
| 25 | `alibaba.damai.mev.open.pushface` |
| 26 | `alibaba.damai.mev.open.pushstand` |
| 27 | `alibaba.damai.ec.privilege.query` |
| 28 | `alibaba.damai.ec.privilege.send` |
| 29 | `alibaba.damai.mp.ptnr.getopenaccountbyid` |
| 30 | `alibaba.damai.mp.ptnr.getopenaccountbyuserid` |
| 31 | `alibaba.damai.mp.ptnr.getopenaccountlist` |
| 32 | `alibaba.damai.mp.ptnr.updateemail` |
| 33 | `alibaba.damai.mp.ptnr.updatepassword` |
| 34 | `alibaba.damai.mp.ptnr.updateopenaccountprofile` |
| 35 | `alibaba.damai.mp.ptnr.delete` |
| 36 | `alibaba.damai.mp.ptnr.updateloginid` |
| 37 | `alibaba.damai.mp.ptnr.create` |
| 38 | `alibaba.damai.mp.ptnr.getopenaccountbyemail` |
| 39 | `alibaba.damai.mp.ptnr.msg.notifygroup` |
| 40 | `alibaba.damai.mp.ptnr.openaccount.validatetoken` |
| 41 | `alibaba.damai.mp.ptnr.openaccount.authwithaccountresponse` |
| 42 | `alibaba.damai.mp.ptnr.openaccount.auth` |
| 43 | `alibaba.damai.orderff.auto.query.status` |
| 44 | `alibaba.damai.orderff.auto.query.page` |
| 45 | `alibaba.damai.orderff.auto.query.detail` |
| 46 | `alibaba.damai.orderff.auto.fail` |
| 47 | `alibaba.damai.orderff.auto.reset` |
| 48 | `alibaba.damai.orderff.auto.success` |
| 49 | `alibaba.damai.orderff.auto.pull` |
| 50 | `alibaba.damai.mp.uc.account.order.query` |

</details>

### 换货API

| # | API名称 |
|---|--------|
| 1 | `tmall.exchange.get` |
| 2 | `tmall.exchange.receive.get` |
| 3 | `tmall.exchange.returngoods.agree` |
| 4 | `tmall.exchange.message.add` |
| 5 | `tmall.exchange.messages.get` |
| 6 | `tmall.exchange.agree` |
| 7 | `tmall.exchange.refuse` |
| 8 | `tmall.exchange.returngoods.refuse` |
| 9 | `tmall.exchange.refusereason.get` |
| 10 | `tmall.exchange.consigngoods` |
| 11 | `tmall.exchange.confirm.consign` |

### 商家营销中心API

| # | API名称 |
|---|--------|
| 1 | `taobao.singletreasure.activity.item.batchadd` |
| 2 | `taobao.singletreasure.activity.item.batchupdate` |
| 3 | `taobao.singletreasure.activity.update` |
| 4 | `taobao.singletreasure.activity.delete` |
| 5 | `taobao.singletreasure.activity.create` |
| 6 | `taobao.singletreasure.activity.item.delete` |
| 7 | `taobao.singletreasure.activity.item.update` |
| 8 | `taobao.singletreasure.activity.query` |
| 9 | `taobao.singletreasure.activity.item.query` |
| 10 | `taobao.singletreasure.activity.name.query` |

### 产品中心API

| # | API名称 |
|---|--------|
| 1 | `alibaba.product.merchantproducts.search` |
| 2 | `alibaba.product.spupublishitem.search` |

### ICBU－数据管家

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.industry.topic.list` |
| 2 | `alibaba.icbu.topic.products` |

### ICBU－物流

| # | API名称 |
|---|--------|
| 1 | `alibaba.onetouch.logistics.express.special.product.type.list` |
| 2 | `alibaba.onetouch.logistics.express.charge.calculate` |
| 3 | `alibaba.onetouch.logistics.express.logistics.product.list` |
| 4 | `alibaba.onetouch.logistics.express.logistics.order.create` |
| 5 | `alibaba.onetouch.logistics.express.address.city.list` |
| 6 | `alibaba.onetouch.logistics.express.address.province.list` |
| 7 | `alibaba.onetouch.logistics.express.address.division.list` |
| 8 | `alibaba.onetouch.logistics.express.address.street.list` |
| 9 | `alibaba.onetouch.logistics.express.order.detail.get` |

### ICBU－一达通

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.xiaoman.fundrelation.query` |
| 2 | `alibaba.icbu.xiaoman.acp.notice` |
| 3 | `alibaba.icbu.xiaoman.admittence.query` |
| 4 | `alibaba.icbu.xiaoman.va.letter.get` |

### ICBU－RFQ

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.rfq.search` |
| 2 | `alibaba.icbu.rfqdetail.get` |
| 3 | `alibaba.icbu.quotation.post` |
| 4 | `alibaba.icbu.annex.upload` |
| 5 | `alibaba.icbu.rfq.myequity` |
| 6 | `alibaba.icbu.rfq.recommend` |
| 7 | `alibaba.icbu.rfq.read` |

### ICBU－信保

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.trade.assurance.account.get` |

### ICBU－商品

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.product.sku.inventory.get` |
| 2 | `alibaba.icbu.product.logistics.country.getcoststatus` |
| 3 | `alibaba.icbu.product.country.getcountrylist` |
| 4 | `alibaba.icbu.product.inventory.get` |
| 5 | `alibaba.icbu.text.trans` |
| 6 | `alibaba.icbu.text.recognize.trans` |
| 7 | `alibaba.icbu.text.recognize` |
| 8 | `alibaba.icbu.distribution.product.query` |
| 9 | `alibaba.icbu.distribution.product.get` |

### 飞猪POI数据API

| # | API名称 |
|---|--------|
| 1 | `alitrip.platform.poi.raw.feed` |
| 2 | `alitrip.platform.content.raw.add` |
| 3 | `alitrip.platform.poi.raw.saverawpoi` |
| 4 | `alitrip.platform.poi.raw.poiout` |
| 5 | `alitrip.platform.poi.raw.poioutbypoiids` |

### 飞猪行政区划API

| # | API名称 |
|---|--------|
| 1 | `alitrip.platform.divisions.getdivisionbyname` |
| 2 | `alitrip.platform.divisions.querybyparentid` |

### 零售终端API (23 APIs)

<details>
<summary>展开查看全部 23 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.nrt.branddetail.query` |
| 2 | `tmall.nrt.brandinfo.query` |
| 3 | `tmall.nrt.item.main.synchronize` |
| 4 | `tmall.nrt.item.get` |
| 5 | `tmall.nrt.coupontemplate.query` |
| 6 | `tmall.nrt.coupon.send` |
| 7 | `tmall.nrt.member.synchronize` |
| 8 | `tmall.nrt.stall.synchronize` |
| 9 | `tmall.nrt.pay.merchant.stall.signing.modify` |
| 10 | `tmall.nrt.member.openid` |
| 11 | `tmall.nrt.store.item.from.online.item` |
| 12 | `tmall.nrt.sms.code.send` |
| 13 | `tmall.nrt.scene.activity.query` |
| 14 | `tmall.nrt.coupon.template.syn` |
| 15 | `tmall.nrt.store.relation.query` |
| 16 | `tmall.nrt.store.contract.query` |
| 17 | `tmall.nrt.store.contract.syn` |
| 18 | `tmall.nrt.asset.authorization.delete` |
| 19 | `tmall.nrt.asset.authorization.add` |
| 20 | `tmall.nrt.miaoling.third.login` |
| 21 | `tmall.nrt.pay.merchant.fundstype.modify` |
| 22 | `tmall.nrt.stall.delete` |
| 23 | `tmall.nrt.order.settle.query` |

</details>

### 手淘用户增长

| # | API名称 |
|---|--------|
| 1 | `taobao.usergrowth.dhh.delivery.batchask` |
| 2 | `taobao.usergrowth.dhh.delivery.ask` |
| 3 | `taobao.growth.reaching.buzzword.query` |
| 4 | `taobao.growth.reaching.suggestion.query` |
| 5 | `taobao.growth.reaching.pictures.recognize` |
| 6 | `taobao.usergrowth.user.ecology.record.report` |
| 7 | `taobao.usergrowth.book.sync` |
| 8 | `taobao.usergrowth.book.volume.sync` |
| 9 | `taobao.usergrowth.book.chapter.sync` |
| 10 | `taobao.usergrowth.dhh.feibiao.ask` |

### ALiOS应用中心

| # | API名称 |
|---|--------|
| 1 | `yunos.appstore.pad.hp.applist` |
| 2 | `yunos.appstore.apps.get` |
| 3 | `yunos.appstore.open.reportad` |
| 4 | `yunos.appstore.open.getads` |

### 法务服务API

| # | API名称 |
|---|--------|
| 1 | `alibaba.related.rule.query` |
| 2 | `alibaba.related.rule.batch.query` |
| 3 | `alibaba.related.rule.backup.query` |
| 4 | `alibaba.related.backup.save` |
| 5 | `alibaba.rightguard.measure.progress` |
| 6 | `alibaba.rightguard.file.getdownloadurlbyfileid` |
| 7 | `alibaba.rightguard.file.getfileidbydownloadurl` |

### b2b认证平台api

| # | API名称 |
|---|--------|
| 1 | `alibaba.auth.cert.get` |

### 企业运营平台-集团财务

| # | API名称 |
|---|--------|
| 1 | `alibaba.fpm.file.upload` |
| 2 | `alibaba.sp.open.payment.sync` |
| 3 | `alibaba.sp.open.account.modify` |
| 4 | `alibaba.sp.open.payment.repay` |
| 5 | `alibaba.cfo.incoming.invoice.pyt.image.upload` |
| 6 | `alibaba.cfo.incoming.invoice.pyt.invoice.scan` |
| 7 | `alibaba.cfo.incoming.invoice.register` |
| 8 | `alibaba.cfo.incoming.invoice.pyt.component.statuscallback` |
| 9 | `alibaba.cfo.incoming.invoice.receive` |

### 闲鱼租房

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.business.house.account.bind` |
| 2 | `alibaba.idle.business.house.account.unbind` |
| 3 | `alibaba.idle.business.house.address.upload` |
| 4 | `alibaba.idle.house.office.publish` |
| 5 | `alibaba.idle.house.office.edit` |
| 6 | `alibaba.idle.business.house.image.upload` |
| 7 | `alibaba.idle.business.house.status.update` |
| 8 | `alibaba.idle.house.shop.publish` |
| 9 | `alibaba.idle.house.shop.edit` |
| 10 | `alibaba.idle.business.house.account.bind.query` |

### 阿里巴巴供应链平台API

| # | API名称 |
|---|--------|
| 1 | `alibaba.ascp.qcc.sample.update` |
| 2 | `alibaba.ascp.qcc.sample.cancel.item.relation` |
| 3 | `taobao.logistics.wms.inventory.adjust.report` |
| 4 | `taobao.logistics.wms.goods.query` |

### 天猫新零售 (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.nr.fulfill.cancel.reason.query` |
| 2 | `tmall.nr.fulfill.cancel` |
| 3 | `tmall.nr.fulfill.logistics.consign` |
| 4 | `tmall.nr.fulfill.order.query` |
| 5 | `tmall.nr.fulfill.sold.orderlist.query` |
| 6 | `tmall.nr.fulfill.logistics.query` |
| 7 | `tmall.nr.inventory.initial` |
| 8 | `tmall.nr.inventory.update` |
| 9 | `tmall.nr.notice.goods.ready` |
| 10 | `tmall.nr.zqs.plan.query` |
| 11 | `tmall.nr.fulfill.logistics.sync` |
| 12 | `tmall.nr.order.query.jst` |
| 13 | `tmall.nr.sold.orderlist.query.jst` |
| 14 | `tmall.nr.item.tag.ops` |
| 15 | `tmall.nr.order.logis.info` |
| 16 | `tmall.nr.seller.storerange.read` |
| 17 | `tmall.nr.seller.storerange.sync` |
| 18 | `alibaba.lsy.crm.activity.get` |
| 19 | `alibaba.lsy.crm.customer.add` |
| 20 | `alibaba.lsy.crm.activity.getbaseinfo` |
| 21 | `tmall.nrt.newcoupon.send` |
| 22 | `alibaba.lsy.crm.customer.add.new` |
| 23 | `tmall.nrt.certificate.send` |
| 24 | `tmall.nrt.certificate.query` |
| 25 | `tmall.nrt.coupon.instance.query` |
| 26 | `alibaba.lsy.crm.customer.appoint` |
| 27 | `alibaba.lsy.crm.activity.sellerinfo` |

</details>

### 酒店团购套餐API

| # | API名称 |
|---|--------|
| 1 | `alitrip.tuan.hotel.adapt.store.get` |
| 2 | `alitrip.tuan.hotel.shop.category.get` |
| 3 | `alitrip.tuan.hotel.item.sku.delete` |
| 4 | `alitrip.tuan.hotel.item.sku.update` |
| 5 | `alitrip.tuan.hotel.item.info.get` |
| 6 | `alitrip.tuan.hotel.image.upload` |
| 7 | `alitrip.tuan.hotel.item.sku.calendar.update` |
| 8 | `taobao.xhotel.combo.status.get` |
| 9 | `taobao.xhotel.combo.review` |
| 10 | `taobao.xhotel.combo.offshelf` |
| 11 | `taobao.xhotel.combo.schema.offshelf` |
| 12 | `taobao.xhotel.combo.schema.review` |

### 阿里影业云智API (22 APIs)

<details>
<summary>展开查看全部 22 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.lark.iot.order.getgoodslist` |
| 2 | `taobao.lark.iot.order.getcinemas` |
| 3 | `taobao.lark.iot.order.confirmorder` |
| 4 | `taobao.lark.pos.basedata.getworkstation` |
| 5 | `taobao.lark.product.upgrade.task` |
| 6 | `taobao.lark.cinema.device.heart` |
| 7 | `taobao.lark.cinema.device.remote.bind` |
| 8 | `taobao.lark.cinema.device.remote.url` |
| 9 | `taobao.lark.cinema.monitor.report` |
| 10 | `taobao.lark.specialfunds.open.queryticket` |
| 11 | `taobao.lark.cinema.device.get` |
| 12 | `taobao.lark.specialfunds.ca.sign` |
| 13 | `taobao.lark.device.secret.active` |
| 14 | `taobao.lark.device.config.get` |
| 15 | `taobao.lark.device.secret.get` |
| 16 | `taobao.lark.device.productversion.push` |
| 17 | `taobao.lark.product.install.get` |
| 18 | `taobao.lark.specialfunds.ca.sign.schedule` |
| 19 | `taobao.lark.cinema.device.task.online` |
| 20 | `taobao.lark.device.credentials.oss.get` |
| 21 | `taobao.lark.cinema.data.backup.report` |
| 22 | `taobao.lark.device.platform.api.route` |

</details>

### 渠道中心API

| # | API名称 |
|---|--------|
| 1 | `tmall.channel.trade.order.get` |
| 2 | `tmall.channel.trade.order.gets` |
| 3 | `tmall.channel.products.query` |

### 阿里健康-疫苗API (21 APIs)

<details>
<summary>展开查看全部 21 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.vaccin.notice.user.create` |
| 2 | `alibaba.health.vaccin.notice.order.cancel` |
| 3 | `alibaba.health.vaccin.notice.order.sign` |
| 4 | `alibaba.health.vaccin.notice.order.create` |
| 5 | `alibaba.health.vaccin.notice.replant.remind` |
| 6 | `alibaba.health.vaccin.notice.announcement.publish` |
| 7 | `alibaba.health.vaccin.notice.user.bind` |
| 8 | `alibaba.health.vaccin.notice.timebucket.remind` |
| 9 | `alibaba.health.vaccin.pov.update` |
| 10 | `alibaba.health.vaccin.notice.send` |
| 11 | `alibaba.health.vaccin.vaccinate.complete` |
| 12 | `alibaba.alihealth.vaccine.register.submit` |
| 13 | `alibaba.alihealth.vaccine.register.cancel` |
| 14 | `alibaba.health.vaccin.order.update` |
| 15 | `alibaba.health.vaccin.appointment.result.notify` |
| 16 | `alibaba.alihealth.vaccine.trade.subscribe.detail.get` |
| 17 | `alibaba.alihealth.vaccine.trade.order.channel.get` |
| 18 | `alibaba.alihealth.vaccine.trade.subscribe.detail.save` |
| 19 | `alibaba.health.vaccin.subscribe.info.return` |
| 20 | `alibaba.health.vaccin.match.on` |
| 21 | `alibaba.health.vaccin.user.register.remind` |

</details>

### 教育账号 API

| # | API名称 |
|---|--------|
| 1 | `yunos.dm.sys.get.domain` |

### 用户增长

| # | API名称 |
|---|--------|
| 1 | `taobao.usergrowth.ad.media.data.sync` |
| 2 | `taobao.usergrowth.ad.material.data.sync` |
| 3 | `taobao.usergrowth.ad.material.audit` |
| 4 | `taobao.usergrowth.ad.material.query` |

### AE-供应链

| # | API名称 |
|---|--------|
| 1 | `aliexpress.ascp.po.query` |
| 2 | `aliexpress.ascp.po.item.query` |
| 3 | `aliexpress.ascp.fro.item.query` |
| 4 | `aliexpress.ascp.item.query` |
| 5 | `aliexpress.ascp.fro.query` |
| 6 | `aliexpress.ascp.ffo.item.query` |
| 7 | `aliexpress.ascp.ffo.query` |
| 8 | `aliexpress.ascp.inventory.log.query` |
| 9 | `aliexpress.ascp.warehouse.inventory.query` |

### 飞猪机票前台类目

| # | API名称 |
|---|--------|
| 1 | `alitrip.uppc.member.gain` |
| 2 | `alitrip.flight.basic.data.city.queryAll` |
| 3 | `alitrip.flight.flightchange.order.query` |

### 平台治理API

| # | API名称 |
|---|--------|
| 1 | `taobao.cloudbridge.caseinvest.execute` |
| 2 | `taobao.sungari.dispose.submit` |
| 3 | `taobao.sungari.dispose.query` |
| 4 | `taobao.sungari.inspection.submit` |

### 天猫超市前台API

| # | API名称 |
|---|--------|
| 1 | `tmall.txcs.finance.bill.query` |
| 2 | `alibaba.mc.tms.settlement.metadata.upload` |
| 3 | `taobao.maochao.oss.authinfo.get` |
| 4 | `taobao.maochao.oss.fileurl.sync` |

### 阿里健康医生 (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.asyncprescribe.prescription.search` |
| 2 | `alibaba.alihealth.asyncprescribe.prescription.detail` |
| 3 | `alibaba.alihealth.outflow.drug.supervision.query` |
| 4 | `alibaba.alihealth.outflow.prescription.hospital.verify` |
| 5 | `alibaba.alihealth.doctor.leshui.ticket.valid` |
| 6 | `alibaba.alihealth.doctor.leshui.audit.result` |
| 7 | `alibaba.alihealth.doctor.leshui.apply.notify` |
| 8 | `alibaba.alihealth.rx.ca.doctor.status.save` |
| 9 | `alibaba.alihealth.rx.ca.prescribe.signed.status.save` |
| 10 | `alibaba.alihealth.rx.ca.device.sign.status.save` |
| 11 | `alibaba.alihealth.doctor.income.update` |
| 12 | `alibaba.alihealth.recommend.cardinfo.get` |
| 13 | `alibaba.alihealth.recommend.mixcardinfo.get` |
| 14 | `alibaba.alihealth.supplier.doctor.income.get` |
| 15 | `alibaba.alihealth.supplier.account.statement.get` |
| 16 | `alibaba.alihealth.supplier.doctor.register.sync` |
| 17 | `alibaba.alihealth.supplier.doctor.tax.sync` |

</details>

### 飞猪酒店标准库

| # | API名称 |
|---|--------|
| 1 | `alitrip.hotel.hstdf.shotel.matchsroomself` |
| 2 | `alitrip.hotel.hstdf.shotel.matchshotelself` |
| 3 | `alitrip.hotel.hstdf.shotel.exportshotel` |
| 4 | `alitrip.hotel.hstdf.shotel.exportsroomtype` |
| 5 | `alitrip.hotel.hstdf.shotel.exnotmatchroom` |
| 6 | `alitrip.hotel.hstdf.poilocation.get` |
| 7 | `alitrip.hotel.hstdf.hotelroomstatic.get` |
| 8 | `alitrip.hotel.hstdf.businessarea.get` |
| 9 | `alitrip.hotel.hstdf.shotel.roomtype.mappings.list` |
| 10 | `taobao.xhotel.hotel.message.receive` |

### AE-Dropshipper

| # | API名称 |
|---|--------|
| 1 | `aliexpress.postproduct.redefining.findaeproductbyidfordropshipper` |
| 2 | `aliexpress.trade.buy.placeorder` |
| 3 | `aliexpress.logistics.buyer.freight.calculate` |
| 4 | `aliexpress.trade.ds.order.get` |
| 5 | `aliexpress.logistics.ds.trackinginfo.query` |
| 6 | `aliexpress.offer.ds.product.simplequery` |
| 7 | `aliexpress.ds.add.info` |
| 8 | `aliexpress.ds.recommend.feed.get` |
| 9 | `aliexpress.ds.product.get` |
| 10 | `aliexpress.ds.image.search` |
| 11 | `aliexpress.ds.commissionorder.listbyindex` |
| 12 | `aliexpress.ds.trade.order.get` |
| 13 | `aliexpress.ds.member.orderdata.submit` |

### 银泰scm-openapi

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.goods.bulkinputcspu` |
| 2 | `alibaba.mos.goods.adjust` |
| 3 | `alibaba.mos.goods.synchinventorybycounting` |
| 4 | `alibaba.mos.goods.searchcspu` |
| 5 | `alibaba.mos.goods.setprice` |
| 6 | `alibaba.mos.order.list.get` |
| 7 | `alibaba.mos.order.refund.list.get` |
| 8 | `alibaba.mos.goods.inventory.getinventorys` |
| 9 | `alibaba.mos.delivery.send` |
| 10 | `alibaba.mos.order.query` |
| 11 | `alibaba.mos.isv.inventory.scrollquery` |

### 信息平台-采购 (26 APIs)

<details>
<summary>展开查看全部 26 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.ceres.supplier.po.query` |
| 2 | `alibaba.ceres.supplier.po.querydetail` |
| 3 | `alibaba.pur.pr.create` |
| 4 | `alibaba.pur.product.sync` |
| 5 | `alibaba.pur.media.statistics` |
| 6 | `alibaba.pur.basket.merge` |
| 7 | `alibaba.pur.supplier.porespcreate` |
| 8 | `alibaba.pur.supplier.asncreate` |
| 9 | `alibaba.pur.supplier.invoicecreate` |
| 10 | `alibaba.pur.create.do` |
| 11 | `alibaba.pur.cmall.goods.sync` |
| 12 | `alibaba.pur.cmall.goods.status.sync` |
| 13 | `alibaba.pur.cmall.package.sync` |
| 14 | `alibaba.pur.resource.api.product.get` |
| 15 | `alibaba.pur.resource.api.order.cancel` |
| 16 | `alibaba.pur.resource.api.order.create` |
| 17 | `alibaba.pur.resource.api.order.before.check` |
| 18 | `alibaba.pur.resource.api.price.get` |
| 19 | `alibaba.pur.resource.api.product.list` |
| 20 | `alibaba.pur.resource.api.order.detail` |
| 21 | `alibaba.pur.prod.rcv.rt.query` |
| 22 | `alibaba.ceres.supplier.prod.po.querydetail` |
| 23 | `aliyun.prod.purchase.po.pay.progress.query` |
| 24 | `aliyun.prod.purchase.po.pay.query` |
| 25 | `aliyun.prod.purchase.po.kp.query` |
| 26 | `alibaba.pur.supplier.feedbackcsol` |

</details>

### 手淘互动API

| # | API名称 |
|---|--------|
| 1 | `taobao.hudong.achievement.shop.discount.query` |
| 2 | `taobao.hudong.achievement.shop.discount.update` |
| 3 | `taobao.hudong.achievement.users.eligibility.check` |

### 淘宝小程序API

| # | API名称 |
|---|--------|
| 1 | `taobao.miniapp.cloud.function.invoke` |
| 2 | `taobao.miniapp.cloud.store.relation.add` |
| 3 | `taobao.smartapp.table.list.get` |
| 4 | `taobao.smartapp.table.meta.get` |
| 5 | `taobao.smartapp.table.add` |
| 6 | `taobao.smartapp.table.update` |
| 7 | `taobao.smartapp.table.get` |
| 8 | `taobao.miniapp.ext.delivery.app.channel.sync` |
| 9 | `taobao.miniapp.ext.delivery.app.channel.configs.query` |
| 10 | `taobao.miniapp.ext.delivery.sell.channel.configs.query` |
| 11 | `taobao.miniapp.ext.delivery.sell.channel.config.sync` |
| 12 | `taobao.miniapp.ext.delivery.seller.task.sync` |
| 13 | `taobao.smartapp.table.fulldata.get` |
| 14 | `taobao.miniapp.tpwd.create` |

### ott支付

| # | API名称 |
|---|--------|
| 1 | `youku.ott.pay.order.queryorderbycp` |
| 2 | `youku.ott.pay.order.queryorder` |
| 3 | `youku.ott.pay.order.createorder` |
| 4 | `youku.ott.pay.order.authpay` |
| 5 | `youku.ott.pay.order.deleteorder` |
| 6 | `youku.ott.iot.status.push` |
| 7 | `youku.ott.iot.devicelist.change` |
| 8 | `youku.ott.pay.order.querycporder` |
| 9 | `youku.ott.pay.order.queryauthstate` |
| 10 | `youku.ott.pay.order.authpaywithprice` |

### 天猫汽车 (37 APIs)

<details>
<summary>展开查看全部 37 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.car.lease.citysynchronize` |
| 2 | `tmall.car.lease.statussynchronize` |
| 3 | `tmall.car.lease.exceptionflowsynchronize` |
| 4 | `tmall.car.lease.queryloanplans` |
| 5 | `tmall.car.lease.payforcustomer` |
| 6 | `tmall.car.lease.orderid.get` |
| 7 | `tmall.car.xcar.synchronize.car.line.data` |
| 8 | `tmall.car.xcar.synchronize.car.model.data` |
| 9 | `tmall.car.xcar.synchronize.car.line.pics.data` |
| 10 | `taobao.car.vehicleinfo.register` |
| 11 | `tmall.aliauto.meta.receive` |
| 12 | `tmall.car.order.query` |
| 13 | `tmall.aliauto.service.receipt.get` |
| 14 | `tmall.aliauto.receipt.state.update` |
| 15 | `tmall.aliauto.order.qrcode` |
| 16 | `tmall.aliauto.service.item.get` |
| 17 | `tmall.aliauto.receipt.order.check` |
| 18 | `tmall.aliauto.eticket.consume` |
| 19 | `tmall.aliauto.eticket.status` |
| 20 | `tmall.aliauto.trade.car.order.get` |
| 21 | `tmall.aliauto.fulfillment.contract.sign` |
| 22 | `tmall.aliauto.trade.restpayfee.modify` |
| 23 | `tmall.aliauto.trade.car.eticket.available.check` |
| 24 | `tmall.aliauto.trade.car.eticket.consume` |
| 25 | `tmall.car.carefree.detail.get` |
| 26 | `tmall.car.finance.detail.get` |
| 27 | `tmall.car.finance.status.sync` |
| 28 | `tmall.aliauto.wisdomdata.omid.recieve` |
| 29 | `tmall.aliauto.fulfillment.delivery.syn` |
| 30 | `tmall.aliauto.fulfillment.auth.check` |
| 31 | `tmall.aliauto.trade.external.order.sycn` |
| 32 | `tmall.aliauto.order.eticket.consume` |
| 33 | `tmall.aliauto.order.auth.check` |
| 34 | `tmall.aliauto.omid.series.mapping.query` |
| 35 | `tmall.aliauto.omid.model.mapping.query` |
| 36 | `tmall.aliauto.series.convert.query` |
| 37 | `tmall.aliauto.model.convert.query` |

</details>

### 麦座API (45 APIs)

<details>
<summary>展开查看全部 45 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.damai.mz.user.register` |
| 2 | `alibaba.damai.mz.user.baseinfo.get` |
| 3 | `alibaba.damai.mz.user.token.refresh` |
| 4 | `alibaba.damai.mz.user.token.apply` |
| 5 | `alibaba.damai.mz.user.userlevel.list` |
| 6 | `alibaba.damai.mz.user.userlevel.modify` |
| 7 | `alibaba.damai.mz.user.baseinfo.modify` |
| 8 | `alibaba.damai.mz.project.class.list` |
| 9 | `alibaba.damai.mz.project.list` |
| 10 | `alibaba.damai.mz.project.detail` |
| 11 | `alibaba.damai.mz.event.list` |
| 12 | `alibaba.damai.mz.order.list` |
| 13 | `alibaba.damai.mz.order.detail` |
| 14 | `alibaba.damai.mz.order.cancel` |
| 15 | `alibaba.damai.mz.order.confirm` |
| 16 | `alibaba.damai.mz.order.create` |
| 17 | `alibaba.damai.mz.paytype.list` |
| 18 | `alibaba.damai.mz.venue.info.get` |
| 19 | `alibaba.damai.mz.user.couponcode.bind` |
| 20 | `alibaba.damai.mz.stand.list` |
| 21 | `alibaba.damai.mz.seat.list` |
| 22 | `alibaba.damai.mz.seat.state.list` |
| 23 | `alibaba.damai.mz.order.render` |
| 24 | `alibaba.damai.mz.promotion.list` |
| 25 | `alibaba.damai.mz.ticket.list` |
| 26 | `alibaba.damai.mz.user.address.add` |
| 27 | `alibaba.damai.mz.user.address.modify` |
| 28 | `alibaba.damai.mz.user.address.remove` |
| 29 | `alibaba.damai.mz.user.address.list` |
| 30 | `alibaba.damai.mz.user.address.default` |
| 31 | `alibaba.damai.mz.user.address.detail` |
| 32 | `alibaba.damai.mz.user.logout` |
| 33 | `alibaba.damai.mz.user.card.bind` |
| 34 | `alibaba.damai.mz.user.card.list` |
| 35 | `alibaba.damai.mz.user.mobilephone.reset` |
| 36 | `alibaba.damai.mz.promotion.detail` |
| 37 | `alibaba.damai.mz.user.thirduid.modify` |
| 38 | `alibaba.damai.mz.b.ptnr.order.list` |
| 39 | `alibaba.damai.mz.b.ptnr.order.tickets` |
| 40 | `alibaba.damai.mz.partners.list` |
| 41 | `alibaba.damai.mz.sponsors.list` |
| 42 | `alibaba.damai.mz.promotion.modify.password` |
| 43 | `alibaba.damai.mz.b.event.sale.data` |
| 44 | `alibaba.damai.mz.card.type.list` |
| 45 | `alibaba.damai.mz.refund.order.detail` |

</details>

### ALIOS广告平台

| # | API名称 |
|---|--------|
| 1 | `yunos.admarket.ad.bid` |
| 2 | `yunos.admarket.material.audit` |

### 业务平台新零售

| # | API名称 |
|---|--------|
| 1 | `taobao.uscesl.iteminfo.put` |
| 2 | `taobao.uscesl.iteminfo.batch.put` |
| 3 | `taobao.uscesl.iteminfo.batch.insert` |
| 4 | `taobao.uscesl.biz.store.insert` |
| 5 | `taobao.uscesl.biz.brand.insert` |
| 6 | `taobao.uscesl.biz.esl.unbind` |
| 7 | `taobao.uscesl.biz.esl.bind` |
| 8 | `taobao.uscesl.biz.esl.info.get` |
| 9 | `taobao.uscesl.biz.ap.delete` |
| 10 | `taobao.uscesl.biz.ap.add` |
| 11 | `taobao.uscesl.biz.light.up` |
| 12 | `taobao.uscesl.biz.ap.activate` |
| 13 | `taobao.uscesl.biz.ap.search` |
| 14 | `taobao.uscesl.biz.item.light.up` |

### 大麦第三方商家接入API

| # | API名称 |
|---|--------|
| 1 | `alibaba.damai.ticklet.qrcode.decode` |
| 2 | `alibaba.damai.mx.opengateway.script` |

### 天猫权益平台api

| # | API名称 |
|---|--------|
| 1 | `alibaba.tmallnft.nft.presend` |

### ICBU商品api

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.product.id.encrypt` |
| 2 | `alibaba.icbu.product.inventory.update` |
| 3 | `alibaba.icbu.product.type.available.get` |

### 神鲸应用API

| # | API名称 |
|---|--------|
| 1 | `alibaba.shenjing.core.activity.getappshowlist` |
| 2 | `alibaba.ib.shenjing.visitor.pad.getqrcodelink` |
| 3 | `alibaba.ib.shenjing.visitor.pad.opendoor` |
| 4 | `alibaba.ib.shenjing.visitor.pad.uploadface` |
| 5 | `alibaba.ib.shenjing.visitor.pad.fetchcodeverify` |
| 6 | `alibaba.ib.shenjing.visitor.pad.getinfo` |

### 阿里影业灯塔

| # | API名称 |
|---|--------|
| 1 | `alibaba.pictures.dengta.order.status.change` |
| 2 | `alibaba.pictures.dengta.wbaccount.price.change` |
| 3 | `alibaba.pictures.dengta.wxaccount.price.change` |
| 4 | `alibaba.pictures.dengta.order.effect.import` |
| 5 | `alibaba.pictures.dengta.ims.douyin.account.changed` |
| 6 | `alibaba.pictures.dengta.ims.order.status.change` |

### 激励API

| # | API名称 |
|---|--------|
| 1 | `taobao.degoperation.check.addr.status` |
| 2 | `taobao.degoperation.show.user.records` |
| 3 | `taobao.degoperation.show.top.records` |
| 4 | `taobao.degoperation.get.by.eventkey` |
| 5 | `taobao.degoperation.do.luckydraw` |
| 6 | `taobao.degoperation.get.info.uuid` |
| 7 | `taobao.degoperation.createqrcode` |

### 优酷-媒资

| # | API名称 |
|---|--------|
| 1 | `youku.mediaapi.video.snapshot.get` |
| 2 | `youku.tvoperator.media.page.query` |
| 3 | `youku.ott.kitty.commonorder.sync` |

### 飞猪会员API

| # | API名称 |
|---|--------|
| 1 | `alibaba.fliggy.interaction.mileage.get` |

### 优酷网盟

| # | API名称 |
|---|--------|
| 1 | `youku.dsp.delivery.resource.multiget` |

### 阿里健康API (69 APIs)

<details>
<summary>展开查看全部 69 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.trade.drug.get` |
| 2 | `taobao.trade.drug.confirmorder` |
| 3 | `taobao.drug.quantity.update` |
| 4 | `taobao.drug.price.update` |
| 5 | `taobao.trade.drug.orders.get` |
| 6 | `alibaba.alihealth.examination.stock.query` |
| 7 | `taobao.drug.shop.list` |
| 8 | `taobao.drug.quantity.batch.update` |
| 9 | `taobao.drug.price.batch.update` |
| 10 | `taobao.trade.drug.order.get` |
| 11 | `alibaba.alihealth.ms.area.province.list` |
| 12 | `alibaba.alihealth.tracecodeseller.product.search` |
| 13 | `alibaba.alihealth.tracecodeseller.warehouse.search` |
| 14 | `alibaba.alihealth.tracecodeseller.channel.search` |
| 15 | `alibaba.alihealth.tracecodeseller.bill.upload` |
| 16 | `alibaba.alihealth.tracecodeseller.bill.result.search` |
| 17 | `alibaba.alihealth.tracecodeseller.ent.search` |
| 18 | `alibaba.alihealth.tracecodeseller.code.relation.codeantiactive` |
| 19 | `alibaba.alihealth.reserve.dental.markitem` |
| 20 | `alibaba.alihealth.reserve.dental.bindshopanditem` |
| 21 | `alibaba.alihealth.reserve.dental.storesanditems` |
| 22 | `alibaba.alihealth.reserve.dental.unbinditem` |
| 23 | `alibaba.alihealth.reserve.dental.modifyrestime` |
| 24 | `alibaba.alihealth.medical.registration.sync` |
| 25 | `alibaba.alihealth.medical.department.sync` |
| 26 | `alibaba.alihealth.medical.doctor.sync` |
| 27 | `alibaba.alihealth.medical.registration.syncnew` |
| 28 | `alibaba.alihealth.booking.reserve.confirm` |
| 29 | `alibaba.alihealth.booking.reserve.treat` |
| 30 | `alibaba.alihealth.booking.reserve.cancel` |
| 31 | `alibaba.alihealth.booking.reserve.checkin` |
| 32 | `alibaba.alihealth.booking.reserve.modify` |
| 33 | `alibaba.alihealth.dental.item.list` |
| 34 | `alibaba.alihealth.dental.item.bind` |
| 35 | `alibaba.alihealth.dental.item.unbind` |
| 36 | `alibaba.alihealth.dental.store.insertorupdate` |
| 37 | `alibaba.alihealth.dental.store.audit.query` |
| 38 | `alibaba.alihealth.dental.bind.audit.query` |
| 39 | `alibaba.alihealth.tracecodeseller.code.single.codereplace` |
| 40 | `alibaba.alihealth.nocov.alldiseaseinfo.get` |
| 41 | `alibaba.alihealth.booking.reserve.rise` |
| 42 | `alibaba.alihealth.dental.statement.query` |
| 43 | `alibaba.alihealth.dental.store.invisible.consume.update` |
| 44 | `alibaba.alihealth.docbase.userinfo.alipayid.get` |
| 45 | `alibaba.alihealth.store.certificate.create` |
| 46 | `alibaba.health.nr.cep.warstqty.batchupdate` |
| 47 | `alibaba.health.nr.cep.outorder.upload` |
| 48 | `alibaba.health.nr.cep.order.query` |
| 49 | `alibaba.alihealth.druguse.query` |
| 50 | `alibaba.alihealth.medicalbase.hos.status.sync` |
| 51 | `alibaba.alihealth.medicalbase.doctor.status.sync` |
| 52 | `alibaba.alihealth.medicalbase.dept.status.sync` |
| 53 | `alibaba.alihealth.imrisk.query` |
| 54 | `alibaba.alihealth.medicalbase.third.order.sync` |
| 55 | `alibaba.alihealth.medicalbase.hos.syncnew` |
| 56 | `alibaba.alihealth.medicalbase.dept.syncnew` |
| 57 | `alibaba.alihealth.medicalbase.doctor.syncnew` |
| 58 | `alibaba.alihealth.medicalbase.third.evaluate.sync` |
| 59 | `alibaba.alihealth.bc.future.stock.inbound` |
| 60 | `alibaba.alihealth.tms.cut.confirm` |
| 61 | `alibaba.alihealth.bc.future.stock.outbound` |
| 62 | `alibaba.alihealth.bc.item.period.sync` |
| 63 | `alibaba.alihealth.btob.order.confirm` |
| 64 | `alibaba.alihealth.btob.refundorder.confirm` |
| 65 | `alibaba.alihealth.shangou.inventory.adjust` |
| 66 | `alibaba.alihealth.shangou.order.pickup` |
| 67 | `alibaba.alihealth.shangou.order.confirm` |
| 68 | `alibaba.alihealth.shangou.oss.get` |
| 69 | `alibaba.alihealth.cne.trace.push` |

</details>

### pos交易api

| # | API名称 |
|---|--------|
| 1 | `taobao.payment.cashier.standard.pay` |
| 2 | `taobao.payment.cashier.allinPay.pay` |

### 新制造API

| # | API名称 |
|---|--------|
| 1 | `taobao.xunxi.hetai.wms.send.dingmessage` |
| 2 | `taobao.xunxi.hetai.wms.company.sync` |
| 3 | `taobao.rhino.integration.crafts.product.sync` |
| 4 | `taobao.rhino.integration.crafts.dtechitem.authurl.get` |
| 5 | `taobao.rhino.integration.crafts.craftform.export` |

### 五道口商品API

| # | API名称 |
|---|--------|
| 1 | `alibaba.wdk.item.merchantsku.update` |
| 2 | `alibaba.wdk.item.merchantsku.query` |
| 3 | `alibaba.wdk.item.merchantsku.create` |
| 4 | `alibaba.wdk.item.brand.query` |
| 5 | `alibaba.wdk.item.category.query` |
| 6 | `alibaba.wdk.item.storesku.query` |
| 7 | `alibaba.wdk.picture.upload` |
| 8 | `alibaba.wdk.item.futureprice.query` |

### 零售通订单履行

| # | API名称 |
|---|--------|
| 1 | `alibaba.lst.shiporder.create` |
| 2 | `alibaba.lst.shiporder.cancel` |
| 3 | `alibaba.lst.shiporder.query` |

### 天猫线下大屏

| # | API名称 |
|---|--------|
| 1 | `tmall.fcbox.notify` |

### AE-Oversea-Solution (26 APIs)

<details>
<summary>展开查看全部 26 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `aliexpress.solution.product.post` |
| 2 | `aliexpress.solution.sku.attribute.query` |
| 3 | `aliexpress.solution.product.edit` |
| 4 | `aliexpress.solution.issue.partner.rma.reverselogistic.state.update` |
| 5 | `aliexpress.solution.issue.partner.rma.reverselogistic.trackinginfo.create` |
| 6 | `aliexpress.solution.issue.partner.rma.screening.create` |
| 7 | `aliexpress.solution.issue.partner.rma.state.update` |
| 8 | `aliexpress.solution.order.fulfill` |
| 9 | `aliexpress.solution.order.get` |
| 10 | `aliexpress.solution.order.receiptinfo.get` |
| 11 | `aliexpress.solution.product.info.get` |
| 12 | `aliexpress.solution.product.list.get` |
| 13 | `aliexpress.solution.order.info.get` |
| 14 | `aliexpress.solution.product.schema.get` |
| 15 | `aliexpress.solution.schema.product.instance.post` |
| 16 | `aliexpress.solution.feed.submit` |
| 17 | `aliexpress.solution.feed.query` |
| 18 | `aliexpress.solution.schema.product.full.update` |
| 19 | `aliexpress.solution.batch.product.inventory.update` |
| 20 | `aliexpress.solution.batch.product.price.update` |
| 21 | `aliexpress.solution.seller.category.tree.query` |
| 22 | `aliexpress.solution.merchant.profile.get` |
| 23 | `aliexpress.solution.feed.list.get` |
| 24 | `aliexpress.solution.batch.product.delete` |
| 25 | `aliexpress.solution.feed.invalidate` |
| 26 | `aliexpress.solution.product.category.suggest` |

</details>

### 阿里精灵基础能力接口

| # | API名称 |
|---|--------|
| 1 | `alibaba.ailabs.aligenie.device.unbind` |

### 阿里健康新零售

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.nr.logistics.query` |

### 闲鱼发布

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.recycle.order.get` |
| 2 | `alibaba.idle.isv.item.query.batch` |

### 飞猪酒店签约中心

| # | API名称 |
|---|--------|
| 1 | `alitrip.hotel.single.info.get` |
| 2 | `alitrip.hotel.hms.partner.info.get` |
| 3 | `alitrip.hotel.alliance.hid.get` |
| 4 | `alitrip.hotel.alliance.settle.order.syn` |

### 人工智能实验室开放平台API (25 APIs)

<details>
<summary>展开查看全部 25 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.ailab.user.token.get` |
| 2 | `alibaba.ailabs.iot.device.status.update` |
| 3 | `alibaba.ailabs.tvs.device.list` |
| 4 | `alibaba.ailabs.iot.device.list.update.notify` |
| 5 | `alibaba.ailab.user.authorized.query` |
| 6 | `alibaba.ailab.user.authorized.cancel` |
| 7 | `taobao.ailab.aicloud.top.hotwords.get` |
| 8 | `taobao.ailab.aicloud.top.hotwords.update` |
| 9 | `alibaba.ailabs.tmallgenie.auth.taobaoauth` |
| 10 | `alibaba.ailabs.tmallgenie.auth.refresh` |
| 11 | `alibaba.ailabs.tmallgenie.auth.device.list` |
| 12 | `alibaba.ailabs.tmallgenie.auth.device.get` |
| 13 | `alibaba.ailabs.tmallgenie.auth.device.unbind` |
| 14 | `alibaba.ailabs.tmallgenie.auth.gettoken` |
| 15 | `alibaba.ailabs.tmallgenie.auth.getcode` |
| 16 | `alibaba.ailabs.tmallgenie.auth.device.qrcode.activate` |
| 17 | `alibaba.ailab.tb.user.skill.oauth` |
| 18 | `alibaba.ailab.user.profile.get` |
| 19 | `alibaba.ailabs.tmallgenie.auth.device.status.get` |
| 20 | `alibaba.ailabs.tmallgenie.auth.switchuser` |
| 21 | `alibaba.ailab.user.open.uid.get` |
| 22 | `alibaba.ailabs.tmallgenie.auth.device.withdeviceid.get` |
| 23 | `taobao.ailab.aicloud.top.skils.list.new` |
| 24 | `alibaba.ailabs.tmallgenie.auth.device.status.getbyctei` |
| 25 | `alibaba.ailabs.tmallgenie.auth.device.qrcode.bind` |

</details>

### 飞猪会员互通API

| # | API名称 |
|---|--------|
| 1 | `alitrip.mi.member.mile.resend` |

### MOZI账号API

| # | API名称 |
|---|--------|
| 1 | `alibaba.mozi.fusion.addorupdate.employee.account` |
| 2 | `alibaba.mozi.fusion.create.employee.account` |
| 3 | `alibaba.mozi.fusion.dimission.employee.account` |
| 4 | `alibaba.mozi.fusion.reentry.employee.account` |
| 5 | `alibaba.mozi.fusion.update.employee.account` |
| 6 | `alibaba.mozi.buc.account.list.accountids` |
| 7 | `alibaba.mozi.buc.account.pageall` |
| 8 | `alibaba.mozi.vds.tenant.api.service.dismiss` |
| 9 | `alibaba.mozi.vds.tenant.api.service.tenantbyid` |
| 10 | `alibaba.mozi.vds.tenant.api.service.getadmin` |
| 11 | `alibaba.mozi.vds.tenant.api.service.pagesubadmins` |
| 12 | `alibaba.mozi.vds.tenant.api.service.matchempcodes` |

### ICBU-橱窗

| # | API名称 |
|---|--------|
| 1 | `alibaba.scbp.showcase.status` |
| 2 | `alibaba.scbp.showcase.list` |
| 3 | `alibaba.scbp.showcase.deleteproduct` |
| 4 | `alibaba.scbp.showcase.addproduct` |
| 5 | `alibaba.scbp.showcase.sort` |
| 6 | `alibaba.scbp.showcase.updateproduct` |

### 云码API

| # | API名称 |
|---|--------|
| 1 | `tmall.mc.record.order.sync` |
| 2 | `tmall.mc.task.charge.launch` |
| 3 | `tmall.mc.device.circle.check` |
| 4 | `aliyun.unimkt.task.charge.launch` |

### MOZI权限API (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.mozi.acl.grant.grantrole` |
| 2 | `alibaba.mozi.acl.userpermissions.revoke` |
| 3 | `alibaba.mozi.acl.role.add.permissions` |
| 4 | `alibaba.mozi.acl.role.add` |
| 5 | `alibaba.mozi.acl.userroles.revoke` |
| 6 | `alibaba.mozi.acl.permission.page.rolepermission` |
| 7 | `alibaba.mozi.acl.role.remove.permissions` |
| 8 | `alibaba.mozi.acl.app.getpermisspkgs` |
| 9 | `alibaba.mozi.acl.permissionpkg.add.permissions` |
| 10 | `alibaba.mozi.acl.permissionpkg.add.roles` |
| 11 | `alibaba.mozi.acl.role.remove` |
| 12 | `alibaba.mozi.acl.permisionpkgs.pagetenantpkgs` |
| 13 | `alibaba.mozi.acl.dp.enumpropertyvalue.create` |
| 14 | `alibaba.mozi.acl.dp.enumpropertyvalue.delete` |
| 15 | `alibaba.mozi.acl.dp.enumpropertyvalue.update` |
| 16 | `alibaba.mozi.acl.dp.create` |
| 17 | `alibaba.mozi.acl.dp.operate.update` |
| 18 | `alibaba.mozi.acl.dp.operate.create` |
| 19 | `alibaba.mozi.acl.dp.property.delete` |
| 20 | `alibaba.mozi.acl.dp.property.update` |
| 21 | `alibaba.mozi.acl.dp.property.create` |
| 22 | `alibaba.mozi.acl.dp.datamodel.detele` |
| 23 | `alibaba.mozi.acl.dp.datamodel.update` |
| 24 | `alibaba.mozi.acl.dp.datamodel.create` |
| 25 | `alibaba.mozi.acl.dp.delete` |
| 26 | `alibaba.mozi.acl.dp.update` |
| 27 | `alibaba.mozi.acl.dp.operate.delete` |

</details>

### 飞猪商家平台 (101 APIs)

<details>
<summary>展开查看全部 101 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alitrip.merchant.galaxy.offer.query` |
| 2 | `alitrip.merchant.galaxy.order.validate` |
| 3 | `alitrip.merchant.galaxy.member.register` |
| 4 | `alitrip.merchant.galaxy.member.token` |
| 5 | `alitrip.merchant.galaxy.wechat.login` |
| 6 | `alitrip.merchant.galaxy.member.query` |
| 7 | `alitrip.merchant.galaxy.hotel.list.search` |
| 8 | `alitrip.merchant.galaxy.brand.search` |
| 9 | `alitrip.merchant.galaxy.member.logout` |
| 10 | `alitrip.merchant.galaxy.order.book` |
| 11 | `alitrip.merchant.galaxy.payment.param.query` |
| 12 | `alitrip.merchant.galaxy.member.card` |
| 13 | `alitrip.merchant.galaxy.order.cancel` |
| 14 | `alitrip.merchant.galaxy.order.list.query` |
| 15 | `alitrip.merchant.galaxy.order.query` |
| 16 | `alitrip.merchant.galaxy.hotel.detail.search` |
| 17 | `alitrip.merchant.galaxy.city.list` |
| 18 | `alitrip.merchant.galaxy.city.like` |
| 19 | `alitrip.merchant.galaxy.wechat.info` |
| 20 | `alitrip.merchant.galaxy.share.get` |
| 21 | `alitrip.merchant.galaxy.member.provider.register` |
| 22 | `alitrip.merchant.galaxy.provider.member.query` |
| 23 | `alitrip.merchant.galaxy.query.participate.number` |
| 24 | `alitrip.merchant.galaxy.activity.draw.participate` |
| 25 | `alitrip.merchant.galaxy.query.draw.summary` |
| 26 | `alitrip.merchant.galaxy.activity.popup.query` |
| 27 | `alitrip.merchant.galaxy.activity.address.add` |
| 28 | `alitrip.merchant.galaxy.message.subscription.query` |
| 29 | `alitrip.merchant.galaxy.message.subscription.storage` |
| 30 | `alitrip.merchant.galaxy.activity.fatigue` |
| 31 | `alitrip.merchant.galaxy.activity.goods.query` |
| 32 | `alitrip.merchant.galaxy.activity.popup.control` |
| 33 | `alitrip.merchant.galaxy.activity.marketing.popup` |
| 34 | `alitrip.merchant.galaxy.favorite.list` |
| 35 | `alitrip.merchant.galaxy.favorite.save` |
| 36 | `alitrip.merchant.galaxy.coupon.valid.list` |
| 37 | `alitrip.merchant.galaxy.card.info` |
| 38 | `alitrip.merchant.galaxy.activity.coupon.list` |
| 39 | `alitrip.merchant.galaxy.coupon.invalid.list` |
| 40 | `alitrip.merchant.galaxy.receive.coupon.by.activity` |
| 41 | `alitrip.merchant.galaxy.favorite.query` |
| 42 | `alitrip.merchant.galaxy.hotel.detail.search.data` |
| 43 | `alitrip.merchant.galaxy.order.fill` |
| 44 | `alitrip.merchant.galaxy.order.coupon.validate` |
| 45 | `alitrip.merchant.galaxy.user.risk` |
| 46 | `alitrip.merchant.galaxy.verify.signature` |
| 47 | `alitrip.merchant.galaxy.voucher.query` |
| 48 | `alitrip.merchant.galaxy.voucher.query.list` |
| 49 | `alitrip.merchant.galaxy.order.query.info` |
| 50 | `alitrip.merchant.galaxy.trigger.event` |
| 51 | `alitrip.merchant.galaxy.wechat.card.parm.query` |
| 52 | `alitrip.merchant.galaxy.wechat.card.query.record` |
| 53 | `alitrip.merchant.galaxy.wechat.add.operation.record` |
| 54 | `alitrip.merchant.galaxy.wechat.add.coupon.record` |
| 55 | `alitrip.merchant.galaxy.member.add.agreement` |
| 56 | `alitrip.merchant.galaxy.member.popup.agreement` |
| 57 | `alitrip.merchant.galaxy.member.complete.switch` |
| 58 | `alitrip.merchant.galaxy.member.login.derby` |
| 59 | `alitrip.merchant.galaxy.member.register.derby` |
| 60 | `alitrip.merchant.galaxy.common.get.enumsbyname` |
| 61 | `alitrip.merchant.galaxy.wechat.user.login` |
| 62 | `alitrip.merchant.galaxy.order.query.order.count` |
| 63 | `alitrip.merchant.galaxy.derby.member.voucher.card.query` |
| 64 | `alitrip.merchant.galaxy.derby.member.voucher.card.purchasable.query` |
| 65 | `alitrip.merchant.galaxy.derby.member.voucher.receipt.auto` |
| 66 | `alitrip.merchant.galaxy.derby.member.voucher.receipt.details.query` |
| 67 | `alitrip.merchant.galaxy.derby.member.voucher.receipt.show` |
| 68 | `alitrip.merchant.galaxy.derby.member.voucher.card.order.place` |
| 69 | `alitrip.merchant.galaxy.wechat.pay.callback` |
| 70 | `alitrip.merchant.galaxy.derby.member.voucher.receipt.details.apply` |
| 71 | `alitrip.merchant.galaxy.derby.member.voucher.card.order.details.query` |
| 72 | `alitrip.merchant.galaxy.derby.member.voucher.card.orders.query` |
| 73 | `alitrip.merchant.galaxy.derby.member.voucher.offline.qrcode` |
| 74 | `alitrip.merchant.galaxy.derby.member.voucher.update.status` |
| 75 | `alitrip.merchant.galaxy.derby.member.voucher.card.active` |
| 76 | `alitrip.merchant.galaxy.derby.member.voucher.card.show.qrcode` |
| 77 | `alitrip.merchant.galaxy.derby.member.voucher.card.order.cancel` |
| 78 | `alitrip.merchant.galaxy.derby.member.voucher.query.amount` |
| 79 | `alitrip.merchant.galaxy.derby.member.voucher.card.change.callback` |
| 80 | `alitrip.merchant.galaxy.common.bind.merchant.id` |
| 81 | `alitrip.merchant.galaxy.derby.member.voucher.receipt.details.auto` |
| 82 | `alitrip.merchant.galaxy.derby.member.generate.seller.qrcode` |
| 83 | `alitrip.merchant.galaxy.voucher.generate.scheme.link` |
| 84 | `alitrip.merchant.galaxy.derby.member.voucher.card.redeem.history` |
| 85 | `alitrip.merchant.galaxy.derby.member.voucher.card.redeem` |
| 86 | `alitrip.merchant.galaxy.derby.member.voucher.card.aps.refund` |
| 87 | `alitrip.merchant.galaxy.member.completes.switch` |
| 88 | `alitrip.merchant.galaxy.member.send.code` |
| 89 | `alitrip.merchant.galaxy.derby.voucher.card.unlimited.change.callback` |
| 90 | `alitrip.merchant.galaxy.wechat.data.lottery.query` |
| 91 | `alitrip.merchant.galaxy.wechat.user.modify.phone` |
| 92 | `alitrip.merchant.galaxy.wechat.user.authorize.login` |
| 93 | `alibaba.fliggy.kollive.addkol` |
| 94 | `alibaba.fliggy.kollive.getkol` |
| 95 | `alibaba.fliggy.kollive.writekolcommission` |
| 96 | `alibaba.fliggy.kollive.createorupdateitemsignup` |
| 97 | `alibaba.fliggy.kollive.processapplication` |
| 98 | `alibaba.fliggy.kollive.updateitemsignuppostapproval` |
| 99 | `alibaba.fliggy.kollive.cleanoutitem` |
| 100 | `alibaba.fliggy.kollive.queryitemsignup` |
| 101 | `alibaba.fliggy.kollive.cancelkolcommission` |

</details>

### 新零售POS

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.commdy.posmerchandise.getmerchandise` |
| 2 | `alibaba.mos.commdy.offline.getfileurl` |

### 资质共享API (16 APIs)

<details>
<summary>展开查看全部 16 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.fivee.importproduct.get` |
| 2 | `taobao.fivee.company.upload` |
| 3 | `taobao.fivee.importproduct.publish` |
| 4 | `taobao.fivee.innerproduct.publish` |
| 5 | `taobao.fivee.innerproduct.get` |
| 6 | `taobao.fivee.company.get` |
| 7 | `taobao.kayle.inspection.task.needaccept` |
| 8 | `taobao.kayle.inspection.task.process` |
| 9 | `taobao.kayle.inspection.task.detail` |
| 10 | `taobao.kayle.inspection.task.descenum` |
| 11 | `taobao.kayle.inspection.task.floworderaccept` |
| 12 | `taobao.kayle.inspection.task.backtosupplement` |
| 13 | `taobao.kayle.inspection.task.inspectionresultupload` |
| 14 | `taobao.kayle.inspection.file.pre.upload.url` |
| 15 | `taobao.kayle.inspection.task.needacceptproduct` |
| 16 | `taobao.kayle.inspection.task.processproduct` |

</details>

### 业务平台事业部-税务平台API

| # | API名称 |
|---|--------|
| 1 | `alibaba.tax.invoice.sync` |

### MOZI 租户

| # | API名称 |
|---|--------|
| 1 | `alibaba.mozi.vds.tenant.api.service.addadmin` |
| 2 | `alibaba.mozi.vds.tenant.api.service.removeadmin` |

### 天猫U先API

| # | API名称 |
|---|--------|
| 1 | `tmall.utry.channel.user.certificate.get` |

### 公益三小时公共 (26 APIs)

<details>
<summary>展开查看全部 26 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.charity.useraction.sync` |
| 2 | `alibaba.charity.charitytime.query` |
| 3 | `alibaba.charity.charitytime.list` |
| 4 | `alibaba.charity.user.bind.geturi` |
| 5 | `alibaba.charity.bind.cancel` |
| 6 | `alibaba.charity.user.external.auth` |
| 7 | `alibaba.charity.user.external.auth.cancel` |
| 8 | `alibaba.charity.charitytime.querytime` |
| 9 | `alibaba.charity.charitytime.user.querythirduserhasauth` |
| 10 | `alibaba.charity.charitytime.commonauth` |
| 11 | `alibaba.charity.charitytime.user.cancelauth` |
| 12 | `alibaba.charity.charitytime.user.queryusercharityaccount` |
| 13 | `alibaba.value.coin.issue` |
| 14 | `alibaba.value.user.getid` |
| 15 | `alibaba.csr.donate.seller.invoice.syncinfo` |
| 16 | `alibaba.csr.donate.org.invoice.undraw.list` |
| 17 | `alibaba.csr.donate.org.invoice.reject` |
| 18 | `alibaba.csr.donate.org.invoice.draw` |
| 19 | `alibaba.csr.game.data.sync` |
| 20 | `alibaba.csr.game.data.sync.check` |
| 21 | `alibaba.csr.daomengkongjian.data.query` |
| 22 | `alibaba.charity.charitytime.recorduseractionandsendaward` |
| 23 | `alibaba.csr.cooperate.user.query` |
| 24 | `alibaba.csr.cooperate.activity.query` |
| 25 | `alibaba.csr.external.data.query` |
| 26 | `alibaba.csr.lemoba.cooperate.donate` |

</details>

### 脚模API

| # | API名称 |
|---|--------|
| 1 | `alibaba.footscan.mini.query.mobilereport` |
| 2 | `alibaba.footscan.mini.report.fragment.second` |
| 3 | `alibaba.footscan.mini.report.fragment.first` |

### 阿里健康处方药平台

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.alidoc.drug.store.update` |
| 2 | `alibaba.alihealth.alidoc.drug.store.add` |
| 3 | `alibaba.alihealth.seller.rx.prescription.detail.batchquery` |
| 4 | `alibaba.alihealth.nr.rx.prescription.get` |

### 优酷播控幻影API

| # | API名称 |
|---|--------|
| 1 | `youku.mirage.query.permission` |

### 天猫汽车金融

| # | API名称 |
|---|--------|
| 1 | `tmall.aliauto.independent.app.finance.status.sync` |

### miniapp开放API (24 APIs)

<details>
<summary>展开查看全部 24 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.miniappp.template.instantiate` |
| 2 | `taobao.miniapp.template.instantiate` |
| 3 | `taobao.miniapp.template.update` |
| 4 | `taobao.miniapp.template.onlineapp` |
| 5 | `taobao.miniapp.template.queryapp` |
| 6 | `taobao.miniapp.template.updateapp` |
| 7 | `taobao.miniapp.distribution.items.bind` |
| 8 | `taobao.miniapp.app.seller.config.complete` |
| 9 | `taobao.miniapp.shorturl.create` |
| 10 | `taobao.miniapp.template.offlineapp` |
| 11 | `taobao.miniapp.template.rollback` |
| 12 | `taobao.miniapp.distribution.order.create` |
| 13 | `taobao.miniapp.distribution.order.get` |
| 14 | `taobao.miniapp.distribution.material.get` |
| 15 | `taobao.miniapp.distribution.material.delete` |
| 16 | `taobao.miniapp.distribution.order.precreate` |
| 17 | `taobao.miniapp.distribution.material.update` |
| 18 | `taobao.miniapp.distribution.material.create` |
| 19 | `taobao.miniapp.widget.template.instantiate` |
| 20 | `taobao.miniapp.widget.template.instance.update` |
| 21 | `taobao.miniapp.widget.template.instance.query` |
| 22 | `taobao.miniapp.interact.benefit.item.get` |
| 23 | `taobao.miniapp.virtual.item.get` |
| 24 | `taobao.miniapp.ugc.content.check` |

</details>

### 淘宝闪购联盟广告API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.union.media.zone.add` |
| 2 | `alibaba.alsc.union.media.zone.get` |
| 3 | `alibaba.alsc.union.kbcpx.positive.order.get` |
| 4 | `alibaba.alsc.union.kbcpx.refund.order.get` |
| 5 | `alibaba.alsc.union.kbcpx.punish.order.get` |
| 6 | `alibaba.alsc.union.kb.item.promotion.share.create` |
| 7 | `alibaba.alsc.union.eleme.word.data.get` |
| 8 | `alibaba.alsc.union.eleme.media.report.chaoqiangshou.detail.query` |

### 信息流API

| # | API名称 |
|---|--------|
| 1 | `taobao.feedflow.account.get` |

### 淘宝C2M

| # | API名称 |
|---|--------|
| 1 | `taobao.sebp.organization.getorderinfo` |
| 2 | `taobao.sebp.organization.getinviteinfo` |

### 新零售供应链API (77 APIs)

<details>
<summary>展开查看全部 77 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.ascp.salecategory.query` |
| 2 | `alibaba.ascp.uop.supplier.consignorder.notify.received` |
| 3 | `alibaba.ascp.uop.supplier.consignorder.outofstock.callback` |
| 4 | `alibaba.ascp.uop.supplier.consignorder.cancel.feedback` |
| 5 | `alibaba.ascp.uop.supplier.consignorder.ship` |
| 6 | `alibaba.ascp.uop.supplier.reverseorder.instorage.feedback` |
| 7 | `alibaba.ascp.uop.supplier.reverseorder.create` |
| 8 | `alibaba.ascp.industry.uop.supplier.consignoder` |
| 9 | `alibaba.ascp.industry.icp.query.lbx` |
| 10 | `alibaba.ascp.uop.taobao.presalesorder.create` |
| 11 | `alibaba.ascp.uop.taobao.presalesorder.consignconfirm` |
| 12 | `alibaba.ascp.uop.supplier.reverseorder.instorage.result` |
| 13 | `alibaba.ascp.aic.supplier.aicinventory.publish` |
| 14 | `alibaba.ascp.aic.supplier.aicinventory.channel.inventory.query` |
| 15 | `alibaba.ascp.purchase.price.create` |
| 16 | `alibaba.ascp.presalespackage.consign` |
| 17 | `alibaba.ascp.channel.distributor.price.get` |
| 18 | `alibaba.ascp.channel.distributor.inventory.get` |
| 19 | `alibaba.ascp.channel.distributor.inventory.list.get` |
| 20 | `alibaba.ascp.channel.supplier.product.list` |
| 21 | `alibaba.ascp.channel.supplier.product.detail` |
| 22 | `alibaba.ascp.channel.distributor.product.detail` |
| 23 | `alibaba.ascp.channel.distributor.product.list` |
| 24 | `alibaba.ascp.channel.sub.refund.create` |
| 25 | `alibaba.ascp.channel.sales.order.create` |
| 26 | `alibaba.ascp.channel.main.refund.create` |
| 27 | `alibaba.ascp.channel.refund.goods.waybill` |
| 28 | `taobao.inv.turnover.query` |
| 29 | `alibaba.ascp.uop.supplier.consignorder.notify.tms.change` |
| 30 | `alibaba.ascp.channel.refund.cancel` |
| 31 | `alibaba.ascp.global.supplier.item.list.info.query` |
| 32 | `alibaba.ascp.uop.self.supplier.waybill.query` |
| 33 | `alibaba.ascp.channel.sales.order.confirm` |
| 34 | `alibaba.ascp.channel.distributor.product.distribute` |
| 35 | `alibaba.ascp.channel.supplier.product.auth` |
| 36 | `alibaba.ascp.channel.supplier.product.price.apply` |
| 37 | `alibaba.ascp.channel.refund.close` |
| 38 | `alibaba.ascp.channel.supplier.product.goods.bind` |
| 39 | `alibaba.ascp.industry.waybill.accept` |
| 40 | `alibaba.ascp.industry.launch.extra.charge` |
| 41 | `alibaba.ascp.industry.waybill.pre.accept` |
| 42 | `alibaba.ascp.channel.sales.order.pay` |
| 43 | `alibaba.ascp.industry.supplier.logistics.callback` |
| 44 | `alibaba.ascp.industry.supplier.service.create.callback` |
| 45 | `alibaba.ascp.channel.sales.order.before.check.new` |
| 46 | `alibaba.ascp.industry.supplier.logistics.push.order` |
| 47 | `alibaba.taobao.isv.inventory.future.replenish.query` |
| 48 | `alibaba.ascp.industry.supplier.logistics.modify.order` |
| 49 | `alibaba.ascp.uop.supplier.consignorder.ship.precheck` |
| 50 | `alibaba.ascp.industry.supplier.logistics.action` |
| 51 | `alibaba.ascp.industry.supplier.logistics.verify` |
| 52 | `alibaba.ascp.industry.supplier.logistics.price` |
| 53 | `alibaba.ascp.industry.supplier.logistics.cancel` |
| 54 | `alibaba.dchain.isv.inventory.aic.batch.merchant.sync` |
| 55 | `alibaba.ascp.channel.distributor.product.sync` |
| 56 | `alibaba.ascp.channel.sales.order.render.query` |
| 57 | `alibaba.ascp.channel.sub.refund.render.query` |
| 58 | `alibaba.ascp.channel.sales.order.cancel` |
| 59 | `alibaba.ascp.channel.file.upload` |
| 60 | `alibaba.ascp.channel.oss.credential.get` |
| 61 | `alibaba.ascp.industry.seller.logistics.action` |
| 62 | `alibaba.ascp.channel.sales.order.create.result.query` |
| 63 | `alibaba.ascp.channel.sales.order.base.query` |
| 64 | `alibaba.ascp.channel.refund.compensate.confirm` |
| 65 | `alibaba.ascp.channel.region.sellable.item.query` |
| 66 | `alibaba.ascp.channel.sales.order.logistics.trace.query` |
| 67 | `alibaba.ascp.channel.refund.order.logistics.trace.query` |
| 68 | `alibaba.ascp.onestock.supplier.product.info.query` |
| 69 | `alibaba.ascp.industry.supplier.logistics.service.callback` |
| 70 | `alibaba.ascp.industry.supplier.waybill.add` |
| 71 | `alibaba.ascp.uop.supplier.consignorder.tmsreport` |
| 72 | `alibaba.ascp.channel.distributor.quotation.get` |
| 73 | `alibaba.ascp.channel.sales.order.gw.logistics.order.update` |
| 74 | `alibaba.ascp.channel.refund.agree` |
| 75 | `alibaba.ascp.channel.refund.agree.return.goods` |
| 76 | `alibaba.ascp.channel.refund.refuse` |
| 77 | `alibaba.ascp.channel.receiver.address.sync` |

</details>

### AliOS支付API

| # | API名称 |
|---|--------|
| 1 | `aliyun.alios.pay.token.get` |
| 2 | `aliyun.alios.pay.record.list` |
| 3 | `aliyun.alios.pay.trade.query` |
| 4 | `aliyun.alios.pay.refund` |
| 5 | `aliyun.alios.pay.period.agreement.pay` |
| 6 | `aliyun.alios.pay.period.agreement.unsign` |
| 7 | `aliyun.alios.pay.period.agreement.status.get` |

### 菜鸟控制塔API

| # | API名称 |
|---|--------|
| 1 | `cainiao.ecc.exceptions.delay.get` |
| 2 | `cainiao.ecc.exceptions.delay.count` |

### 群聊开放三方工具API

| # | API名称 |
|---|--------|
| 1 | `taobao.chatting.platform.newuser.user.group.list` |
| 2 | `taobao.chatting.platform.newuser.user.join.group.info` |

### 银泰OPENAPI

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.carnival.open.rights.send` |
| 2 | `alibaba.mos.carnival.tripatitecode.open.bank.issuecode` |
| 3 | `alibaba.mos.carnival.consumption.cash.trade` |

### 小程序API

| # | API名称 |
|---|--------|
| 1 | `yunos.miniapp.activity.call` |
| 2 | `yunos.miniapp.datatunnel.call` |

### 菜鸟末端商业

| # | API名称 |
|---|--------|
| 1 | `cainiao.cntec.shopkeeper.supply.statistics.query` |
| 2 | `cainiao.cntec.locallife.communitylife.syncorderstatus` |
| 3 | `cainiao.cntec.locallife.communitylife.verifyservicecode` |
| 4 | `cainiao.cntec.compass.rpa.exe.resultsave` |
| 5 | `cainiao.cntec.locallife.print.order.sync` |
| 6 | `cainiao.cntec.locallife.print.device.sync` |

### 阿里健康挂号号源直连

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medicalbase.order.status.sync` |

### 千牛业务API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `cainiao.logisticscloud.isv.cpticket.create` |
| 2 | `cainiao.logisticscloud.isv.cpticket.query` |
| 3 | `taobao.message.fuwu.supply.config.state.sync` |
| 4 | `taobao.message.fuwu.event.sync` |
| 5 | `taobao.qianniu.delivery.cprender` |
| 6 | `taobao.qianniu.delivery.agreement.query` |
| 7 | `taobao.qianniu.delivery.alipay.query` |
| 8 | `taobao.qianniu.delivery.submit` |
| 9 | `taobao.qianniu.delivery.agreement.sign` |
| 10 | `taobao.qianniu.delivery.order.query` |
| 11 | `taobao.qianniu.delivery.order.list` |
| 12 | `taobao.qianniu.delivery.order.cancel` |
| 13 | `taobao.qianniu.delivery.order.pay` |
| 14 | `taobao.qianniu.delivery.waitpay.query` |
| 15 | `taobao.qianniu.delivery.config.query` |
| 16 | `taobao.qianniu.delivery.config.update` |
| 17 | `taobao.qianniu.delivery.order.status.query` |

</details>

### AE-UserOpen-Recommend

| # | API名称 |
|---|--------|
| 1 | `aliexpress.usergrowth.search.items.get` |
| 2 | `aliexpress.usergrowth.recommend.items.get` |

### Efficient Tools

| # | API名称 |
|---|--------|
| 1 | `aliexpress.affiliate.link.generate` |

### Data Reports

| # | API名称 |
|---|--------|
| 1 | `aliexpress.affiliate.order.list` |
| 2 | `aliexpress.affiliate.order.get` |
| 3 | `aliexpress.affiliate.order.listbyindex` |

### Promotion Creatives

| # | API名称 |
|---|--------|
| 1 | `aliexpress.affiliate.hotproduct.query` |
| 2 | `aliexpress.affiliate.category.get` |
| 3 | `aliexpress.affiliate.product.query` |
| 4 | `aliexpress.affiliate.product.smartmatch` |
| 5 | `aliexpress.affiliate.productdetail.get` |
| 6 | `aliexpress.affiliate.featuredpromo.get` |
| 7 | `aliexpress.affiliate.featuredpromo.products.get` |
| 8 | `aliexpress.affiliate.hotproduct.download` |
| 9 | `aliexpress.affiliate.image.search` |

### 菜鸟国际出口

| # | API名称 |
|---|--------|
| 1 | `cainiao.global.handover.savedraft` |
| 2 | `cainiao.global.handover.update` |
| 3 | `cainiao.global.handover.cloudprint.get` |
| 4 | `cainiao.global.handover.parcel.query` |
| 5 | `cainiao.global.handover.cancel` |
| 6 | `cainiao.global.handover.commit` |
| 7 | `cainiao.global.handover.content.query` |
| 8 | `cainiao.global.handover.pdf.get` |
| 9 | `cainiao.global.solution.service.resource.query` |
| 10 | `cainiao.global.logistic.order.create` |
| 11 | `cainiao.global.solution.inquiry` |
| 12 | `cainiao.global.logistics.carrier.querylist` |
| 13 | `cainiao.global.commithandovercontent.update` |
| 14 | `cainiao.global.handover.content.subbag.add` |

### 全域会员通

| # | API名称 |
|---|--------|
| 1 | `alibaba.member.sync` |
| 2 | `alibaba.member.checkmerchant` |
| 3 | `alibaba.member.identity.sync` |
| 4 | `alibaba.member.identity.signfinish` |
| 5 | `alibaba.member.identity.rescindfinish` |
| 6 | `alibaba.member.exit` |
| 7 | `alibaba.member.point.change.sync` |
| 8 | `alibaba.member.merchant.level.setting.sync` |
| 9 | `alibaba.member.isv.page.query` |

### 交易猫API (33 APIs)

<details>
<summary>展开查看全部 33 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.jym.member.realname.verify.withoutuid` |
| 2 | `alibaba.jym.industry.vmos.common.callback` |
| 3 | `alibaba.jym.goods.external.goods.vmos.offon.game` |
| 4 | `alibaba.jym.industry.taskswitch.save` |
| 5 | `alibaba.jym.industry.outsidegamepropertysync.syncpropertyinfo` |
| 6 | `alibaba.jym.industry.outsidegamepropertysync.querypropertyinfo` |
| 7 | `alibaba.jym.industry.trade.max.price.get` |
| 8 | `alibaba.jym.industry.recommend.goods.get` |
| 9 | `alibaba.jym.item.external.goods.batch.synoffsale` |
| 10 | `alibaba.jym.steam.refund.audit` |
| 11 | `alibaba.jym.steam.fulfillment.update` |
| 12 | `alibaba.jym.steam.shadowuser.get` |
| 13 | `alibaba.jym.industry.file.upload.apply` |
| 14 | `alibaba.jym.industry.file.upload.signature.get` |
| 15 | `alibaba.jym.industry.cloudgame.session.status.sync` |
| 16 | `alibaba.jym.industry.cloudgame.session.video.sync` |
| 17 | `alibaba.jym.industry.channel.goods.offsales.notify` |
| 18 | `alibaba.jym.industry.channel.account.unbind.notify` |
| 19 | `alibaba.jym.industry.external.captcha.task.update` |
| 20 | `alibaba.jym.industry.cloudgame.game.status.sync` |
| 21 | `alibaba.jym.industry.cloudgame.game.monitor.ocr` |
| 22 | `alibaba.jym.industry.cloudgame.session.proxy.query` |
| 23 | `alibaba.jym.industry.cloudgame.session.proxy.network` |
| 24 | `alibaba.jym.industry.cloudgame.xengine.collectresult.upload` |
| 25 | `alibaba.jym.industry.cloudgame.xengine.status.upload` |
| 26 | `alibaba.jym.industry.cloudgame.game.deploy.sync` |
| 27 | `alibaba.jym.industry.cloudgame.pkg.upgrade.submit` |
| 28 | `alibaba.jym.industry.cloudgame.xengine.status.logintaskupdate` |
| 29 | `alibaba.jym.industry.cloudgame.upgrade.distribute` |
| 30 | `alibaba.jym.servicecenter.mediation.immessage.auth` |
| 31 | `alibaba.jym.servicecenter.mediation.result.push` |
| 32 | `alibaba.jym.servicecenter.mediation.strategy.push` |
| 33 | `alibaba.jym.industry.cloudgame.pkg.upgrade.trigger` |

</details>

### 影城自运营开放Api

| # | API名称 |
|---|--------|
| 1 | `taobao.film.tfavatar.bill.ticket.payment.query` |
| 2 | `taobao.film.tfavatar.bill.sale.print.query` |
| 3 | `taobao.film.tfavatar.bill.sale.refund.query` |
| 4 | `taobao.film.tfavatar.bill.sale.payment.query` |
| 5 | `taobao.film.tfavatar.bill.ticket.refund.query` |
| 6 | `taobao.film.tfavatar.bill.sale.payment.query.vii` |
| 7 | `taobao.film.tfavatar.bill.sale.refund.query.vii` |

### 商家应用云

| # | API名称 |
|---|--------|
| 1 | `taobao.miniapp.cloud.mongo.insert` |
| 2 | `taobao.miniapp.cloud.mongo.update` |
| 3 | `taobao.miniapp.cloud.store.listfile` |

### 国际火车票API

| # | API名称 |
|---|--------|
| 1 | `alitrip.rail.ir.division.get` |
| 2 | `alitrip.rail.ir.carrier.get` |
| 3 | `alitrip.rail.ir.station.get` |
| 4 | `alitrip.rail.trade.issueticket` |
| 5 | `alitrip.rail.trade.closeticket` |
| 6 | `alitrip.rail.ir.service.get` |

### 天猫校园API

| # | API名称 |
|---|--------|
| 1 | `tmall.campus.authstatus.query` |
| 2 | `tmall.campus.retail.iot.devicecontent.list` |
| 3 | `tmall.campus.retail.iot.resourcecontainer.push` |

### 消息API

| # | API名称 |
|---|--------|
| 1 | `alibaba.leg.msg.post` |
| 2 | `alibaba.idle.order.msg.send` |

### 菜鸟发货工作台API

| # | API名称 |
|---|--------|
| 1 | `cainiao.consignplatform.order.cancel` |
| 2 | `cainiao.consignplatform.order.create` |

### 五道口-物流-自提API

| # | API名称 |
|---|--------|
| 1 | `alibaba.wdk.logistics.pus.pickup.cararrived` |

### 船票API

| # | API名称 |
|---|--------|
| 1 | `alitrip.ship.return.notify` |
| 2 | `alitrip.ship.order.notify` |
| 3 | `alitrip.ship.product.syncbase` |
| 4 | `alitrip.ship.product.synccall` |
| 5 | `alitrip.ship.product.syncnunber` |

### 飞猪-综合交通api

| # | API名称 |
|---|--------|
| 1 | `alitrip.rentcar.commodity.stdvehicle.query` |
| 2 | `alitrip.rentcar.commodity.store.change.notify` |
| 3 | `alitrip.rentcar.commodity.store.range.change.notify` |
| 4 | `alitrip.rentcar.commodity.city.change.notify` |
| 5 | `alitrip.rentcar.commodity.store.rule.change.notify` |
| 6 | `alitrip.rentcar.commodity.storevehmodel.addedservice.change.notify` |
| 7 | `alitrip.rentcar.commodity.storevehmodel.base.change.notify` |
| 8 | `alitrip.rentcar.commodity.store.vehicle.change.notify` |
| 9 | `alitrip.rentcar.commodity.company.vehiclemodel.notify` |
| 10 | `alitrip.rentcar.commodity.company.change.notify` |
| 11 | `alitrip.rentcar.zzc.callback.order.create` |
| 12 | `alitrip.rentcar.zzc.callback.order.update` |
| 13 | `alitrip.rentcar.zzc.callback.jointbookinginfo.query` |

### iHome CBD API

| # | API名称 |
|---|--------|
| 1 | `alibaba.ihomefactory.haixun.render.url.get` |
| 2 | `alibaba.ihomefactory.haixun.render.bind` |
| 3 | `alibaba.ihomefactory.haixun.render.order.get` |
| 4 | `alibaba.ihomefactory.haixun.benefit.code.activate` |

### 新零售开放API

| # | API名称 |
|---|--------|
| 1 | `taobao.place.store.itemstore.band` |

### 云游戏API (23 APIs)

<details>
<summary>展开查看全部 23 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.cloudgame.user.mixuserid.check` |
| 2 | `youku.cgame.score.report` |
| 3 | `alibaba.cgame.score.report` |
| 4 | `alibaba.cgame.avatar.userbody.query` |
| 5 | `alibaba.cgame.content.distribution.file.download.update` |
| 6 | `alibaba.cgame.liteplay.avatar.body.query` |
| 7 | `alibaba.cgame.liteplay.avatar.record.report` |
| 8 | `alibaba.cgame.content.distribution.app.deletion.update` |
| 9 | `alibaba.cgame.mp.mpsession.sendmessagetogame` |
| 10 | `alibaba.cgame.mp.mpproject.loginexistaccount` |
| 11 | `alibaba.cgame.mp.mpproject.initnewproject` |
| 12 | `alibaba.cloudgame.interactive.game.room.create` |
| 13 | `alibaba.cloudgame.interactive.game.start` |
| 14 | `alibaba.cloudgame.interactive.game.joincode.assign` |
| 15 | `alibaba.cloudgame.interactive.game.heartbeat` |
| 16 | `alibaba.cloudgame.interactive.game.player.kickout` |
| 17 | `alibaba.cloudgame.interactive.game.player.status.get` |
| 18 | `alibaba.cloudgame.interactive.game.status.get` |
| 19 | `alibaba.cloudgame.interactive.game.player.stop` |
| 20 | `alibaba.cloudgame.interactive.game.room.shutdown` |
| 21 | `alibaba.cloudgame.interactive.game.gamepad.get` |
| 22 | `alibaba.cloudgame.openid.query` |
| 23 | `alibaba.cgame.logitech.game.query` |

</details>

### 国际虚拟API

| # | API名称 |
|---|--------|
| 1 | `alibaba.global.virtual.sendcode` |

### 交易开放

| # | API名称 |
|---|--------|
| 1 | `taobao.opentrade.queue.query` |
| 2 | `taobao.opentrade.queue.users.mark` |
| 3 | `taobao.opentrade.activity.sync` |
| 4 | `taobao.opentrade.activity.query` |
| 5 | `taobao.opentrade.special.users.mark` |
| 6 | `taobao.opentrade.special.users.query` |
| 7 | `taobao.opentrade.special.items.bind` |
| 8 | `taobao.opentrade.special.items.unbind` |
| 9 | `taobao.opentrade.special.items.query` |
| 10 | `taobao.opentrade.special.rule.update` |
| 11 | `taobao.opentrade.tools.items.query` |
| 12 | `taobao.opentrade.tools.items.unbind` |
| 13 | `taobao.opentrade.tools.items.bind` |

### 本地生活商户基础API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.merchant.ext.ticketcode.use` |
| 2 | `alibaba.alsc.merchant.ext.ticketcode.send` |
| 3 | `alibaba.alsc.daodian.ticket.reserve` |
| 4 | `alibaba.alsc.daodian.ticket.consult` |

### 消息amp通道

| # | API名称 |
|---|--------|
| 1 | `taobao.message.send` |
| 2 | `taobao.bc.chat.message.send` |

### 口碑综合体API

| # | API名称 |
|---|--------|
| 1 | `taobao.koubei.mall.common.mall.auth.page` |
| 2 | `taobao.koubei.mall.common.store.comment.page` |
| 3 | `taobao.koubei.mall.common.store.display.goods.list` |
| 4 | `taobao.koubei.mall.common.store.detail.query` |
| 5 | `taobao.koubei.mall.common.store.page` |
| 6 | `taobao.koubei.mall.common.mall.detail.get` |
| 7 | `taobao.koubei.mall.common.mall.near.list` |
| 8 | `taobao.koubei.mall.common.item.shelf.page` |
| 9 | `taobao.koubei.mall.common.item.detail.query` |
| 10 | `taobao.koubei.mall.common.item.super.discount.list` |

### 国际站内容-视频

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbu.video.query` |
| 2 | `alibaba.icbu.video.relation.product.detail` |
| 3 | `alibaba.icbu.video.relation.product.main` |
| 4 | `alibaba.icbu.video.upload` |
| 5 | `alibaba.icbu.video.relation.product.list` |

### IoT售后解决方案API

| # | API名称 |
|---|--------|
| 1 | `cainiao.iot.ticket.sp.comment` |
| 2 | `cainiao.iot.ticket.sp.mail.voucher.upload` |
| 3 | `cainiao.iot.ticket.sp.mail.sign.upload` |
| 4 | `cainiao.iot.ticket.sp.maintain.update` |
| 5 | `cainiao.iot.ticket.detail.query` |
| 6 | `cainiao.iot.ticket.sp.maintain.vtwo.create` |
| 7 | `cainiao.iot.ticket.sp.vtwo.accept` |

### 装企端

| # | API名称 |
|---|--------|
| 1 | `alibaba.decoration.design.info.empty.create.new` |
| 2 | `alibaba.decoration.housetype.image.product.new` |
| 3 | `alibaba.decoration.model.read.obj` |
| 4 | `alibaba.decoration.model.read.fbx` |

### 视觉开放API(viapi)

| # | API名称 |
|---|--------|
| 1 | `aliyun.viapi.imageaudit.scanimage` |
| 2 | `aliyun.viapi.goodstech.classifygoods` |
| 3 | `aliyun.viapi.objectdet.detectobject` |
| 4 | `aliyun.viapi.facebody.compareface` |
| 5 | `aliyun.viapi.facebody.detectface` |
| 6 | `aliyun.viapi.facebody.recognizeface` |
| 7 | `aliyun.viapi.ocr.character` |
| 8 | `aliyun.viapi.imageseg.segmenthead` |
| 9 | `aliyun.viapi.imageseg.segmentcomodity` |
| 10 | `aliyun.viapi.imageseg.segmenthdbody` |
| 11 | `aliyun.viapi.imageseg.segment.commonimage` |
| 12 | `aliyun.viapi.imageaudit.scantext` |
| 13 | `aliyun.viapi.goodstech.recognize.furniturespu` |
| 14 | `aliyun.viapi.goodstech.recognize.furniture.attribute` |

### 曲库开放平台歌曲API

| # | API名称 |
|---|--------|
| 1 | `xiami.content.songs.info.get` |
| 2 | `xiami.content.songs.audio.get` |
| 3 | `xiami.content.songs.info.query` |
| 4 | `xiami.content.songs.audio.getrefrain` |
| 5 | `xiami.content.songs.collect.get` |
| 6 | `xiami.content.album.info.get` |
| 7 | `xiami.content.company.info.get` |
| 8 | `xiami.content.music.info.get` |
| 9 | `xiami.content.music.info.query` |
| 10 | `xiami.content.music.collect.get` |

### 阿里健康三方机构

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.order.query` |
| 2 | `alibaba.alihealth.medical.item.publish` |
| 3 | `alibaba.alihealth.medical.order.refuse` |
| 4 | `alibaba.alihealth.medical.im.data.upload` |
| 5 | `alibaba.alihealth.medical.doctor.msg.send` |
| 6 | `alibaba.alijk.yidong.benefit.card.issue` |
| 7 | `alibaba.alijk.yidong.benefit.card.query` |

### 阿里健康-检测检验-预约

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.lab.item.sync` |
| 2 | `alibaba.alihealth.lab.item.store.relation.sync` |
| 3 | `alibaba.alihealth.lab.item.tbitemsku.relation.sync` |
| 4 | `alibaba.alihealth.lab.store.sync` |

### 天猫精灵供应链网关API (28 APIs)

<details>
<summary>展开查看全部 28 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.tmallgenie.scp.location.get` |
| 2 | `alibaba.tmallgenie.scp.plan.consensus.demand.upload` |
| 3 | `alibaba.tmallgenie.scp.plan.ctom.consensus.demand.upload` |
| 4 | `alibaba.tmallgenie.scp.plan.channel.get` |
| 5 | `alibaba.tmallgenie.scp.plan.sale.qty.get` |
| 6 | `alibaba.tmallgenie.scp.plan.saleforcast.pm.month.upload` |
| 7 | `alibaba.tmallgenie.scp.plan.location.quote.upload` |
| 8 | `alibaba.tmallgenie.scp.plan.netdemand.upload` |
| 9 | `alibaba.tmallgenie.scp.plan.materiel.get` |
| 10 | `alibaba.tmallgenie.scp.plan.current.po.get` |
| 11 | `alibaba.tmallgenie.scp.plan.feedback.oem.upload` |
| 12 | `alibaba.tmallgenie.scp.plan.inventor.qty.get` |
| 13 | `alibaba.tmallgenie.scp.plan.forecast.raw.upload` |
| 14 | `alibaba.tmallgenie.scp.plan.channel.quote.upload` |
| 15 | `alibaba.tmallgenie.scp.plan.forecast.oem.upload` |
| 16 | `alibaba.tmallgenie.scp.plan.feedback.raw.upload` |
| 17 | `alibaba.tmallgenie.scp.plan.mouthfour.upload` |
| 18 | `alibaba.tmallgenie.scp.plan.saleforcast.pm.upload` |
| 19 | `alibaba.tmallgenie.scp.plan.saleforcast.saler.upload` |
| 20 | `alibaba.tmallgenie.scp.plan.sku.supplier.quote.upload` |
| 21 | `alibaba.tmallgenie.scp.plan.correct.supplier.quote.upload` |
| 22 | `alibaba.tmallgenie.scp.plan.summary.sale.qty.get` |
| 23 | `alibaba.tmallgenie.scp.plan.rawpo.gap.return` |
| 24 | `alibaba.tmallgenie.scp.plan.bom.upload` |
| 25 | `alibaba.tmallgenie.scp.plan.correct.supplier.quote.raw.upload` |
| 26 | `alibaba.tmallgenie.scp.plan.netdemand.raw.upload` |
| 27 | `alibaba.tmallgenie.scp.plan.current.rawpo.get` |
| 28 | `alibaba.tmallgenie.scp.plan.material.purchase.attr.get` |

</details>

### 曲库开放平台TraceAPI

| # | API名称 |
|---|--------|
| 1 | `xiami.content.resource.action.report` |

### CRM猎户座前台

| # | API名称 |
|---|--------|
| 1 | `alibaba.crm.customer.tag.judge` |
| 2 | `alibaba.crm.cloudmeeting.clueman.register` |
| 3 | `alibaba.crm.cloudmeeting.meeting.create` |
| 4 | `alibaba.crm.cloudmeeting.interaction.create` |
| 5 | `alibaba.crm.cloudmeeting.meeting.modify` |
| 6 | `alibaba.crm.customer.group.tag.list` |
| 7 | `alibaba.crm.share.clue.create` |
| 8 | `alibaba.crm.share.clueman.create` |

### 飞猪发票

| # | API名称 |
|---|--------|
| 1 | `alitrip.receipt.seller.invoice.return` |
| 2 | `alitrip.receipt.seller.invoice.red` |
| 3 | `alitrip.receipt.issueresult.notify` |

### 同城零售全渠道

| # | API名称 |
|---|--------|
| 1 | `alibaba.perfect.performance.localitem.publish` |
| 2 | `alibaba.perfect.performance.localitem.edit` |
| 3 | `alibaba.tcwms.outbound.pick.receive` |
| 4 | `alibaba.tcwms.outbound.load.container.receive` |
| 5 | `alibaba.tcwms.outbound.order.cancel` |
| 6 | `alibaba.tcwms.outbound.load.boxcode.create` |

### 阿里高德打车API

| # | API名称 |
|---|--------|
| 1 | `taobao.top.latour.coupon.finish` |
| 2 | `taobao.top.latour.coupon.send` |

### 斑马小程序

| # | API名称 |
|---|--------|
| 1 | `yunos.ebanma.miniapp.voicegw.hondacall` |

### 五棱镜任务API

| # | API名称 |
|---|--------|
| 1 | `taobao.pentaprism.task.trigger` |
| 2 | `taobao.pentaprism.task.trigger.from` |

### 零售通交易API

| # | API名称 |
|---|--------|
| 1 | `alibaba.lst.trade.order.get` |

### 零售通结算API

| # | API名称 |
|---|--------|
| 1 | `alibaba.lst.trade.order.fundbill.query` |

### AE任务开放平台

| # | API名称 |
|---|--------|
| 1 | `aliexpress.interactive.task.delivery.query` |
| 2 | `aliexpress.interactive.task.complete` |

### 飞猪玩法平台API

| # | API名称 |
|---|--------|
| 1 | `alitrip.interact.task.report` |
| 2 | `alitrip.fliggy.award.apply` |
| 3 | `alitrip.fliggy.award.user.record.query` |
| 4 | `alitrip.fliggy.coupon.out.status.notify` |

### 本地生活内容API

| # | API名称 |
|---|--------|
| 1 | `alibaba.kbalgo.alscpois.get` |

### 国际化中台服务域保险

| # | API名称 |
|---|--------|
| 1 | `alibaba.middle.claimsaccept.receive` |
| 2 | `alibaba.middle.claimsbill.receive` |
| 3 | `alibaba.middle.claimsresult.receive` |

### 出库实操API

| # | API名称 |
|---|--------|
| 1 | `wdk.ums.outbound.sorting.waveinfoquery` |
| 2 | `wdk.ums.outbound.sorting.taskgroup.pull` |

### 阿里健康-健康证

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.examination.reserve.certificate.notify` |

### 隐私保护API

| # | API名称 |
|---|--------|
| 1 | `taobao.top.oaid.decrypt` |
| 2 | `taobao.top.oaid.client.decrypt` |
| 3 | `taobao.crm.history.ouid.get` |
| 4 | `taobao.crm.history.omid.get` |
| 5 | `taobao.top.package.auth.info.get` |
| 6 | `taobao.top.package.query` |
| 7 | `taobao.top.package.unauth.query` |
| 8 | `taobao.top.package.auth.check` |
| 9 | `taobao.shangou.oaid.decrypt` |
| 10 | `taobao.top.secret.group.query` |
| 11 | `taobao.top.secret.group.update` |

### ICBU-DropShipping

| # | API名称 |
|---|--------|
| 1 | `alibaba.shipping.freight.calculate` |
| 2 | `alibaba.dropshipping.product.get` |
| 3 | `alibaba.dropshipping.token.create` |
| 4 | `alibaba.buynow.order.create` |
| 5 | `alibaba.order.freight.calculate` |
| 6 | `alibaba.order.logistics.tracking.get` |
| 7 | `alibaba.order.pay.result.query` |
| 8 | `alibaba.dropshipping.order.pay` |
| 9 | `alibaba.dropshipping.store.save` |

### 阿里健康保险-信息交互

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.insurance.inst.insure.order.policy.query` |
| 2 | `alibaba.alihealth.insurance.inst.user.rights.use.check` |
| 3 | `alibaba.alihealth.insurance.inst.user.rights.use.notify` |
| 4 | `alibaba.alihealth.insurance.inst.insure.order.info.syn` |
| 5 | `alibaba.alihealth.insurance.inst.miniprogram.qrcode.get` |
| 6 | `alibaba.alihealth.insurance.xl.rights.check` |

### 周期购API

| # | API名称 |
|---|--------|
| 1 | `alibaba.zqs.fulfill.complete` |

### 闲鱼已验货 (21 APIs)

<details>
<summary>展开查看全部 21 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.isv.item.publish` |
| 2 | `alibaba.idle.isv.media.upload` |
| 3 | `alibaba.idle.isv.item.edit` |
| 4 | `alibaba.idle.isv.item.downshelf` |
| 5 | `alibaba.idle.isv.item.query` |
| 6 | `alibaba.idle.isv.spu.search` |
| 7 | `alibaba.idle.isv.order.ship` |
| 8 | `alibaba.idle.isv.refund.query` |
| 9 | `alibaba.idle.isv.user.query` |
| 10 | `alibaba.idle.item.user.publishitems` |
| 11 | `alibaba.idle.isv.order.adjustprice` |
| 12 | `alibaba.idle.isv.order.close` |
| 13 | `alibaba.idle.user.permit.revoke` |
| 14 | `alibaba.idle.user.permit.query` |
| 15 | `alibaba.idle.logistics.companies.query` |
| 16 | `alibaba.idle.isv.user.authorize` |
| 17 | `alibaba.idle.isv.user.info` |
| 18 | `alibaba.idle.isv.fansprice.config` |
| 19 | `alibaba.idle.isv.rate.create` |
| 20 | `alibaba.idle.isv.logistics.resend` |
| 21 | `alibaba.idle.selected.recheck.result.query` |

</details>

### 租户API

| # | API名称 |
|---|--------|
| 1 | `alibaba.databank.open.tenant.syncuser` |

### 阿信-交易API (21 APIs)

<details>
<summary>展开查看全部 21 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.axin.trans.fund.confirm` |
| 2 | `taobao.alitrip.axin.trans.pay.img.upload` |
| 3 | `taobao.alitrip.axin.trans.pay.register.create` |
| 4 | `taobao.alitrip.axin.trans.fund.update` |
| 5 | `taobao.alitrip.axin.trans.fund.add` |
| 6 | `taobao.alitrip.axin.trans.fund.query.by.order` |
| 7 | `taobao.alitrip.axin.trans.refund.create` |
| 8 | `taobao.alitrip.axin.trans.pay.sign.check` |
| 9 | `taobao.alitrip.axin.trans.pay.register.reapply` |
| 10 | `taobao.alitrip.axin.trans.pay.register.audit` |
| 11 | `taobao.alitrip.travel.axin.hotel.order.refund` |
| 12 | `taobao.alitrip.travel.axin.hotel.order.pay` |
| 13 | `taobao.alitrip.travel.axin.hotel.order.create` |
| 14 | `taobao.alitrip.travel.axin.hotel.order.detail` |
| 15 | `taobao.alitrip.travel.axin.hotel.order.validate` |
| 16 | `taobao.alitrip.travel.axin.hotelticket.product.list` |
| 17 | `taobao.alitrip.travel.axin.hotelticket.product.detail` |
| 18 | `taobao.alitrip.travel.axin.hotelticket.order.validate` |
| 19 | `taobao.alitrip.travel.axin.hotelticket.order.createorder` |
| 20 | `taobao.alitrip.travel.axin.hotelticket.refund.orderrefund` |
| 21 | `taobao.alitrip.travel.axin.hotelticket.order.query` |

</details>

### 飞猪商业化API (18 APIs)

<details>
<summary>展开查看全部 18 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alitrip.bp.couponinfo.sync` |
| 2 | `alitrip.bp.channel.crow.query` |
| 3 | `alitrip.bp.ad.exposure.report` |
| 4 | `alitrip.bp.ad.order.report` |
| 5 | `alitrip.bp.ad.click.report` |
| 6 | `alitrip.bp.ad.campaign.create` |
| 7 | `alitrip.bp.ad.campaign.update.time` |
| 8 | `alitrip.bp.ad.campaign.update.status` |
| 9 | `alitrip.bp.ad.campaign.update.budget` |
| 10 | `alitrip.bp.ad.campaign.query` |
| 11 | `alitrip.bp.ad.campaign.budget.sug` |
| 12 | `alitrip.bp.ad.group.query` |
| 13 | `alitrip.bp.ad.group.update` |
| 14 | `alitrip.bp.ad.material.price.sug` |
| 15 | `alitrip.bp.ad.material.update` |
| 16 | `alitrip.bp.ad.campaign.data.get` |
| 17 | `alitrip.bp.ad.campaign.data.batch.get` |
| 18 | `alitrip.bp.ad.campaign.page.query` |

</details>

### 天猫好房交易API

| # | API名称 |
|---|--------|
| 1 | `tmall.alihouse.trade.nhchannel.orderdetail` |
| 2 | `tmall.alihouse.trade.user.oaid.decrypt` |
| 3 | `tmall.alihouse.trade.coupon.order.common.code.exchange` |
| 4 | `tmall.alihouse.trade.order.second.house.operate` |

### MMC中心仓出库实操API

| # | API名称 |
|---|--------|
| 1 | `alibaba.mmc.wms.sorting.bindcontainer` |
| 2 | `alibaba.mmc.wms.sorting.gettaskdetail` |
| 3 | `alibaba.mmc.wms.sorting.callback` |

### 天猫优品

| # | API名称 |
|---|--------|
| 1 | `taobao.tmallbest.invoice.signin.sync` |

### 阿信-基础数据 (29 APIs)

<details>
<summary>展开查看全部 29 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.alitrip.travel.axin.poi.detail.query` |
| 2 | `taobao.alitrip.travel.axin.poi.search` |
| 3 | `taobao.alitrip.travel.axin.hotel.list.get` |
| 4 | `taobao.alitrip.travel.axin.hotel.city.get` |
| 5 | `taobao.alitrip.travel.axin.hotel.price.get` |
| 6 | `taobao.alitrip.travel.fsc.hotel.list.query` |
| 7 | `taobao.alitrip.travel.fsc.hotel.modify.increment` |
| 8 | `taobao.alitrip.travel.axin.hotel.price.batch.get` |
| 9 | `taobao.alitrip.travel.axin.hotel.shid.list.query` |
| 10 | `taobao.alitrip.travel.axin.hotel.detail.query` |
| 11 | `taobao.alitrip.travel.axin.hotel.room.list.query` |
| 12 | `taobao.alitrip.travel.axin.hotel.price.query` |
| 13 | `taobao.alitrip.travel.axin.hotel.match` |
| 14 | `taobao.alitrip.travel.axin.hotel.room.match` |
| 15 | `taobao.alitrip.travel.fsc.route.api.business.area.get` |
| 16 | `taobao.alitrip.travel.fsc.route.api.product.offline` |
| 17 | `taobao.alitrip.travel.fsc.route.api.product.online` |
| 18 | `taobao.alitrip.travel.fsc.route.api.project.close` |
| 19 | `taobao.alitrip.travel.fsc.route.api.project.open` |
| 20 | `taobao.alitrip.travel.fsc.route.api.project.update` |
| 21 | `taobao.alitrip.travel.fsc.route.api.project.inventory.update` |
| 22 | `taobao.alitrip.travel.fsc.route.api.project.add` |
| 23 | `taobao.alitrip.travel.fsc.route.api.product.update` |
| 24 | `taobao.alitrip.travel.fsc.route.api.product.add` |
| 25 | `taobao.alitrip.travel.fsc.route.api.division.apply` |
| 26 | `taobao.alitrip.travel.fsc.route.api.poi.apply` |
| 27 | `taobao.alitrip.travel.fsc.route.api.division.get` |
| 28 | `taobao.alitrip.travel.fsc.route.api.poi.get` |
| 29 | `taobao.alitrip.travel.fsc.route.api.product.label.get` |

</details>

### 阿里健康公益线API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.pw.applynode.update` |
| 2 | `alibaba.alihealth.pw.applynode.updatename` |
| 3 | `alibaba.alihealth.pw.gm.pending.list` |
| 4 | `alibaba.alihealth.pw.gm.detail` |
| 5 | `alibaba.alihealth.pw.gm.audit` |
| 6 | `alibaba.alihealth.pw.gm.ids.list` |
| 7 | `alibaba.alihealth.pw.special.synchronode` |
| 8 | `alibaba.alihealth.pw.special.synchropatientname` |
| 9 | `alibaba.alihealth.pw.special.synchrosms` |
| 10 | `alibaba.alihealth.pw.dingtalk.remind` |

### 鸟潮物流API

| # | API名称 |
|---|--------|
| 1 | `alibaba.niaochao.logistics.coldinfo.get` |

### 银泰开放平台 (42 APIs)

<details>
<summary>展开查看全部 42 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.mosrp.query.open.refundlist` |
| 2 | `alibaba.mos.goods.open.category.findlist` |
| 3 | `alibaba.mos.entryorder.query` |
| 4 | `alibaba.mos.stockout.query` |
| 5 | `alibaba.mos.goods.open.cspu.query` |
| 6 | `alibaba.mos.goods.open.cspu.create` |
| 7 | `alibaba.mos.goods.open.cspu.update` |
| 8 | `alibaba.mos.stockout.create` |
| 9 | `alibaba.mos.entryorder.create` |
| 10 | `alibaba.mos.inventory.search` |
| 11 | `alibaba.mos.tm.open.order.query` |
| 12 | `alibaba.mos.goods.open.spu.save` |
| 13 | `alibaba.mos.goods.open.spu.query` |
| 14 | `alibaba.mos.card.amount.query` |
| 15 | `alibaba.mos.goods.open.sku.create` |
| 16 | `alibaba.mos.card.amount.refund` |
| 17 | `alibaba.mos.card.amount.pay` |
| 18 | `alibaba.mos.goods.open.spu.tmallrelation` |
| 19 | `alibaba.mos.order.delivery.confirm` |
| 20 | `alibaba.mos.order.return.confirm` |
| 21 | `alibaba.mos.inventory.report` |
| 22 | `alibaba.mos.isv.inventory.scroll.query` |
| 23 | `alibaba.mos.virtualinventory.report` |
| 24 | `alibaba.mos.virtual.inventory.query` |
| 25 | `alibaba.mos.order.delivery.modify` |
| 26 | `alibaba.mos.goods.open.itemprops.get` |
| 27 | `alibaba.mos.goods.open.tempropvalues.get` |
| 28 | `alibaba.mos.card.center.merchants.createorder` |
| 29 | `alibaba.mos.card.center.merchants.querychannelorderdetails` |
| 30 | `alibaba.mos.goods.open.price.activity.create` |
| 31 | `alibaba.mos.goods.open.price.activity.setting` |
| 32 | `alibaba.mos.goods.open.price.plan.query` |
| 33 | `alibaba.mos.goods.open.gold.goods.create` |
| 34 | `alibaba.mos.goods.open.cspu.scroll` |
| 35 | `alibaba.mos.fin.pytinvoiceresult.report` |
| 36 | `alibaba.mos.fin.pytredconfirmresult.report` |
| 37 | `alibaba.mos.fin.pytreversalresult.report` |
| 38 | `alibaba.mos.fin.pytoutputinvoice.report` |
| 39 | `alibaba.mos.order.confirm` |
| 40 | `alibaba.mos.trade.order.remote.close` |
| 41 | `alibaba.nt.ntfinanceopen.generaldata.outinnersync` |
| 42 | `alibaba.nt.ntfinanceopen.generaldata.outquery` |

</details>

### 海南离岛对外API

| # | API名称 |
|---|--------|
| 1 | `alibaba.dutyfree.stock.query` |

### 飞猪-菲住联盟

| # | API名称 |
|---|--------|
| 1 | `alitrip.fz.card.out.book` |
| 2 | `alitrip.fz.fire.order.cancel` |
| 3 | `alitrip.fz.fire.order.check` |
| 4 | `alitrip.fz.fire.order.create` |
| 5 | `alitrip.fz.fire.order.query` |
| 6 | `alitrip.fz.rate.query.byid` |
| 7 | `alitrip.fz.fire.rate.query.page` |
| 8 | `alitrip.fz.fire.roomtype.query.page` |
| 9 | `alitrip.fz.fire.hotel.query.page` |

### 自动驾驶API

| # | API名称 |
|---|--------|
| 1 | `alibaba.adlab.business.parcelbooking.address.search` |
| 2 | `alibaba.adlab.business.parcelbooking.rangtime.get` |
| 3 | `alibaba.adlab.business.parcelbooking.order.create` |
| 4 | `alibaba.adlab.business.parcelbooking.package.get` |
| 5 | `alibaba.adlab.business.parcelbooking.order.cancel` |
| 6 | `alibaba.adlab.device.iot.action.callback` |

### MMC五盘货项目

| # | API名称 |
|---|--------|
| 1 | `alibaba.mmc.order.query` |
| 2 | `alibaba.mmc.settle.subsidy.list` |
| 3 | `alibaba.mmc.supplychain.appoint.inbound.cancel` |
| 4 | `alibaba.mmc.supplychain.purchase.adjust` |
| 5 | `alibaba.mmc.supplychain.purchase.adjustconfirm` |

### 逛逛API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.guangguang.content.article.publish` |
| 2 | `taobao.guangguang.content.resource.check` |
| 3 | `taobao.guangguang.content.video.publish` |
| 4 | `taobao.guangguang.content.resource.upload` |
| 5 | `taobao.guangguang.content.item.source.search` |
| 6 | `taobao.guangguang.content.topic.group.list` |
| 7 | `taobao.guangguang.content.video.uploadcomplete` |
| 8 | `taobao.guangguang.content.brand.search` |
| 9 | `taobao.guangguang.content.topic.search` |
| 10 | `taobao.guangguang.content.item.search` |
| 11 | `taobao.guangguang.content.topic.list` |
| 12 | `taobao.guangguang.content.video.uploadinit` |
| 13 | `taobao.guangguang.content.image.upload` |
| 14 | `taobao.guangguang.content.delete` |
| 15 | `taobao.guangguang.creation.hd.query` |
| 16 | `taobao.guangguang.content.relation.id.get` |
| 17 | `taobao.guangguang.content.item.recommend` |

</details>

### 书旗内容文巢 (28 APIs)

<details>
<summary>展开查看全部 28 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.shuqi.content.backend.correct.chapter.content` |
| 2 | `alibaba.shuqi.content.backend.correct.replace.online` |
| 3 | `alibaba.shuqi.content.backend.correct.chapter.list` |
| 4 | `alibaba.shuqi.content.backend.correct.create` |
| 5 | `alibaba.shuqi.backend.correct.list` |
| 6 | `alibaba.shuqi.content.backend.correct.user.info` |
| 7 | `alibaba.shuqi.content.backend.correct.content.save` |
| 8 | `alibaba.shuqi.content.backend.correct.chapter.info` |
| 9 | `alibaba.shuqi.content.backend.correct.record` |
| 10 | `alibaba.shuqi.content.backend.correct.reset` |
| 11 | `alibaba.shuqi.content.backend.correct.task.delete` |
| 12 | `alibaba.shuqi.content.backend.correct.cp.reader.list` |
| 13 | `alibaba.shuqi.content.backend.correct.condition.list` |
| 14 | `alibaba.shuqi.content.backend.tool.author.migrate` |
| 15 | `alibaba.shuqi.content.backend.tool.author.bookinfo` |
| 16 | `alibaba.shuqi.content.backend.low.quality.list` |
| 17 | `alibaba.shuqi.content.backend.cpsetting.new.list` |
| 18 | `alibaba.shuqi.content.backend.cp.create` |
| 19 | `alibaba.shuqi.content.backend.cpsetting.new.checkinterface` |
| 20 | `alibaba.shuqi.content.backend.cpsetting.new.save` |
| 21 | `alibaba.shuqi.content.backend.cpsetting.sync.key` |
| 22 | `alibaba.shuqi.content.backend.cpsetting.encrypt.rule` |
| 23 | `alibaba.shuqi.content.backend.cpsetting.update.level` |
| 24 | `alibaba.shuqi.content.backend.cpsetting.new.info` |
| 25 | `alibaba.shuqi.content.backend.bookai.selections.list` |
| 26 | `alibaba.shuqi.content.backend.book.foreword.list` |
| 27 | `alibaba.shuqi.content.backend.book.foreword.upsert` |
| 28 | `alibaba.shuqi.content.backend.book.foreword.detail` |

</details>

### 海外-淘宝客API

| # | API名称 |
|---|--------|
| 1 | `taobao.ovs.tbk.shop.get` |
| 2 | `taobao.ovs.tbk.tpwd.create` |
| 3 | `taobao.ovs.tbk.order.details.get` |
| 4 | `taobao.ovs.tbk.order.details.batch.get` |
| 5 | `taobao.ovs.tbk.favitem.get` |
| 6 | `taobao.ovs.tbk.settle.order.details.get` |
| 7 | `taobao.ovs.tbk.material.item.link.convert` |
| 8 | `taobao.ovs.tbk.material.item.optional` |
| 9 | `taobao.ovs.tbk.material.item.info.get` |
| 10 | `taobao.ovs.tbk.material.item.recommend` |
| 11 | `taobao.ovs.tbk.general.link.parse` |

### mos-hr-员工

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.user.list.search` |

### 银泰开放平台(内部)

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.current.bill.query` |
| 2 | `alibaba.mos.current.settlement.bill.create` |
| 3 | `alibaba.mos.current.receivable.bill.create` |
| 4 | `alibaba.mos.current.bill.querybyno` |
| 5 | `alibaba.mos.trade.open.haiding.order.sync` |
| 6 | `alibaba.mos.current.charge.bill.create` |
| 7 | `alibaba.mos.current.settlement.bill.delete` |
| 8 | `alibaba.nt.ntfinanceopen.generaldata.query` |
| 9 | `alibaba.nt.ntfinanceopen.generaldata.innersync` |

### 乌鸫API

| # | API名称 |
|---|--------|
| 1 | `alibaba.wudong.genie.mydevice.list` |
| 2 | `alibaba.wudong.genie.mydevice.count` |
| 3 | `alibaba.wudong.genie.roleservice.roleinfo` |
| 4 | `alibaba.wudong.genie.roleservice.rolelist` |
| 5 | `alibaba.wudong.genie.roleservice.saveresponsible` |
| 6 | `alibaba.wudong.genie.roleservice.saverole` |
| 7 | `alibaba.wudong.genie.roleservice.editrole` |
| 8 | `alibaba.wudong.genie.roleservice.deleterole` |
| 9 | `alibaba.wudong.genie.roleservice.getrole` |

### 阿里健康-本地医疗-青少年健康 (16 APIs)

<details>
<summary>展开查看全部 16 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.adolescent.health.service.item.get` |
| 2 | `alibaba.alihealth.adolescent.health.exam.tasks.list.get` |
| 3 | `alibaba.alihealth.adolescent.health.exam.paper.get` |
| 4 | `alibaba.alihealth.adolescent.health.exam.material.list.get` |
| 5 | `alibaba.alihealth.adolescent.health.exam.result.get` |
| 6 | `alibaba.alihealth.adolescent.health.exam.complete.submit` |
| 7 | `alibaba.alihealth.adolescent.health.doctor.list.get` |
| 8 | `alibaba.alihealth.adolescent.health.record.add` |
| 9 | `alibaba.alihealth.adolescent.health.record.update` |
| 10 | `alibaba.alihealth.adolescent.health.record.all.query` |
| 11 | `alibaba.alihealth.adolescent.health.record.delete` |
| 12 | `alibaba.alihealth.adolescent.health.alihealthuserid.get` |
| 13 | `alibaba.alihealth.adolescent.health.userrecord.get` |
| 14 | `alibaba.alihealth.adolescent.health.card.invalid` |
| 15 | `alibaba.alihealth.adolescent.user.unbinding.update` |
| 16 | `alibaba.alihealth.adolescent.dingtalk.campus.list.get` |

</details>

### 阿里健康-本地医疗-通用预约服务 (18 APIs)

<details>
<summary>展开查看全部 18 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.reservation.keep.appointment.finish` |
| 2 | `alibaba.alihealth.medical.reservation.confirm` |
| 3 | `alibaba.alihealth.medical.reservation.reject` |
| 4 | `alibaba.alihealth.medical.reservation.cancel` |
| 5 | `alibaba.alihealth.medical.reservation.cancellation.confirm` |
| 6 | `alibaba.alihealth.medical.reservation.cancellation.reject` |
| 7 | `alibaba.alihealth.medical.reservation.modification.confirm` |
| 8 | `alibaba.alihealth.medical.report.customer.report.sync` |
| 9 | `alibaba.alihealth.medical.reservation.modification.reject` |
| 10 | `alibaba.alihealth.medical.cargo.sync` |
| 11 | `alibaba.alihealth.medical.cargo.suitableitemskus.query` |
| 12 | `alibaba.alihealth.medical.cargo.itemsku.supply` |
| 13 | `alibaba.alihealth.medical.cargo.itemsku.supply.withdraw` |
| 14 | `alibaba.alihealth.examination.lab.order.status.sync` |
| 15 | `alibaba.alihealth.examination.lab.order.query` |
| 16 | `alibaba.alihealth.lab.reservation.lab.report.sync` |
| 17 | `alibaba.alihealth.lab.reservation.lab.sample.sign` |
| 18 | `alibaba.alihealth.lab.reservation.lab.order.ship` |

</details>

### MMC店仓项目

| # | API名称 |
|---|--------|
| 1 | `alibaba.mmc.inventory.increment.synchronous` |

### 自动驾驶内部API

| # | API名称 |
|---|--------|
| 1 | `aliyun.adlab.fault.inject.getcaseinfo` |
| 2 | `aliyun.adlab.fault.inject.uploadtaskinfo` |

### MTP项目

| # | API名称 |
|---|--------|
| 1 | `alibaba.mtp.supplychain.inboundcallback` |
| 2 | `alibaba.mtp.supplychain.inbound.partcallback` |
| 3 | `alibaba.mtp.supplychain.capacity.sync` |
| 4 | `alibaba.mtp.supplychain.querycheck.appointment` |
| 5 | `alibaba.mtp.supplychain.appointment.confirm` |
| 6 | `alibaba.mtp.supplychain.appointment.update` |
| 7 | `alibaba.mtp.supplychain.inboundorder.print` |
| 8 | `alibaba.mtp.supplychain.delivery.driver.bind` |
| 9 | `alibaba.mtp.supplychain.diff.callback` |

### IT智慧园区

| # | API名称 |
|---|--------|
| 1 | `alibaba.it.campus.reception.place.like.list` |
| 2 | `alibaba.it.campus.reception.tenant.save` |
| 3 | `alibaba.it.campus.reception.tenant.update` |
| 4 | `alibaba.it.campus.reception.tenant.pagelist` |
| 5 | `alibaba.it.campus.reception.tenant.like.list` |
| 6 | `alibaba.it.campus.reception.place.save` |
| 7 | `alibaba.it.campus.reception.place.update` |
| 8 | `alibaba.it.campus.reception.place.delete` |
| 9 | `alibaba.it.campus.reception.place.pagelist` |

### 千帆计划

| # | API名称 |
|---|--------|
| 1 | `tmall.ovs.delivery.order.info.send` |
| 2 | `tmall.ovs.delivery.package.info.send` |
| 3 | `tmall.ovs.delivery.order.tracking.node.send` |
| 4 | `tmall.ovs.logistic.order.create.send` |
| 5 | `tmall.ovs.delivery.package.good.logistics.property.send` |
| 6 | `tmall.ovs.delivery.package.goods.logistics.dimension.send` |
| 7 | `tmall.ovs.delivery.package.goods.logistics.dimension.send.check` |
| 8 | `tmall.ovs.delivery.package.unknown.import` |
| 9 | `tmall.ovs.delivery.package.reject` |
| 10 | `tmall.ovs.delivery.package.second.order.tracking.send` |
| 11 | `tmall.ovs.delivery.package.pick.up.way.send` |

### 阿里健康孔雀翎WMS

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.cep.wms.receivement.callback` |
| 2 | `alibaba.health.cep.wms.shipment.callback` |
| 3 | `alibaba.health.cep.wms.transfer.save` |
| 4 | `alibaba.health.cep.wms.inventory.save` |

### 飞猪交易平台API

| # | API名称 |
|---|--------|
| 1 | `taobao.fplatform.order.get` |

### 阿里健康-本地医疗-通用渠道 (20 APIs)

<details>
<summary>展开查看全部 20 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.channel.store.info.query` |
| 2 | `alibaba.alihealth.medical.channel.item.info.query` |
| 3 | `alibaba.alihealth.medical.channel.order.create` |
| 4 | `alibaba.alihealth.medical.channel.order.pay` |
| 5 | `alibaba.alihealth.medical.channel.order.cancel` |
| 6 | `alibaba.alihealth.medical.channel.order.refund.apply` |
| 7 | `alibaba.alihealth.medical.channel.order.pay.check` |
| 8 | `alibaba.alihealth.medical.channel.inventory.calendar.query` |
| 9 | `alibaba.alihealth.medical.channel.inventory.timeslice.query` |
| 10 | `alibaba.alihealth.medical.channel.reservation.modify` |
| 11 | `alibaba.alihealth.medical.channel.report.query` |
| 12 | `alibaba.alihealth.medical.channel.order.query` |
| 13 | `alibaba.alihealth.medical.channel.detection.reservation.cancel` |
| 14 | `alibaba.alihealth.medical.channel.detection.reservation.submit` |
| 15 | `alibaba.alihealth.medical.channel.detection.refund.apply` |
| 16 | `alibaba.alihealth.medical.channel.detection.inventory.query` |
| 17 | `alibaba.alihealth.medical.channel.detection.store.query` |
| 18 | `alibaba.alihealth.medical.channel.detection.barcode.bind` |
| 19 | `alibaba.alihealth.medical.channel.detection.report.query` |
| 20 | `alibaba.alihealth.medical.channel.detection.reservation.query` |

</details>

### 天猫校园共享前端类目 (64 APIs)

<details>
<summary>展开查看全部 64 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.xiaoyuan.share.ride.campus.relation.get` |
| 2 | `tmall.xiaoyuan.share.ride.order.refund.create` |
| 3 | `tmall.xiaoyuan.share.ride.order.appeal.update` |
| 4 | `tmall.xiaoyuan.share.ride.order.appeal.check` |
| 5 | `tmall.xiaoyuan.share.ride.order.price.change` |
| 6 | `tmall.xiaoyuan.share.ride.order.status.get` |
| 7 | `tmall.xiaoyuan.share.ride.async.item.create` |
| 8 | `tmall.xiaoyuan.share.ride.on.shelf.check` |
| 9 | `tmall.xiaoyuan.share.ride.order.create` |
| 10 | `tmall.xiaoyuan.share.ride.order.detail.list.get` |
| 11 | `tmall.xiaoyuan.share.ride.unlock` |
| 12 | `tmall.xiaoyuan.share.base.query.account.info.by.campus` |
| 13 | `tmall.xiaoyuan.share.isv.campus.area.get` |
| 14 | `tmall.xiaoyuan.share.isv.relation.online.get` |
| 15 | `tmall.xiaoyuan.share.isv.res.on.shelf.check` |
| 16 | `tmall.xiaoyuan.share.isv.order.create` |
| 17 | `tmall.xiaoyuan.share.isv.order.status.get` |
| 18 | `tmall.xiaoyuan.share.isv.order.refund` |
| 19 | `tmall.xiaoyuan.share.isv.order.closed` |
| 20 | `tmall.xiaoyuan.share.isv.order.appeal.check` |
| 21 | `tmall.xiaoyuan.share.isv.order.began` |
| 22 | `tmall.xiaoyuan.share.isv.order.price.change` |
| 23 | `tmall.xiaoyuan.share.isv.order.appeal.update` |
| 24 | `tmall.xiaoyuan.share.isv.order.free.check` |
| 25 | `tmall.campus.share.area.list.query` |
| 26 | `tmall.campus.share.building.list.query` |
| 27 | `tmall.campus.share.device.report` |
| 28 | `tmall.campus.share.weilai.device.insert` |
| 29 | `tmall.campus.share.user.card.sync` |
| 30 | `tmall.campus.share.isv.order.query` |
| 31 | `tmall.campus.share.isv.gmv.detail.query` |
| 32 | `tmall.xiaoyuan.share.isv.user.verified` |
| 33 | `alibaba.campus.out.account.wl.bind.callback` |
| 34 | `tmall.xiaoyuan.share.isv.file.get` |
| 35 | `tmall.xiaoyuan.share.isv.query.user.verified` |
| 36 | `tmall.campus.share.isv.recharge.order.query` |
| 37 | `tmall.xiaoyuan.share.isv.campus.device.bind` |
| 38 | `tmall.xiaoyuan.share.isv.campus.user.get` |
| 39 | `tmall.xiaoyuan.share.isv.campus.device.model.list.query` |
| 40 | `tmall.xiaoyuan.share.isv.campus.device.report` |
| 41 | `tmall.xiaoyuan.share.isv.campus.device.stop` |
| 42 | `tmall.xiaoyuan.share.isv.campus.device.boot` |
| 43 | `tmall.xiaoyuan.share.isv.campus.device.attr.query` |
| 44 | `tmall.xiaoyuan.share.isv.campus.device.info.query` |
| 45 | `tmall.xiaoyuan.share.isv.campus.device.unbind` |
| 46 | `tmall.xiaoyuan.share.isv.campus.device.info.update` |
| 47 | `tmall.xiaoyuan.share.isv.campus.order.fulfil` |
| 48 | `tmall.xiaoyuan.share.income.stat` |
| 49 | `tmall.xiaoyuan.share.isv.pay.order.callback` |
| 50 | `tmall.xiaoyuan.share.isv.campus.user.bind.info.get` |
| 51 | `tmall.xiaoyuan.share.isv.campus.activity.instance.list` |
| 52 | `tmall.xiaoyuan.share.isv.campus.send.sms` |
| 53 | `tmall.xiaoyuan.share.isv.campus.activity.issue.benefits` |
| 54 | `tmall.xiaoyuan.share.isv.campus.wallet.allocation.gift.amount` |
| 55 | `tmall.xiaoyuan.share.isv.campus.fund.withdraw.audit.list` |
| 56 | `tmall.xiaoyuan.share.isv.campus.phone.query` |
| 57 | `tmall.xiaoyuan.share.isv.campus.fund.accredit.list` |
| 58 | `tmall.xiaoyuan.share.isv.campus.fund.take.back.gift` |
| 59 | `tmall.xiaoyuan.share.isv.campus.fund.max.gift.amount` |
| 60 | `tmall.xiaoyuan.share.isv.campus.wallet.withdraw.confirm` |
| 61 | `tmall.xiaoyuan.share.isv.campus.user.wallet.list` |
| 62 | `tmall.xiaoyuan.share.isv.campus.wallet.withdraw.render` |
| 63 | `tmall.xiaoyuan.share.isv.campus.user.fund.order.list` |
| 64 | `tmall.xiaoyuan.share.isv.campus.message.push` |

</details>

### 淘宝闪购联盟-单店推广API (22 APIs)

<details>
<summary>展开查看全部 22 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.union.eleme.promotion.storepromotion.query` |
| 2 | `alibaba.alsc.union.eleme.promotion.storepromotion.get` |
| 3 | `alibaba.alsc.union.eleme.promotion.officialactivity.get` |
| 4 | `alibaba.alsc.union.promotion.link.analyze` |
| 5 | `alibaba.alsc.union.eleme.media.activity.coupon.send` |
| 6 | `alibaba.alsc.union.eleme.promotion.itempromotion.query` |
| 7 | `alibaba.alsc.union.eleme.promotion.itempromotion.get` |
| 8 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.stock.release` |
| 9 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.stock.lock` |
| 10 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.detail.get` |
| 11 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.query` |
| 12 | `alibaba.alsc.union.eleme.tool.order.attrbute.check` |
| 13 | `alibaba.alsc.union.eleme.promotion.itempromotion.store.query` |
| 14 | `alibaba.alsc.union.eleme.promotion.storepromotion.batch.get` |
| 15 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.bind.link.get` |
| 16 | `alibaba.alsc.union.eleme.promotion.otherchannel.get` |
| 17 | `alibaba.alsc.union.eleme.storepromotion.reviewbwc.diagnose` |
| 18 | `alibaba.alsc.union.eleme.promotion.retail.itempromotion.get` |
| 19 | `alibaba.alsc.union.eleme.promotion.retail.itempromotion.query` |
| 20 | `alibaba.alsc.union.eleme.promotion.officialactivity.wxscheme` |
| 21 | `alibaba.alsc.union.commission.future.rate.query` |
| 22 | `alibaba.alsc.union.commission.rate.query` |

</details>

### 阿里健康-本地医疗-通用订单服务

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.order.realtime.get` |

### 蚂蚁采购

| # | API名称 |
|---|--------|
| 1 | `alibaba.ant.pur.basket.merge` |
| 2 | `alibaba.ant.pur.product.sync` |
| 3 | `alibaba.ant.pur.pr.create` |

### 阿里健康-消费医疗-电子凭证服务

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.evoucher.paymentvoucher.get` |
| 2 | `alibaba.alihealth.medical.evoucher.paymentvoucher.redeem` |

### 阿里健康-消费医疗-商品门店服务

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.item.sku.mutualrelation.sync` |
| 2 | `alibaba.alihealth.medical.store.sync` |
| 3 | `alibaba.alihealth.medical.item.onsale` |
| 4 | `alibaba.alihealth.medical.item.offsale` |
| 5 | `alibaba.alihealth.medical.item.sync` |

### 洞窝_api

| # | API名称 |
|---|--------|
| 1 | `alibaba.crowdsourcing.ai.material.get` |

### 代发管理

| # | API名称 |
|---|--------|
| 1 | `taobao.daifa.distributor.order.query` |
| 2 | `taobao.daifa.order.distribute` |
| 3 | `taobao.daifa.supplier.order.query` |
| 4 | `taobao.daifa.distributor.role.get` |
| 5 | `taobao.daifa.distributor.bind` |
| 6 | `taobao.daifa.distributor.bind.rela.query` |
| 7 | `taobao.daifa.supplier.order.consign` |
| 8 | `taobao.daifa.supplier.role.get` |
| 9 | `taobao.daifa.supplier.bind` |
| 10 | `taobao.daifa.supplier.bind.rela.query` |
| 11 | `taobao.daifa.distributor.order.cancel` |
| 12 | `taobao.daifa.userinfo.update` |
| 13 | `taobao.top.distribution.upload` |
| 14 | `taobao.top.distribution.oaid.decrypt` |

### 补发场景

| # | API名称 |
|---|--------|
| 1 | `taobao.reissue.consign` |
| 2 | `taobao.reissue.fail.sync` |

### 天猫校园零售 (40 APIs)

<details>
<summary>展开查看全部 40 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `tmall.campus.retail.categroy.forest.query` |
| 2 | `tmall.campus.retail.marketing.activity.item.promotion.add` |
| 3 | `tmall.campus.retail.marketing.activity.item.promotion.update` |
| 4 | `tmall.campus.retail.marketing.detail.item.promotion.add` |
| 5 | `tmall.campus.retail.marketing.detail.item.promotion.update` |
| 6 | `tmall.campus.retail.marketing.detail.delete` |
| 7 | `tmall.campus.retail.marketing.activity.delete` |
| 8 | `tmall.campus.retail.marketing.remain.num.get` |
| 9 | `tmall.campus.retail.marketing.detail.item.promotion.list` |
| 10 | `tmall.campus.retail.item.query` |
| 11 | `tmall.campus.retail.offline.main.item.publish` |
| 12 | `tmall.campus.retail.offline.sub.item.publish` |
| 13 | `tmall.campus.retail.item.update` |
| 14 | `tmall.campus.retail.store.query` |
| 15 | `tmall.campus.retail.employee.query` |
| 16 | `tmall.campus.retail.brand.query.one` |
| 17 | `tmall.campus.retail.brand.query.keyword` |
| 18 | `tmall.campus.retail.marketing.activity.shop.promotion.add` |
| 19 | `tmall.campus.retail.marketing.activity.shop.promotion.update` |
| 20 | `tmall.campus.retail.marketing.detail.shop.promotion.add` |
| 21 | `tmall.campus.retail.marketing.detail.shop.promotion.update` |
| 22 | `tmall.campus.retail.marketing.detail.shop.participates.add` |
| 23 | `tmall.campus.retail.online.main.item.publish` |
| 24 | `tmall.campus.retail.brand.query` |
| 25 | `tmall.campus.retail.tp.non.standard.prefix.push` |
| 26 | `tmall.campus.retail.offline.storeitem.publish` |
| 27 | `tmall.campus.retail.offline.storeitem.publishquery` |
| 28 | `tmall.campus.retail.offline.storeitem.publishretry` |
| 29 | `tmall.campus.retail.offline.storeitem.publishresetretry` |
| 30 | `tmall.campus.retail.item.publish.offline.sub` |
| 31 | `tmall.campus.retail.item.publish.offline.main` |
| 32 | `tmall.campus.retail.offline.storeitem.modify` |
| 33 | `tmall.campus.retail.invoice.create` |
| 34 | `tmall.campus.retail.marketing.crowd.list.get` |
| 35 | `tmall.campus.retail.item.img.query` |
| 36 | `tmall.campus.retail.online.item.category.create.modify` |
| 37 | `tmall.campus.retail.online.item.create.modify` |
| 38 | `tmall.campus.inventory.retail.item.transfer` |
| 39 | `tmall.campus.retail.item.img.push` |
| 40 | `tmall.campus.retail.item.img.batch.query` |

</details>

### 阿里健康&一树-孔雀翎WMS

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.ys.cep.wms.receivement.callback` |
| 2 | `alibaba.health.ys.cep.wms.shipment.callback` |
| 3 | `alibaba.health.ys.cep.wms.transfer.save` |
| 4 | `alibaba.health.ys.cep.wms.inventory.save` |

### MMC物流域项目

| # | API名称 |
|---|--------|
| 1 | `alibaba.mmc.logistics.gethumanlabors` |
| 2 | `alibaba.mmc.logistics.getupdatehumanlabors` |
| 3 | `alibaba.mmc.logistics.gethumanattendance` |
| 4 | `alibaba.mmc.logistics.addhumanlabors` |
| 5 | `alibaba.mmc.logistics.modifyhumanlabors` |
| 6 | `alibaba.mmc.logistics.addhumanattendance` |

### 淘宝互动平台开放招募

| # | API名称 |
|---|--------|
| 1 | `taobao.interaction.avatar.query` |
| 2 | `taobao.interaction.tblife.user.info.get` |
| 3 | `taobao.interaction.tblife.user.info.query` |
| 4 | `taobao.interaction.tblife.user.figure.get` |
| 5 | `taobao.interaction.tblife.shop.item.buy` |
| 6 | `taobao.interaction.tblife.shop.item.list` |
| 7 | `taobao.interaction.tblife.user.figure.query` |
| 8 | `taobao.taolife.user.required.confirm` |

### 点淘API

| # | API名称 |
|---|--------|
| 1 | `taobao.livex.anchorfavorite.activity.report` |
| 2 | `taobao.livex.anchorfavorite.activity.username.check` |
| 3 | `taobao.livex.anchorfavorite.accountname.check` |
| 4 | `taobao.livex.anchorfavorite.benefit.issue` |

### 我的小窝玩法前端类目

| # | API名称 |
|---|--------|
| 1 | `tmall.alihouse.marketing.userpoint.get` |
| 2 | `tmall.alihouse.marketing.userinfo.init` |
| 3 | `tmall.alihouse.marketing.points.add` |
| 4 | `tmall.alihouse.marketing.threepoints.get` |
| 5 | `tmall.alihouse.marketing.areahouses.list` |
| 6 | `tmall.alihouse.marketing.areas.unlock` |
| 7 | `tmall.alihouse.marketing.houses.delete` |
| 8 | `tmall.alihouse.marketing.houses.build` |
| 9 | `tmall.alihouse.marketing.houses.upgrade` |
| 10 | `tmall.alihouse.marketing.sencecoin.send` |
| 11 | `tmall.alihouse.marketing.aldconfig.get` |
| 12 | `tmall.alihouse.marketing.interact.challengeinfo.get` |
| 13 | `tmall.alihouse.marketing.interact.challengebaseinfo.get` |
| 14 | `tmall.alihouse.marketing.interact.crowd.filter` |

### 盒马航头仓

| # | API名称 |
|---|--------|
| 1 | `taobao.wdk.ums.inbound.save.pallet` |
| 2 | `wdk.ums.inbound.unbind.pallet` |

### 阿里健康&一树-电商中台对接

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.ys.cep.trade.orderdetails.getbyorderdetails` |
| 2 | `alibaba.health.ys.cep.trade.orderdetails.getorderdetails` |

### 猫超卡活动API

| # | API名称 |
|---|--------|
| 1 | `tmall.card.activity.lifecycle.notify` |
| 2 | `tmall.supermarket.card.benefits.issue` |

### 瓴羊客服云

| # | API名称 |
|---|--------|
| 1 | `aliyun.ly.alime.user.accesstoken.get` |

### 飞猪推广平台

| # | API名称 |
|---|--------|
| 1 | `alibaba.fliggy.cps.coupon.offer` |
| 2 | `alibaba.fliggy.cps.coupon.issue` |
| 3 | `alibaba.fliggy.promote.promotion.position.create` |
| 4 | `alibaba.fliggy.promote.activity.link` |
| 5 | `alibaba.fliggy.promote.orders.newlist` |
| 6 | `alibaba.fliggy.promote.hotel.list` |
| 7 | `alibaba.fliggy.promote.hotel.details` |
| 8 | `alibaba.fliggy.promote.hotel.offline` |
| 9 | `alibaba.fliggy.promote.hotel.online` |
| 10 | `alibaba.fliggy.promote.hotel.fetch` |
| 11 | `alibaba.fliggy.wx.order.details` |
| 12 | `alibaba.fliggy.promote.crowd.query` |

### 斑马新能源充电互联互通接口Api

| # | API名称 |
|---|--------|
| 1 | `yunos.charge.pnp.auth.update` |
| 2 | `yunos.charge.pnp.start.charge` |

### 阿里健康-消费医疗-保险合作

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.insurance.policy.sync` |
| 2 | `alibaba.alihealth.medical.insurance.claim.settlement.record.query` |
| 3 | `alibaba.alihealth.medical.insuracne.policy.claim.settlement.close` |
| 4 | `alibaba.alihealth.medical.insurance.claim.settlement.apply` |
| 5 | `alibaba.alihealth.medical.insurance.claim.settlement.info.query` |
| 6 | `alibaba.alihealth.medical.insurance.claim.settlement.info.update` |
| 7 | `alibaba.alihealth.medical.insuracne.claim.settlement.withdraw` |

### 本地生活客资平台-客资API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.kb.leads.record.modify` |
| 2 | `alibaba.alsc.kb.leads.record.pagequery` |

### 阿里妈妈-媒体开放平台

| # | API名称 |
|---|--------|
| 1 | `alibaba.tanx.ssp.settle.report.query` |

### 阿里妈妈-UniDesk (60 APIs)

<details>
<summary>展开查看全部 60 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.unidesk.rta.user.advertiser.get` |
| 2 | `taobao.unidesk.rta.ad.campaign.get` |
| 3 | `taobao.unidesk.rta.ad.campaign.add` |
| 4 | `taobao.unidesk.rta.ad.campaign.update` |
| 5 | `taobao.unidesk.rta.ad.campaign.delete` |
| 6 | `taobao.unidesk.rta.ad.campaign.status.update` |
| 7 | `taobao.unidesk.rta.ad.campaign.budget.update` |
| 8 | `taobao.unidesk.rta.ad.adgroup.get` |
| 9 | `taobao.unidesk.rta.ad.adgroup.add` |
| 10 | `taobao.unidesk.rta.ad.adgroup.update` |
| 11 | `taobao.unidesk.rta.ad.adgroup.status.update` |
| 12 | `taobao.unidesk.rta.ad.adgroup.pricing.update` |
| 13 | `taobao.unidesk.rta.ad.adgroup.budget.update` |
| 14 | `taobao.unidesk.rta.ad.adgroup.delete` |
| 15 | `taobao.unidesk.rta.ad.creative.get` |
| 16 | `taobao.unidesk.rta.ad.creative.program.add` |
| 17 | `taobao.unidesk.rta.ad.creative.program.update` |
| 18 | `taobao.unidesk.rta.ad.creative.custom.add` |
| 19 | `taobao.unidesk.rta.ad.creative.custom.update` |
| 20 | `taobao.unidesk.rta.assets.material.get` |
| 21 | `taobao.unidesk.rta.assets.material.add` |
| 22 | `taobao.unidesk.rta.assets.creativecomponent.get` |
| 23 | `taobao.unidesk.rta.assets.creativecomponent.add` |
| 24 | `taobao.unidesk.rta.assets.creativecomponent.update` |
| 25 | `taobao.unidesk.rta.ad.targeting.region.get` |
| 26 | `taobao.unidesk.rta.ad.targeting.awemecategory.get` |
| 27 | `taobao.unidesk.rta.ad.targeting.behaviorinterestkeyword.get` |
| 28 | `taobao.unidesk.rta.ad.targeting.behaviorinterestcategory.get` |
| 29 | `taobao.unidesk.rta.ad.targeting.awemetopauthor.get` |
| 30 | `taobao.unidesk.rta.assets.material.videocover.suggest` |
| 31 | `taobao.unidesk.rta.assets.material.share` |
| 32 | `taobao.unidesk.rta.ad.adgroup.budget.suggest` |
| 33 | `taobao.unidesk.rta.tools.industry.get` |
| 34 | `taobao.unidesk.rta.report.daily.get` |
| 35 | `taobao.unidesk.rta.report.hourly.get` |
| 36 | `taobao.unidesk.rta.report.asynctask.result.get` |
| 37 | `taobao.unidesk.rta.assets.material.asynctask.result.get` |
| 38 | `taobao.unidesk.rta.assets.material.asynctask.get` |
| 39 | `taobao.unidesk.rta.report.asynctask.add` |
| 40 | `taobao.unidesk.rta.assets.material.asynctask.add` |
| 41 | `taobao.unidesk.rta.report.asynctask.get` |
| 42 | `taobao.unidesk.rta.assets.landingpage.add` |
| 43 | `taobao.unidesk.rta.assets.landingpage.get` |
| 44 | `taobao.unidesk.rta.assets.profile.add` |
| 45 | `taobao.unidesk.rta.assets.profile.get` |
| 46 | `taobao.unidesk.rta.assets.profile.delete` |
| 47 | `taobao.unidesk.rta.ad.creativegroup.get` |
| 48 | `taobao.unidesk.rta.tools.stickerstyle.get` |
| 49 | `taobao.unidesk.rta.assets.talentauth.add` |
| 50 | `taobao.unidesk.rta.assets.talentauth.get` |
| 51 | `taobao.unidesk.rta.tools.monitorurl.get` |
| 52 | `taobao.unidesk.rta.report.order.detail.hourly.get` |
| 53 | `taobao.unidesk.rta.ad.raise.report.get` |
| 54 | `taobao.unidesk.rta.ad.raise.version.get` |
| 55 | `taobao.unidesk.rta.ad.raise.stop` |
| 56 | `taobao.unidesk.rta.ad.raise.get` |
| 57 | `taobao.unidesk.rta.ad.raise.update` |
| 58 | `taobao.unidesk.rta.assets.dpa.product.add` |
| 59 | `taobao.unidesk.rta.assets.dpa.product.get` |
| 60 | `alibaba.taobao.ud.lite.meida.cost.push` |

</details>

### 阿里健康&一树-ERP信息同步

| # | API名称 |
|---|--------|
| 1 | `alibaba.health.ys.cep.vip.insure.notice.sync` |
| 2 | `alibaba.health.ys.crm.tags.val.list` |
| 3 | `alibaba.health.ys.crm.vip.tag.list` |

### 斑马新能源充电微信小程序插件API (28 APIs)

<details>
<summary>展开查看全部 28 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `yunos.charge.client.rmark.user.query` |
| 2 | `yunos.charge.client.wxstation.filtercondition` |
| 3 | `yunos.charge.client.wxpay.completepoint` |
| 4 | `yunos.charge.client.wechat.rmark.user.update` |
| 5 | `yunos.charge.client.wechat.rmark.charge.parseqrcode` |
| 6 | `yunos.charge.client.wechat.rmark.charge.startcharge` |
| 7 | `yunos.charge.client.wechat.rmrak.order.unfished` |
| 8 | `yunos.charge.client.wechat.rmark.charge.stopcharge` |
| 9 | `yunos.charge.client.wechat.ramrk.order.info` |
| 10 | `yunos.charge.client.wechat.rmark.order.list` |
| 11 | `yunos.charge.client.wxstation.getpoisbykeywords` |
| 12 | `yunos.charge.client.wxstation.getstations` |
| 13 | `yunos.charge.client.wxstation.getstationdetails` |
| 14 | `yunos.charge.client.wxstation.stationbyconnid` |
| 15 | `yunos.charge.client.wxpay.createpaymentpoint` |
| 16 | `yunos.charge.client.wxpay.getpointstatus` |
| 17 | `yunos.charge.client.wxstation.citybypoi` |
| 18 | `yunos.charge.client.wechat.rmark.comment.add` |
| 19 | `yunos.charge.client.wechat.rmark.common.getosspolicy` |
| 20 | `yunos.charge.client.wechat.rmark.comment.show` |
| 21 | `yunos.charge.client.wechat.rmark.comment.detail` |
| 22 | `yunos.charge.client.wechat.rmark.comment.status` |
| 23 | `yunos.charge.client.wechat.rmark.comment.tag` |
| 24 | `yunos.charge.client.wechat.rmark.lockdown` |
| 25 | `yunos.charge.client.wechat.rmark.invoice.detail` |
| 26 | `yunos.charge.client.wechat.rmark.invoice.commonadd` |
| 27 | `yunos.charge.client.wechat.rmark.banner` |
| 28 | `yunos.charge.client.wechat.rmark.paysign` |

</details>

### FC3D

| # | API名称 |
|---|--------|
| 1 | `alibaba.fc.cloud.rendering.getaccesstoken` |
| 2 | `alibaba.fc.cloud.rendering.sessionlifecyclenotify` |
| 3 | `alibaba.fc.blockchain.query.addressbytel` |
| 4 | `alibaba.fc.cloud.rendering.sendbenefit` |
| 5 | `alibaba.fc.blockchain.query.nftinfobyaddress` |
| 6 | `alibaba.fc.cloud.rendering.benefit.dispatch` |

### 酒店交易API

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.order.distribution.validate` |
| 2 | `taobao.xhotel.order.distribution.create` |
| 3 | `taobao.xhotel.order.distribution.pay` |
| 4 | `taobao.xhotel.order.distribution.detail` |
| 5 | `taobao.xhotel.order.distribution.cancel` |
| 6 | `taobao.xhotel.order.international.distribution.detail` |
| 7 | `taobao.xhotel.order.international.distribution.validate` |
| 8 | `taobao.xhotel.trade.international.distribution.cancel` |
| 9 | `taobao.xhotel.order.international.distribution.create` |
| 10 | `taobao.xhotel.order.distribution.invoicing` |
| 11 | `taobao.xhotel.order.distribution.tmc.list` |
| 12 | `taobao.xhotel.order.distribution.tmc.query.invoice` |
| 13 | `taobao.xhotel.order.distribution.tmc.update.invoice.cycle` |

### 机构API

| # | API名称 |
|---|--------|
| 1 | `taobao.liveagency.bind.info.get` |
| 2 | `taobao.liveagency.orders.overview.get` |
| 3 | `taobao.liveagency.orders.file.get` |
| 4 | `taobao.liveagency.item.info.get` |

### 天猫好房平台服务API

| # | API名称 |
|---|--------|
| 1 | `tmall.alihouse.platform.serviceorder.punish.cancel` |
| 2 | `tmall.alihouse.platform.serviceorder.query` |

### 斑马充电中台开放API

| # | API名称 |
|---|--------|
| 1 | `yunos.charge.stop.charge` |
| 2 | `yunos.charge.start.charge` |
| 3 | `yunos.charge.invoice.add` |
| 4 | `yunos.charge.invoice.historylist` |
| 5 | `yunos.charge.invoice.detail` |
| 6 | `yunos.charge.invoice.orderlist` |
| 7 | `yunos.charge.auth.equipment` |
| 8 | `yunos.charge.station.confirm` |
| 9 | `yunos.charge.storage.ls.pullstation` |
| 10 | `yunos.banma.charge.sdk.apirouter` |
| 11 | `yunos.charge.pay.cashierurl` |
| 12 | `yunos.charge.pay.paymenturl` |
| 13 | `yunos.charge.pay.addsign` |
| 14 | `yunos.charge.pay.signstatus` |

### 盒马CRM

| # | API名称 |
|---|--------|
| 1 | `alibaba.wdk.crowd.tags.update` |

### 银泰物流平台

| # | API名称 |
|---|--------|
| 1 | `alibaba.mos.tms.iot.package.report` |

### 天猫校园供应链

| # | API名称 |
|---|--------|
| 1 | `tmall.campus.scm.nooriginalorder.receive` |
| 2 | `tmall.campus.scm.originalorder.receive` |
| 3 | `tmall.campus.scm.order.receive` |
| 4 | `tmall.campus.scm.inventory.synchronize` |

### 斑马新能源充电平台cms接口API

| # | API名称 |
|---|--------|
| 1 | `yunos.charge.cms.demoscreen.gettimeintervalstat` |
| 2 | `yunos.charge.cms.demoscreen.getorderstat` |
| 3 | `yunos.charge.cms.demoscreen.getsummary` |

### 本地生活用户增长互动业务

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.growth.interactive.mini.game.index.query` |
| 2 | `alibaba.alsc.growth.interactive.mini.game.integral.grant` |
| 3 | `alibaba.alsc.growth.interactive.mini.game.notice.push.send` |
| 4 | `alibaba.alsc.growth.interactive.mini.game.notice.push.batch.send` |
| 5 | `alibaba.alsc.growth.interactive.task.querytask` |
| 6 | `alibaba.alsc.growth.interactive.mini.game.identity.authorization.query` |
| 7 | `alibaba.alsc.growth.interactive.sns.rank.savesnapshotrank` |
| 8 | `alibaba.alsc.growth.interactive.fan.competition.school.progress.query` |
| 9 | `alibaba.alsc.growth.interactive.mini.game.participation.qualification.consult` |
| 10 | `alibaba.alsc.growth.interactive.sns.rank.reward` |

### 天淘海外服务平台

| # | API名称 |
|---|--------|
| 1 | `alibaba.oversea.fulfil.localreturn.query` |
| 2 | `alibaba.oversea.sp.lr.inform.claim.result` |
| 3 | `alibaba.oversea.sp.lr.inform.insure` |
| 4 | `alibaba.oversea.sp.lr.inform.claim.create` |

### moss

| # | API名称 |
|---|--------|
| 1 | `alibaba.yun.weather.detail.get` |

### 智能应用系统类目

| # | API名称 |
|---|--------|
| 1 | `taobao.smartapp.template.service.switch` |
| 2 | `taobao.smartapp.introduction.create` |
| 3 | `taobao.smartapp.introduction.update` |
| 4 | `taobao.smartapp.introduction.list.get` |
| 5 | `taobao.smartapp.introduction.items.bind` |
| 6 | `taobao.smartapp.introduction.card.send` |
| 7 | `taobao.smartapp.introduction.detail.get` |

### 设计家权益API

| # | API名称 |
|---|--------|
| 1 | `alibaba.mpmw.coupon.ent.product.query` |
| 2 | `alibaba.mpmw.coupon.emp.product.query` |

### 闲鱼电商SAAS (98 APIs)

<details>
<summary>展开查看全部 98 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.isv.order.query` |
| 2 | `alibaba.idle.isv.pv.query` |
| 3 | `alibaba.idle.goosefish.trade.extra.data.upload` |
| 4 | `alibaba.idle.isv.item.cpv.recommend.property.search` |
| 5 | `alibaba.idle.isv.item.cpv.recommend` |
| 6 | `alibaba.idle.isv.item.ai.desc.generate` |
| 7 | `alibaba.idle.isv.item.cpv.category.fulltree` |
| 8 | `alibaba.idle.isv.servicerate.bizquery` |
| 9 | `alibaba.idle.sechand.car.dealer.quality.query` |
| 10 | `alibaba.idle.cro.record.query` |
| 11 | `alibaba.idle.sechand.car.dealer.quality.user.token` |
| 12 | `alibaba.idle.isv.item.cpv.category.fulltree.with.priv` |
| 13 | `alibaba.idle.isv.order.rate.query` |
| 14 | `alibaba.idle.isv.item.buy.limit.rule.query` |
| 15 | `alibaba.idle.isv.item.buy.limit.rule.delete` |
| 16 | `alibaba.idle.isv.item.buy.limit.rule.update` |
| 17 | `alibaba.idle.isv.item.buy.limit.rule.create` |
| 18 | `alibaba.idle.isv.item.ship.type` |
| 19 | `alibaba.idle.isv.item.cycle.buy.activity.list` |
| 20 | `alibaba.idle.isv.trade.dispute.query` |
| 21 | `alibaba.idle.isv.price.strength.check` |
| 22 | `alibaba.idle.isv.address.modify.query` |
| 23 | `alibaba.idle.isv.address.modify.agree` |
| 24 | `alibaba.idle.isv.address.modify.refuse` |
| 25 | `alibaba.idle.coin.coindeduction.open` |
| 26 | `alibaba.idle.coin.coindeduction.list` |
| 27 | `alibaba.idle.coin.coindeduction.close` |
| 28 | `alibaba.idle.coin.coindeduction.query` |
| 29 | `alibaba.idle.coin.coindeduction.change` |
| 30 | `alibaba.idle.coin.coindeduction.check` |
| 31 | `alibaba.idle.coin.coindeduction.user.check` |
| 32 | `alibaba.idle.coin.coindeduction.item.query` |
| 33 | `alibaba.idle.merchant.media.pic.to.id` |
| 34 | `alibaba.idle.isv.item.media.pic.to.id` |
| 35 | `alibaba.idle.fun.content.publish` |
| 36 | `alibaba.idle.isv.order.report.upload` |
| 37 | `alibaba.idle.isv.lease.seller.address.add` |
| 38 | `alibaba.idle.isv.lease.seller.address.query` |
| 39 | `alibaba.idle.isv.lease.order.adjustprice` |
| 40 | `alibaba.idle.isv.lease.order.inspection.upload` |
| 41 | `alibaba.idle.isv.lease.seller.address.edit` |
| 42 | `alibaba.idle.isv.lease.order.return.address.edit` |
| 43 | `alibaba.idle.isv.lease.seller.address.delete` |
| 44 | `alibaba.idle.isv.lease.proof.pic.upload` |
| 45 | `alibaba.idle.item.pledge.aggrement.upload` |
| 46 | `alibaba.idle.isv.order.url.add` |
| 47 | `alibaba.idle.isv.item.url.query` |
| 48 | `alibaba.idle.selected.recheck.order.perform` |
| 49 | `alibaba.idle.isv.lease.order.dummy.consign` |
| 50 | `alibaba.idle.selected.preget.report.diffurl` |
| 51 | `alibaba.idle.local.message.send` |
| 52 | `alibaba.idle.local.message.pic.upload` |
| 53 | `alibaba.idle.local.im.bind.query` |
| 54 | `alibaba.idle.local.im.unbind` |
| 55 | `alibaba.idle.local.im.bind` |
| 56 | `alibaba.idle.isv.item.ship.locations.query` |
| 57 | `alibaba.idle.coupon.isv.media.upload` |
| 58 | `alibaba.idle.isv.order.ma.update` |
| 59 | `alibaba.idle.isv.order.ma.send` |
| 60 | `alibaba.idle.isv.order.ma.onlysend` |
| 61 | `alibaba.idle.isv.eticket.order.refund` |
| 62 | `alibaba.idle.isv.item.eitcket.edit` |
| 63 | `alibaba.idle.isv.xgpu.quote` |
| 64 | `alibaba.idle.isv.single.order.rate.query` |
| 65 | `alibaba.idle.xgpu.item.bind.query` |
| 66 | `alibaba.idle.local.service.isv.relation.operate` |
| 67 | `alibaba.idle.local.service.isv.relation.query` |
| 68 | `alibaba.idle.local.service.isv.range.query` |
| 69 | `alibaba.idle.local.service.isv.range.create` |
| 70 | `alibaba.idle.isv.auth.item.edit` |
| 71 | `alibaba.idle.isv.auth.item.query` |
| 72 | `alibaba.idle.isv.auth.item.publish` |
| 73 | `alibaba.idle.isv.auth.media.upload` |
| 74 | `alibaba.idle.isv.auth.pv.query` |
| 75 | `alibaba.idle.isv.auth.item.downshelf` |
| 76 | `alibaba.idle.isv.auth.spu.query` |
| 77 | `alibaba.idle.isv.auth.cspu.query` |
| 78 | `alibaba.idle.logistics.auth.companies.query` |
| 79 | `alibaba.idle.isv.auth.order.adjustprice` |
| 80 | `alibaba.idle.isv.auth.order.dummy.consign` |
| 81 | `alibaba.idle.logistics.isv.template.query` |
| 82 | `alibaba.idle.logistics.isv.template.create` |
| 83 | `alibaba.idle.logistics.isv.template.update` |
| 84 | `alibaba.idle.logistics.isv.template.division` |
| 85 | `alibaba.idle.isv.auth.pic.upload` |
| 86 | `alibaba.idle.logistics.isv.template.delete` |
| 87 | `alibaba.idle.isv.service.order.query` |
| 88 | `alibaba.idle.isv.service.refund.query` |
| 89 | `alibaba.idle.isv.service.order.dealrefund` |
| 90 | `alibaba.idle.isv.service.order.ship` |
| 91 | `alibaba.idle.isv.service.order.close` |
| 92 | `alibaba.idle.isv.buyer.default.address.query` |
| 93 | `alibaba.idle.coin.coindeduction.ratio.list` |
| 94 | `alibaba.idle.coin.coindeduction.store.retry` |
| 95 | `alibaba.idle.coin.coindeduction.store.status` |
| 96 | `alibaba.idle.coin.coindeduction.store.modify` |
| 97 | `alibaba.idle.coin.coindeduction.store.open` |
| 98 | `alibaba.idle.coin.coindeduction.store.items` |

</details>

### 淘特互动任务API

| # | API名称 |
|---|--------|
| 1 | `alibaba.taote.interact.diversion.task.trigger` |

### 服务开放平台API

| # | API名称 |
|---|--------|
| 1 | `taobao.open.service.status.update` |

### 万相台无界API (127 APIs)

<details>
<summary>展开查看全部 127 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.universalbp.new.report.query.realtime` |
| 2 | `taobao.universalbp.new.campaign.findpage` |
| 3 | `taobao.universalbp.new.campaign.advanced.batchupdate` |
| 4 | `taobao.universalbp.new.campaign.updatepart` |
| 5 | `taobao.universalbp.new.campaign.updategroup` |
| 6 | `taobao.universalbp.new.campaign.get` |
| 7 | `taobao.universalbp.new.campaign.findlist` |
| 8 | `taobao.universalbp.new.campaign.delete` |
| 9 | `taobao.universalbp.new.solution.addlist` |
| 10 | `taobao.universalbp.new.campaign.budget.batchupdate` |
| 11 | `taobao.universalbp.new.campaign.bid.batchupdate` |
| 12 | `taobao.universalbp.new.material.intelligentpreshow` |
| 13 | `taobao.universalbp.new.adgroup.updatepart` |
| 14 | `taobao.universalbp.new.adgroup.delete` |
| 15 | `taobao.universalbp.new.member.findbrandinfolist` |
| 16 | `taobao.universalbp.new.material.shop.get` |
| 17 | `taobao.universalbp.new.material.item.findpage` |
| 18 | `taobao.universalbp.new.material.accessallowed` |
| 19 | `taobao.universalbp.new.adgroup.horizontal.findpage` |
| 20 | `taobao.universalbp.new.adgroup.bid.batchupdate` |
| 21 | `taobao.universalbp.new.adgroup.addlist` |
| 22 | `taobao.universalbp.new.account.get.balance` |
| 23 | `taobao.universalbp.new.account.get.can.use.bizcode` |
| 24 | `taobao.universalbp.new.suggest.bidword.price` |
| 25 | `taobao.universalbp.new.bidword.update` |
| 26 | `taobao.universalbp.new.bidword.suggestkrlist` |
| 27 | `taobao.universalbp.new.bidword.suggestdefaultlist` |
| 28 | `taobao.universalbp.new.bidword.qscore` |
| 29 | `taobao.universalbp.new.bidword.findlist` |
| 30 | `taobao.universalbp.new.bidword.delete` |
| 31 | `taobao.universalbp.new.bidword.add` |
| 32 | `taobao.universalbp.new.label.findpage` |
| 33 | `taobao.universalbp.new.label.findlist` |
| 34 | `taobao.universalbp.new.label.dmpconvert` |
| 35 | `taobao.universalbp.new.account.is.universal.user` |
| 36 | `taobao.universalbp.new.wordpackage.suggestkrlist` |
| 37 | `taobao.universalbp.new.wordpackage.update` |
| 38 | `taobao.universalbp.new.wordpackage.suggestdefaultlist` |
| 39 | `taobao.universalbp.new.wordpackage.findlist` |
| 40 | `taobao.universalbp.new.wordpackage.delete` |
| 41 | `taobao.universalbp.new.wordpackage.add` |
| 42 | `taobao.universalbp.new.crowd.horizontal.modifystatus` |
| 43 | `taobao.universalbp.new.crowd.horizontal.modifybidprice` |
| 44 | `taobao.universalbp.new.crowd.horizontal.modifydiscount` |
| 45 | `taobao.universalbp.new.crowd.findrecommendcrowd` |
| 46 | `taobao.universalbp.new.crowd.horizontal.findpage` |
| 47 | `taobao.universalbp.new.crowd.findlist` |
| 48 | `taobao.universalbp.new.crowd.batchmodify` |
| 49 | `taobao.universalbp.new.crowd.batchdelete` |
| 50 | `taobao.universalbp.new.creative.getcreativebyconditionmap` |
| 51 | `taobao.universalbp.new.creative.manage.findmanagepage` |
| 52 | `taobao.universalbp.new.creative.findrequire` |
| 53 | `taobao.universalbp.new.creative.preview` |
| 54 | `taobao.universalbp.new.creative.preadd` |
| 55 | `taobao.universalbp.new.creative.horizontal.findpage` |
| 56 | `taobao.universalbp.new.creative.getbindcreativelist` |
| 57 | `taobao.universalbp.new.creative.update` |
| 58 | `taobao.universalbp.new.creative.add` |
| 59 | `taobao.universalbp.new.creative.bind` |
| 60 | `taobao.universalbp.new.creative.updatepart` |
| 61 | `taobao.universalbp.new.creative.updatecreativeandtemplate` |
| 62 | `taobao.universalbp.new.creative.unbind` |
| 63 | `taobao.universalbp.new.shield.textjudge` |
| 64 | `taobao.universalbp.new.adzone.findconfiglist` |
| 65 | `taobao.universalbp.new.stdcategory.findcategorycondition` |
| 66 | `taobao.universalbp.new.stdcategory.findlist` |
| 67 | `taobao.universalbp.new.shopcategory.findlist` |
| 68 | `taobao.universalbp.new.campaigngroup.modify` |
| 69 | `taobao.universalbp.new.campaigngroup.findlist` |
| 70 | `taobao.universalbp.new.campaigngroup.add` |
| 71 | `taobao.universalbp.new.algo.getbidsuggestion` |
| 72 | `taobao.universalbp.new.adzone.horizontal.findpage` |
| 73 | `taobao.universalbp.new.report.query.area` |
| 74 | `taobao.universalbp.new.report.query.creative` |
| 75 | `taobao.universalbp.new.report.query.not.item.promotion` |
| 76 | `taobao.universalbp.new.report.query.item.promotion` |
| 77 | `taobao.universalbp.new.report.query.crowd` |
| 78 | `taobao.universalbp.new.report.query.bidword` |
| 79 | `taobao.universalbp.new.report.query.adgroup` |
| 80 | `taobao.universalbp.new.report.query.campaign` |
| 81 | `taobao.universalbp.new.report.query.account` |
| 82 | `taobao.universalbp.new.commonapi.getcodeconfig` |
| 83 | `taobao.universalbp.new.label.dmp.finddmpcrowdbymoduleconfig` |
| 84 | `taobao.universalbp.new.label.dmp.finddmpmoduleconfig` |
| 85 | `taobao.universalbp.new.label.findconfiglist` |
| 86 | `taobao.universalbp.new.campaign.findsubcampaignid` |
| 87 | `taobao.universalbp.new.diagnose.highlight` |
| 88 | `taobao.universalbp.new.report.chargesum` |
| 89 | `taobao.universalbp.new.report.async.download.get.url` |
| 90 | `taobao.universalbp.new.report.async.download.find.task.page` |
| 91 | `taobao.universalbp.new.report.async.create.download.task` |
| 92 | `taobao.universalbp.new.diagnose.adgroup.faultlist` |
| 93 | `taobao.universalbp.new.diagnose.campaign.faultlist` |
| 94 | `taobao.universalbp.new.algo.getbatchbidsuggestion` |
| 95 | `taobao.universalbp.new.check.complete.scene` |
| 96 | `taobao.universalbp.new.algo.getbudgetsuggestion` |
| 97 | `taobao.universalbp.new.campaign.site.itemdiff` |
| 98 | `taobao.universalbp.new.algo.geteffectprediction` |
| 99 | `taobao.universalbp.new.creative.check.role` |
| 100 | `taobao.universalbp.new.creative.report.material` |
| 101 | `taobao.universalbp.new.solution.modify` |
| 102 | `taobao.universalbp.new.material.find.spot` |
| 103 | `taobao.universalbp.new.creative.update.rotation` |
| 104 | `taobao.universalbp.new.blackword.find` |
| 105 | `taobao.universalbp.new.blackword.update` |
| 106 | `taobao.universalbp.new.potential.bidword.find` |
| 107 | `taobao.universalbp.new.campaign.updatedetent` |
| 108 | `taobao.universalbp.new.campaign.onerecover` |
| 109 | `taobao.universalbp.new.campaign.oneclick` |
| 110 | `taobao.universalbp.new.itemcross.promotion.find` |
| 111 | `taobao.universalbp.new.adzone.aggregated.findlist` |
| 112 | `taobao.universalbp.new.campaign.freeze` |
| 113 | `taobao.universalbp.new.campaign.finish` |
| 114 | `taobao.universalbp.new.check.universal.role` |
| 115 | `taobao.universalbp.new.report.query.realtime.special` |
| 116 | `taobao.universalbp.new.creative.update.material.time` |
| 117 | `taobao.universalbp.new.creative.update.material` |
| 118 | `taobao.universalbp.new.word.gategory.find` |
| 119 | `taobao.universalbp.new.word.index.detail` |
| 120 | `taobao.universalbp.new.member.sign.protocol` |
| 121 | `taobao.universalbp.new.member.judge.signprotocol` |
| 122 | `taobao.universalbp.new.member.judge.sign.bp.protocol` |
| 123 | `taobao.universalbp.new.campaign.onebpsearch.batchupdate` |
| 124 | `taobao.universalbp.new.campaign.onebpsite.batchupdate` |
| 125 | `taobao.universalbp.new.campaign.onebpdisplay.batchupdate` |
| 126 | `taobao.universalbp.new.template.getsuggest` |
| 127 | `taobao.universalbp.new.report.query.realtime.maochao` |

</details>

### 飞猪服务平台

| # | API名称 |
|---|--------|
| 1 | `alitrip.serve.workorder.relation` |
| 2 | `alitrip.xspace.case.create` |
| 3 | `alitrip.serve.workorder.relation.query` |
| 4 | `alibaba.fliggy.pushcenter.intention.query` |

### 原力平台API

| # | API名称 |
|---|--------|
| 1 | `taobao.force.async.result.notify` |

### 业务平台事业部-网关平台API

| # | API名称 |
|---|--------|
| 1 | `alibaba.cfo.trade.info.query.ant` |

### 天猫家装API

| # | API名称 |
|---|--------|
| 1 | `taobao.jzfx.orders.query` |
| 2 | `taobao.jzfx.refund.query` |
| 3 | `taobao.jzfx.logistics.offline.send` |

### 淘分销API

| # | API名称 |
|---|--------|
| 1 | `taobao.tfx.distributor.settle.status.get` |
| 2 | `taobao.tfx.item.publish` |
| 3 | `taobao.tfx.distributor.agreement.status.get` |
| 4 | `taobao.tfx.alipay.sign.url.get` |
| 5 | `taobao.tfx.distributor.agreement.sign` |
| 6 | `taobao.tfx.distributor.active` |
| 7 | `taobao.tfx.distributor.settle` |
| 8 | `taobao.tfx.item.sync` |
| 9 | `taobao.tfx.item.unlink` |
| 10 | `taobao.tfx.item.link` |
| 11 | `taobao.tfx.distributor.items.query` |
| 12 | `taobao.tfx.product.search` |
| 13 | `taobao.tfx.product.detail.get` |
| 14 | `taobao.tfx.product.price.set` |

### 优酷CRP

| # | API名称 |
|---|--------|
| 1 | `youku.crp.scm.order.modify` |

### 橙狮体育课程视频生产

| # | API名称 |
|---|--------|
| 1 | `alibaba.alisports.splan.generate.oss.policy` |
| 2 | `alibaba.alisports.splan.generate.task` |
| 3 | `alibaba.alisports.splan.generate.result.save` |
| 4 | `alibaba.alisports.splan.generate.create` |

### 小活动开放API

| # | API名称 |
|---|--------|
| 1 | `taobao.activity.item.list.query` |
| 2 | `taobao.activity.item.discounts.query` |
| 3 | `taobao.activity.item.risk.calc` |
| 4 | `taobao.activity.item.info.query` |
| 5 | `taobao.activity.status.manage` |
| 6 | `taobao.activity.info.get` |
| 7 | `taobao.activity.schema.get` |
| 8 | `taobao.activity.info.list.get` |
| 9 | `taobao.activity.schema.edit` |
| 10 | `taobao.activity.scenes.cancel` |
| 11 | `taobao.activity.scene.publish` |
| 12 | `taobao.activity.scene.schema.get` |
| 13 | `taobao.activity.scene.get` |
| 14 | `taobao.activity.data.get` |
| 15 | `taobao.activity.shorturl.refresh` |

### 阿里体育智能运动api (41 APIs)

<details>
<summary>展开查看全部 41 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.alisports.smartsports.sports.rounds.data.upload` |
| 2 | `alibaba.alisports.smartsports.sports.statis.data.upload` |
| 3 | `alibaba.alisports.smartsports.venue.resource.bydevice.get` |
| 4 | `alibaba.alisports.smartsports.venue.ai.resource.get` |
| 5 | `alibaba.alisports.smartsports.dynamic.qrcode.get` |
| 6 | `alibaba.alisports.smartsports.venue.close` |
| 7 | `alibaba.alisports.smartsports.venue.room.get` |
| 8 | `alibaba.alisports.smartsports.rounds.data.query` |
| 9 | `alibaba.alisports.smartsports.room.status.upload` |
| 10 | `alibaba.alisports.smartsports.video.clip.status.update` |
| 11 | `alibaba.alisports.smartsports.device.venue.config.get` |
| 12 | `alibaba.alisports.smartsports.venue.clip.record.upload` |
| 13 | `alibaba.alisports.smartsports.venue.config.get` |
| 14 | `alibaba.alisports.smartsports.device.config.get` |
| 15 | `alibaba.alisports.smartsports.game.stats.data.query` |
| 16 | `alibaba.alisports.smartsports.game.current.score.query` |
| 17 | `alibaba.alisports.smartsports.scheduler.cloud.switch.get` |
| 18 | `alibaba.alisports.smartsports.venue.config.update` |
| 19 | `alibaba.alisports.smartsports.room.create.status.upload` |
| 20 | `alibaba.alisports.smartsports.game.score.round.data.query` |
| 21 | `alibaba.alisports.smartsports.identification.result.upload` |
| 22 | `alibaba.alisports.smartsports.sports.round.data.upload.complete` |
| 23 | `alibaba.alisports.smartsports.room.user.info.query` |
| 24 | `alibaba.alisports.smartsports.room.identification.result.upload` |
| 25 | `alibaba.alisports.smartsports.room.hawkeye.animation.upload` |
| 26 | `alibaba.alisports.smartsports.room.hawkeye.list.upload` |
| 27 | `alibaba.alisports.smartsports.device.job.list` |
| 28 | `alibaba.alisports.smartsports.basketball.game.score.record.query` |
| 29 | `alibaba.alisports.smartsports.sports.aiuser.data.upload` |
| 30 | `alibaba.alisports.smartsports.sports.rounds.training.type.upload` |
| 31 | `alibaba.alisports.smartsports.game.score.time.round.data.query` |
| 32 | `alibaba.alisports.smartsports.game.time.match.data.query` |
| 33 | `alibaba.alisports.smartsports.live.config.query` |
| 34 | `alibaba.alisports.smartsports.venue.config.info.get` |
| 35 | `alibaba.alisports.smartsports.live.ops.camera.monitor` |
| 36 | `alibaba.alisports.smartsports.video.ops.status.update` |
| 37 | `alibaba.alisports.smartsports.eci.task.result` |
| 38 | `alibaba.alisports.smartsports.aitennis.appver` |
| 39 | `alibaba.alisports.smartsports.dynamic.short.qrcode.get` |
| 40 | `alibaba.alisports.smartsports.exam.item.data.upload` |
| 41 | `alibaba.alisports.smartsports.room.insights.message.send` |

</details>

### 闲鱼物流

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.logistics.courier.sync` |
| 2 | `alibaba.idle.logistics.weight.price.sync` |
| 3 | `alibaba.idle.logistics.status.sync` |
| 4 | `alibaba.idle.logistics.route.sync` |
| 5 | `alibaba.idle.logistics.template.update` |
| 6 | `alibaba.idle.logistics.template.query` |
| 7 | `alibaba.idle.logistics.template.create` |
| 8 | `alibaba.idle.logistics.template.delete` |
| 9 | `alibaba.idle.logistics.template.query.list` |
| 10 | `alibaba.idle.logistics.template.division` |

### 盒马配送API

| # | API名称 |
|---|--------|
| 1 | `wdk.dms.delivery.dock.get` |
| 2 | `wdk.dms.delivery.order.status.callback` |
| 3 | `wdk.dms.center.jd.trace.push` |
| 4 | `wdk.dms.center.common.trace.push` |

### 淘宝买菜次日达-快递送达 (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `alibaba.tbmc.item.publish` |
| 2 | `alibaba.tbmc.item.update` |
| 3 | `alibaba.tbmc.order.get` |
| 4 | `alibaba.tbmc.item.publish.schema.get` |
| 5 | `alibaba.tbmc.item.recommend.query` |
| 6 | `alibaba.tbmc.inventory.publish` |
| 7 | `alibaba.tbmc.effective.brand.authorization` |
| 8 | `alibaba.tbmc.item.base.sale.price.update` |
| 9 | `alibaba.tbmc.item.base.sale.price.query` |
| 10 | `alibaba.tbmc.item.status.update` |
| 11 | `alibaba.tbmc.supplier.sale.range.query` |
| 12 | `alibaba.tbmc.fulfill.offline.send` |
| 13 | `alibaba.tbmc.refund.get` |
| 14 | `alibaba.tbmc.refund.intercept.result` |
| 15 | `alibaba.tbmc.refund.audit` |
| 16 | `alibaba.tbmc.item.page.query` |
| 17 | `alibaba.tbmc.item.get.with.schema` |

</details>

### 淘宝闪购联盟-卡券API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.union.eleme.coupon.store.query` |
| 2 | `alibaba.alsc.union.eleme.coupon.detail.get` |
| 3 | `alibaba.alsc.union.eleme.coupon.query` |
| 4 | `alibaba.alsc.union.eleme.coupon.order.refund` |
| 5 | `alibaba.alsc.union.eleme.coupon.order.create` |
| 6 | `alibaba.alsc.union.eleme.coupon.order.query` |
| 7 | `alibaba.alsc.union.eleme.coupon.order.pay` |

### TanxBP API

| # | API名称 |
|---|--------|
| 1 | `taobao.tanx.rta.id.allocate` |
| 2 | `taobao.tanx.rta.id.associate` |
| 3 | `taobao.tanx.rta.id.account.list` |
| 4 | `taobao.tanx.rta.id.list` |
| 5 | `taobao.tanx.rta.id.disassociate` |
| 6 | `taobao.tanx.rta.id.sync` |
| 7 | `taobao.tanx.dsp.report.list` |

### 淘宝闪购联盟-采购单API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.union.eleme.couponpackage.purchase.ticket.get` |
| 2 | `alibaba.alsc.union.eleme.couponpackage.purchase.query` |
| 3 | `alibaba.alsc.union.eleme.couponpackage.purchase.ticket.create` |
| 4 | `alibaba.alsc.union.eleme.couponpackage.purchase.ticket.refund` |
| 5 | `alibaba.alsc.union.eleme.couponpackage.purchase.detail.get` |

### 以旧换新-信用付

| # | API名称 |
|---|--------|
| 1 | `taobao.ofn.credit.prepay.recover.query` |
| 2 | `taobao.ofn.credit.prepay.recover.cancel` |
| 3 | `taobao.ofn.credit.prepay.recover` |
| 4 | `taobao.recycle.credit.prededuct.detail.get` |

### 淘天物流API (18 APIs)

<details>
<summary>展开查看全部 18 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.logistics.express.delivery.cut.notify` |
| 2 | `taobao.logistics.express.pickcode.check` |
| 3 | `taobao.logistics.express.packageweight.sync` |
| 4 | `taobao.logistics.express.courier.sync` |
| 5 | `taobao.logistics.express.collect.sync` |
| 6 | `taobao.logistics.express.service.sync` |
| 7 | `taobao.logistics.express.order.tms.update` |
| 8 | `taobao.logistics.express.order.tms.cancel` |
| 9 | `taobao.logistics.express.order.pay.tms.query` |
| 10 | `taobao.logistics.express.operate.sync` |
| 11 | `taobao.logistics.tms.transportorder.result.report` |
| 12 | `taobao.logistics.file.upload.apply` |
| 13 | `taobao.logistics.express.abnormal.report` |
| 14 | `taobao.logistics.wms.device.report` |
| 15 | `taobao.logistics.trace.get.new` |
| 16 | `taobao.logistics.mail.return.service` |
| 17 | `taobao.logistics.express.diagnosis.sync` |
| 18 | `taobao.logistics.express.bill.reversal` |

</details>

### 闲鱼循环商店-前台

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.cycleshop.seller.goodslist` |
| 2 | `alibaba.idle.cycleshop.seller.packlist` |
| 3 | `alibaba.idle.cycleshop.seller.reportinfo` |
| 4 | `alibaba.idle.cycleshop.seller.goodspush` |
| 5 | `alibaba.idle.isv.item.price.advice` |

### 飞猪大交通顺风车api

| # | API名称 |
|---|--------|
| 1 | `alitrip.traffic.hitch.user.auth.query` |
| 2 | `alitrip.traffic.hitch.order.create` |
| 3 | `alitrip.traffic.hitch.order.sync` |
| 4 | `alitrip.hitch.coupon.status.notify` |

### 淘宝直播AI开放

| # | API名称 |
|---|--------|
| 1 | `taobao.live.virtualanchor.get.live.detail` |
| 2 | `taobao.live.aiopen.aliyun.get.oss.token` |
| 3 | `taobao.live.virtualanchor.model.common.upload` |
| 4 | `taobao.live.virtualanchor.model.personal.upload` |
| 5 | `taobao.live.virtualanchor.model.personal.stock.upload` |
| 6 | `taobao.live.virtualanchor.model.tone.upload` |
| 7 | `taobao.live.virtualanchor.push.item.card` |
| 8 | `taobao.live.digitalanchor.get.reportstats` |

### 闲鱼彩票

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.isv.lottery.redeem.callback` |
| 2 | `alibaba.idle.isv.lottery.writeoff.callback` |

### ICBU-直播

| # | API名称 |
|---|--------|
| 1 | `alibaba.icbulive.productlist.pageget` |
| 2 | `alibaba.icbulive.product.push` |

### 淘天仓储API (17 APIs)

<details>
<summary>展开查看全部 17 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.logistics.wms.goods.info.sync` |
| 2 | `taobao.logistics.wms.packageentryorder.pull` |
| 3 | `taobao.logistics.wms.packagedeliveryorder.pull` |
| 4 | `taobao.logistics.wms.packageentryorder.confirm` |
| 5 | `taobao.logistics.wms.packagedeliveryorder.confirm` |
| 6 | `taobao.logistics.wms.valueaddedorder.confirm` |
| 7 | `taobao.logistics.wms.packageexception.report` |
| 8 | `taobao.logistics.wms.entryorder.stocking.apply` |
| 9 | `taobao.logistics.wms.returnaddress.query` |
| 10 | `taobao.logistics.wms.opexception.report` |
| 11 | `taobao.logistics.wms.active.registration.result.report` |
| 12 | `taobao.logistics.wms.inventory.imbalance.create` |
| 13 | `taobao.logistics.wms.deliveryorder.package.report` |
| 14 | `taobao.logistics.wms.goods.packagingsolution.check` |
| 15 | `taobao.logistics.wms.shiporder.create` |
| 16 | `taobao.logistics.wms.shiporder.cancel` |
| 17 | `taobao.logistics.wms.shiporder.complete` |

</details>

### 淘天跨境API

| # | API名称 |
|---|--------|
| 1 | `taobao.logistics.clearance.repush` |
| 2 | `taobao.logistics.clearance.receiptreport` |
| 3 | `taobao.logistics.order.process.status.report` |
| 4 | `taobao.logistics.wms.tally.verification.sync` |

### 探号API

| # | API名称 |
|---|--------|
| 1 | `alibaba.tanhao.item.propertydef.query` |
| 2 | `alibaba.tanhao.item.external.batch.publish` |
| 3 | `alibaba.tanhao.item.game.sever.query` |
| 4 | `alibaba.tanhao.item.external.goods.batch.onsale` |
| 5 | `alibaba.tanhao.item.external.goods.batchtask.query` |
| 6 | `alibaba.tanhao.item.external.goods.detail.query` |
| 7 | `alibaba.tanhao.item.external.goods.status.batch.query` |
| 8 | `alibaba.tanhao.item.external.goods.batch.offsale` |
| 9 | `alibaba.tanhao.item.external.goods.batch.delete` |
| 10 | `alibaba.tanhao.item.external.goods.batch.modifyprice` |

### 商品质量分API

| # | API名称 |
|---|--------|
| 1 | `taobao.item.diagnose.batch.submit` |
| 2 | `taobao.item.diagnose.list.get` |
| 3 | `taobao.item.diagnose.manage.list.get` |
| 4 | `taobao.item.diagnose.publish.single.execute` |

### 商家财务api

| # | API名称 |
|---|--------|
| 1 | `taobao.finance.fund.bill.export` |

### 绘蛙API (27 APIs)

<details>
<summary>展开查看全部 27 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `lianfan.huiwa.task.image.get` |
| 2 | `lianfan.huiwa.model.get` |
| 3 | `lianfan.huiwa.model.scene.submit` |
| 4 | `lianfan.huiwa.task.image.submit` |
| 5 | `lianfan.huiwa.model.tags.get` |
| 6 | `lianfan.huiwa.image.huaman.check` |
| 7 | `lianfan.huiwa.model.human.submit` |
| 8 | `lianfan.huiwa.user.query` |
| 9 | `lianfan.huiwa.model.scene.byte.submit` |
| 10 | `lianfan.huiwa.task.image.expand.submit` |
| 11 | `lianfan.huiwa.image.automaticmatting.submit` |
| 12 | `lianfan.huiwa.image.automaticmatting.get` |
| 13 | `lianfan.huiwa.scene.recommend.get` |
| 14 | `lianfan.huiwa.project.create` |
| 15 | `lianfan.huiwa.project.itemandtask.query` |
| 16 | `lianfan.huiwa.task.video.submit` |
| 17 | `lianfan.huiwa.task.video.get` |
| 18 | `lianfan.huiwa.model.del` |
| 19 | `lianfan.huiwa.prompt.recommend` |
| 20 | `lianfan.huiwa.model.video.submit` |
| 21 | `lianfan.huiwa.model.video.get` |
| 22 | `lianfan.huiwa.task.storyboard.submit` |
| 23 | `lianfan.huiwa.task.audio.submit` |
| 24 | `lianfan.huiwa.task.list.query` |
| 25 | `lianfan.huiwa.task.content.understanding.submit` |
| 26 | `lianfan.huiwa.aicreation.submit` |
| 27 | `lianfan.huiwa.aicreation.image.submit` |

</details>

### 闲鱼房源-前台

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.new.house.item.add` |
| 2 | `alibaba.idle.new.house.item.query` |
| 3 | `alibaba.idle.new.house.image.upload` |
| 4 | `alibaba.idle.new.house.item.status.update` |
| 5 | `alibaba.idle.new.house.item.update` |
| 6 | `alibaba.idle.new.house.community.upload` |
| 7 | `alibaba.idle.house.addcorporateaccount` |
| 8 | `alibaba.idle.house.removecorporateaccount` |
| 9 | `alibaba.idle.house.querycorporateaccount` |
| 10 | `alibaba.idle.new.house.itemlist.query` |

### 闲客联盟

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.affiliate.material.guide.get` |
| 2 | `alibaba.idle.affiliate.general.link.convert` |
| 3 | `alibaba.idle.affiliate.material.query` |
| 4 | `alibaba.idle.affiliate.cps.order.query` |
| 5 | `alibaba.idle.affiliate.income.summary` |
| 6 | `alibaba.idle.affiliate.material.exact.get` |
| 7 | `alibaba.idle.affiliate.cps.income.details.query` |
| 8 | `alibaba.idle.affiliate.cps.income.details.signle.query` |
| 9 | `alibaba.idle.affliate.cpa.income.detail.get` |
| 10 | `alibaba.idle.affiliate.cpa.income.details.query` |
| 11 | `alibaba.idle.affiliate.cpa.period.summary.query` |
| 12 | `alibaba.idle.affiliate.cpa.income.summary` |
| 13 | `alibaba.idle.affiliate.campaign.get` |
| 14 | `alibaba.idle.affiliate.user.action.log.query` |
| 15 | `alibaba.idle.affiliate.daily.performance.query` |

### 场景金融服务

| # | API名称 |
|---|--------|
| 1 | `alibaba.fin.risk.score.query` |

### 生态开放API

| # | API名称 |
|---|--------|
| 1 | `taobao.item.batch.edit.task.update` |

### 淘宝小时达履约 (24 APIs)

<details>
<summary>展开查看全部 24 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.xsd.order.work.update` |
| 2 | `taobao.xsd.order.deliverer.change` |
| 3 | `taobao.xsd.order.logistics.track.callback` |
| 4 | `tmall.nr.fn.trace.query` |
| 5 | `taobao.xsd.order.logistics.order.callback` |
| 6 | `alibaba.xsd.logistics.order.status.callback` |
| 7 | `alibaba.xsd.logistics.order.abnormal.callback` |
| 8 | `alibaba.xsd.store.updaterange` |
| 9 | `alibaba.xsd.logistics.order.abnormal.record.callback` |
| 10 | `alibaba.xsd.logistics.store.status.callback` |
| 11 | `alibaba.xsd.logistics.store.range.callback` |
| 12 | `alibaba.xsd.logistics.store.businesstime.callback` |
| 13 | `alibaba.xsd.logistics.workorder.reply` |
| 14 | `alibaba.xsd.store.delivery.config.query` |
| 15 | `alibaba.xsd.store.delivery.purchase` |
| 16 | `alibaba.xsd.store.delivery.config.update` |
| 17 | `taobao.xsd.order.delivery.recall` |
| 18 | `taobao.xsd.order.delivery.query` |
| 19 | `alibaba.xsd.logistics.order.weight.callback` |
| 20 | `alibaba.xsd.logistics.store.extraservice.callback` |
| 21 | `taobao.xsd.order.delivery.switchselfdelivery` |
| 22 | `taobao.shangou.open.register` |
| 23 | `taobao.shangou.open.deregister` |
| 24 | `taobao.xsd.order.fulfill.querylifecycle` |

</details>

### 酒店营销api

| # | API名称 |
|---|--------|
| 1 | `taobao.xhotel.promotion.resource.unbind` |
| 2 | `taobao.xhotel.promotion.resource.bind` |
| 3 | `taobao.xhotel.promotion.create` |
| 4 | `taobao.xhotel.promotion.query` |
| 5 | `taobao.xhotel.promotion.list` |

### 以旧换新-溯源码

| # | API名称 |
|---|--------|
| 1 | `taobao.ofn.recycle.order.bind.status.query` |
| 2 | `taobao.ofn.recycle.qrcode.bind.status.query` |
| 3 | `taobao.ofn.recycle.qrcode.sync` |

### 天猫APP互动

| # | API名称 |
|---|--------|
| 1 | `tmall.app.farm.game.entity.num.check` |
| 2 | `tmall.app.farm.game.entity.operate` |

### ICBU-物流

| # | API名称 |
|---|--------|
| 1 | `alibaba.onetouch.logistics.express.logistics.solution.semi.list` |

### 闲鱼质检报告

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.isv.report.upload` |
| 2 | `alibaba.idle.isv.report.query` |
| 3 | `alibaba.idle.isv.report.price` |
| 4 | `alibaba.idle.isv.report.detail.by.id` |

### 淘宝闪购联盟-商品API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.union.supply.outer.item.state.update` |
| 2 | `alibaba.alsc.union.supply.outer.item.edit` |
| 3 | `alibaba.alsc.union.supply.outer.item.publish` |
| 4 | `alibaba.alsc.union.supply.outer.item.share` |

### 以旧换新-国补

| # | API名称 |
|---|--------|
| 1 | `alibaba.ofn.gov.subsidy.seller.invoice.info` |
| 2 | `taobao.smp.zfbt.sn.checklock` |
| 3 | `taobao.smp.zfbt.sn.checklog.get` |
| 4 | `taobao.smp.zfbt.sn.historylock.get` |
| 5 | `taobao.smp.zfbt.sn.service.get` |
| 6 | `tmall.gov.subsidy.audit.order.query` |
| 7 | `taobao.smp.zfbt.pic.upload.send` |
| 8 | `taobao.smp.zfbt.sn.unlocklog.get` |

### 飞猪金融API

| # | API名称 |
|---|--------|
| 1 | `alitrip.finance.callback.standard` |
| 2 | `alitrip.finance.standard.mock.request` |
| 3 | `alitrip.finance.zhixin.loan.receipt.status.notify` |
| 4 | `alitrip.finance.zhixin.repay.notify` |
| 5 | `alitrip.finance.zhixin.credit.notify` |
| 6 | `alitrip.finance.zhixin.loan.notify` |
| 7 | `alitrip.finance.standard.loanexcess.resgister.notify` |

### 三方AI项目

| # | API名称 |
|---|--------|
| 1 | `taobao.smart.call.talk.template.query` |
| 2 | `taobao.smart.call.virtual.number.query` |
| 3 | `taobao.smart.call.task.create` |
| 4 | `taobao.smart.call.task.list.query` |
| 5 | `taobao.smart.call.task.edit` |
| 6 | `taobao.smart.call.message.send` |

### 天猫APP用增

| # | API名称 |
|---|--------|
| 1 | `tmall.app.user.increase.yidong.query` |
| 2 | `tmall.app.user.increase.yidong.issue` |

### 闲鱼用增

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.usergrowth.rta.ask` |

### 本地生活信贷金融API

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.eloan.notice.credit` |
| 2 | `alibaba.alsc.eloan.notice.loan` |
| 3 | `alibaba.alsc.eloan.notice.repayment` |
| 4 | `alibaba.alsc.eloan.notice.refund` |
| 5 | `alibaba.alsc.eloan.notice.autorepayment` |
| 6 | `alibaba.alsc.eloan.notice.account` |
| 7 | `alibaba.alsc.eloan.notice.leads` |
| 8 | `alibaba.alsc.eloan.notice.leadsloanresult` |
| 9 | `alibaba.alsc.eloan.notice.couponchange` |
| 10 | `alibaba.alsc.eloan.notice.quotarateadjust` |

### 采购宝API (34 APIs)

<details>
<summary>展开查看全部 34 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.pc.order.render` |
| 2 | `taobao.pc.order.create` |
| 3 | `taobao.pc.order.confirm` |
| 4 | `taobao.pc.order.detail` |
| 5 | `taobao.pc.order.list` |
| 6 | `taobao.pc.order.cancel` |
| 7 | `taobao.pc.item.query` |
| 8 | `taobao.pc.item.detail.query` |
| 9 | `taobao.pc.order.received` |
| 10 | `taobao.pc.refund.router` |
| 11 | `taobao.pc.refund.submit` |
| 12 | `taobao.pc.refund.close` |
| 13 | `taobao.pc.refund.return` |
| 14 | `taobao.pc.refund.detail` |
| 15 | `taobao.pc.refund.list` |
| 16 | `taobao.pc.refund.render.query` |
| 17 | `taobao.pc.refund.render.adjust` |
| 18 | `taobao.pc.item.price.query` |
| 19 | `taobao.pc.item.quantity.query` |
| 20 | `taobao.pc.item.status.query` |
| 21 | `taobao.pc.package.detail` |
| 22 | `taobao.pc.bills.query` |
| 23 | `taobao.pc.bills.confirm` |
| 24 | `taobao.pc.invoice.apply` |
| 25 | `taobao.pc.invoice.detail` |
| 26 | `taobao.pc.package.trace` |
| 27 | `taobao.pc.ego.category.level.query` |
| 28 | `taobao.pc.ego.category.query` |
| 29 | `taobao.pc.project.invoice.subject.create` |
| 30 | `taobao.pc.refund.auto.reason.parse` |
| 31 | `taobao.pc.bargain.feedback` |
| 32 | `taobao.pc.bargain.cancel` |
| 33 | `taobao.pc.bargain.create` |
| 34 | `taobao.pc.bargain.candidate.list` |

</details>

### 盒马门店数字化

| # | API名称 |
|---|--------|
| 1 | `alibaba.wdk.shop.shelflife.get` |

### 闲鱼游戏

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.game.report.save` |
| 2 | `alibaba.idle.game.report.upload` |
| 3 | `alibaba.idle.game.report.media.upload` |

### 行业-宠物-API

| # | API名称 |
|---|--------|
| 1 | `taobao.industry.pet.doc.query` |
| 2 | `taobao.industry.pet.doc.add` |
| 3 | `taobao.industry.pet.doc.update` |
| 4 | `taobao.industry.pet.type.query` |
| 5 | `taobao.industry.pet.doc.addalipaydoc` |

### 淘宝服饰

| # | API名称 |
|---|--------|
| 1 | `taobao.industry.image.ai.check` |
| 2 | `taobao.industry.sync.item` |
| 3 | `taobao.industry.change.order` |
| 4 | `taobao.fs.trade.buyer.history.items.query` |
| 5 | `taobao.fs.ww.items.status.query` |

### 采购宝开放API (29 APIs)

<details>
<summary>展开查看全部 29 个API</summary>

| # | API名称 |
|---|--------|
| 1 | `taobao.pc.out.tower.order.detail` |
| 2 | `taobao.pc.out.tower.order.list` |
| 3 | `taobao.pc.out.tower.refund.router` |
| 4 | `taobao.pc.out.tower.refund.render.query` |
| 5 | `taobao.pc.out.tower.refund.render.adjust` |
| 6 | `taobao.pc.out.tower.refund.submit` |
| 7 | `taobao.pc.out.tower.refund.close` |
| 8 | `taobao.pc.out.tower.refund.return` |
| 9 | `taobao.pc.out.tower.refund.detail` |
| 10 | `taobao.pc.out.tower.refund.list` |
| 11 | `taobao.pc.out.tower.order.render` |
| 12 | `taobao.pc.out.tower.order.create` |
| 13 | `taobao.pc.out.tower.order.confirm` |
| 14 | `taobao.pc.out.tower.order.cancel` |
| 15 | `taobao.pc.out.tower.order.received` |
| 16 | `taobao.pc.out.item.query` |
| 17 | `taobao.pc.out.item.detail.query` |
| 18 | `taobao.pc.out.item.status.query` |
| 19 | `taobao.pc.out.item.price.query` |
| 20 | `taobao.pc.out.item.quantity.query` |
| 21 | `taobao.pc.out.tower.package.detail` |
| 22 | `taobao.pc.out.tower.bills.query` |
| 23 | `taobao.pc.out.tower.bills.confirm` |
| 24 | `taobao.pc.out.tower.invoice.apply` |
| 25 | `taobao.pc.out.tower.invoice.detail` |
| 26 | `taobao.pc.out.tower.package.trace` |
| 27 | `taobao.pc.out.ego.category.query` |
| 28 | `taobao.pc.out.ego.category.level.query` |
| 29 | `taobao.pc.out.tower.refund.auto.reason.parse` |

</details>

### 天猫家享行业

| # | API名称 |
|---|--------|
| 1 | `alibaba.industry.waybill.code.apply` |
| 2 | `alibaba.industry.waybill.detail.query` |

### 闲鱼奢品寄卖

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.luxconsign.order.query` |
| 2 | `alibaba.idle.luxconsign.order.perform` |
| 3 | `alibaba.idle.isv.bid.price.query` |

### 补寄API

| # | API名称 |
|---|--------|
| 1 | `tmall.reshipping.agree` |
| 2 | `tmall.reshipping.refuse` |
| 3 | `tmall.reshipping.consigngoods` |
| 4 | `tmall.reshipping.get` |
| 5 | `tmall.reshipping.receive.get` |
| 6 | `tmall.reshipping.message.add` |
| 7 | `tmall.reshipping.messages.get` |
| 8 | `tmall.reshipping.refusereason.get` |

### 闲鱼商业化

| # | API名称 |
|---|--------|
| 1 | `alibaba.idle.ad.audit.submit` |
| 2 | `alibaba.idle.ad.conversion.upload` |

### 灵犀互娱_云智能应用_ADC

| # | API名称 |
|---|--------|
| 1 | `alibaba.lingxi.adc.task.submit` |
| 2 | `alibaba.lingxi.adc.open.task.captchatask.verify` |
| 3 | `alibaba.lingxi.adc.open.task.captchatask.get` |
| 4 | `alibaba.lingxi.adc.open.task.submit` |
| 5 | `alibaba.lingxi.adc.open.cloudgame.lockresource` |

### 三方接入API

| # | API名称 |
|---|--------|
| 1 | `taobao.iphd.users.eligibility.check` |

### 以旧换新订单

| # | API名称 |
|---|--------|
| 1 | `taobao.ofn.idle.order.fulfill` |
| 2 | `taobao.ofn.idle.inspection.report` |
| 3 | `alibaba.ofn.supplier.qcimage.upload` |

### 天猫超市储值卡API

| # | API名称 |
|---|--------|
| 1 | `alibaba.aself.benefitcenter.cardorder.make.finish` |
| 2 | `alibaba.aself.benefitcenter.logistics.company.query` |
| 3 | `alibaba.aself.benefitcenter.cardorder.info.query` |
| 4 | `alibaba.aself.benefitcenter.cardorder.send.finish` |

### 阿里健康-消费医疗-通用toB业务

| # | API名称 |
|---|--------|
| 1 | `alibaba.alihealth.medical.tob.order.submit` |
| 2 | `alibaba.alihealth.medical.tob.report.query` |

### Skill开放

| # | API名称 |
|---|--------|
| 1 | `taobao.top.skill.open.session.status` |
| 2 | `taobao.top.skill.open.session.destroy` |
| 3 | `taobao.top.skill.open.session.create` |
| 4 | `taobao.top.skill.open.chat.submit` |
| 5 | `taobao.top.skill.open.chat.poll` |
| 6 | `taobao.top.skill.open.interaction.reply` |

### 淘宝闪购联盟-闪拼

| # | API名称 |
|---|--------|
| 1 | `alibaba.alsc.groupbuy.order.query` |
| 2 | `alibaba.alsc.groupbuy.refund.order.query` |

### 数字生活

| # | API名称 |
|---|--------|
| 1 | `alibaba.cco.szsh.delivery.notification.send` |
| 2 | `taobao.virtual.hylink.bc.item.manage` |

---

## 二、当前API文档：taobao.appstore.subscribe.get

> 查询appstore应用订购关系
> (对于新上架的多版本应用，建议使用taobao.vas.subscribe.get)
> 不需用户授权

### 公共参数

#### 请求地址

| 环境 | HTTP地址 | HTTPS地址 |
|------|----------|-----------|
| 正式环境 | http://gw.api.taobao.com/router/rest | https://eco.taobao.com/router/rest |

#### 公共请求参数

| 名称 | 类型 | 必须 | 描述 |
|------|------|------|------|
| method | String | 是 | API接口名称，例如:taobao.appstore.subscribe.get |
| app_key | String | 是 | TOP分配给应用的AppKey，例如：12345678 |
| session | String | 否 | 用户登录授权成功后，TOP颁发给应用的授权信息 |
| timestamp | String | 是 | 时间戳，格式为yyyy-MM-dd HH:mm:ss，时区为GMT+8 |
| v | String | 是 | API协议版本，可选值：2.0 |
| sign_method | String | 是 | 签名的摘要算法，可选值为：hmac，md5，hmac-sha256 |
| sign | String | 是 | API输入参数签名结果 |
| format | String | 否 | 响应格式。默认为xml格式，可选值：xml，json |
| simplify | Boolean | 否 | 是否采用精简JSON返回格式，仅当format=json时有效，默认值为：false |

#### 公共响应参数

| 名称 | 类型 | 描述 |
|------|------|------|
| request_id | String | 平台颁发的每次请求访问的唯一标识 |
| error_response | String | 请求访问失败时返回的根节点 |
| code | String | 请求失败返回的错误码 |
| msg | String | 请求失败返回的错误信息 |
| sub_code | String | 请求失败返回的子错误码 |
| sub_msg | String | 请求失败返回的子错误信息 |
| \*\*\*_response | String | 请求成功返回的根节点 |

### 请求参数

| 名称 | 类型 | 必须 | 示例值 | 描述 |
|------|------|------|--------|------|
| nick | String | true | tbtest110 | 用户昵称 |
| lease_id | Number | false | 14192 | 订购插件实例ID |

### 响应参数

| 名称 | 类型 | 示例值 | 描述 |
|------|------|--------|------|
| user_subscribe | UserSubscribe | | 用户订购信息 |
| status | String | subscribeUser | 订购状况。应用订购者：subscribeUser;尚未订购：unsubscribeUser；非法用户：invalidateUser |
| start_date | Date | 2000-01-01 00:00:00 | 订购开始时间。格式:yyyy-MM-dd HH:mm:ss |
| end_date | Date | 2000-01-31 00:00:00 | 订购结束时间。格式:yyyy-MM-dd HH:mm:ss |
| version_no | Number | 1 | 0-无版本信息；1-初级版；2-中级版；3-高级版 |

### 请求示例

#### JAVA

```java
TaobaoClient client = new DefaultTaobaoClient(url, appkey, secret);\nAppstoreSubscribeGetRequest req = new AppstoreSubscribeGetRequest();\nreq.setNick("tbtest110");\nreq.setLeaseId(14192L);\nAppstoreSubscribeGetResponse rsp = client.execute(req);\nSystem.out.println(rsp.getBody());
```

#### PHP

```php
$c = new TopClient;\n$c->appkey = $appkey;\n$c->secretKey = $secret;\n$req = new AppstoreSubscribeGetRequest;\n$req->setNick("tbtest110");\n$req->setLeaseId("14192");\n$resp = $c->execute($req);
```

#### .NET

```csharp
ITopClient client = new DefaultTopClient(url, appkey, secret);\nAppstoreSubscribeGetRequest req = new AppstoreSubscribeGetRequest();\nreq.Nick = "tbtest110";\nreq.LeaseId = 14192L;\nAppstoreSubscribeGetResponse rsp = client.Execute(req);\nConsole.WriteLine(rsp.Body);
```

#### CURL

```bash
curl -X POST 'http://gw.api.taobao.com/router/rest' \\\n-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \\\n-d 'app_key=12129701' \\\n-d 'format=json' \\\n-d 'method=taobao.appstore.subscribe.get' \\\n-d 'partner_id=apidoc' \\\n-d 'sign=469DA26D79C53DAD1B97FE6040EBFEF1' \\\n-d 'sign_method=hmac' \\\n-d 'timestamp=2026-05-16+13%3A54%3A32' \\\n-d 'v=2.0' \\\n-d 'lease_id=14192' \\\n-d 'nick=tbtest110'
```

#### Python

```python
# -*- coding: utf-8 -*-\nimport top.api\n\nreq=top.api.AppstoreSubscribeGetRequest(url,port)\nreq.set_app_info(top.appinfo(appkey,secret))\n\nreq.nick="tbtest110"\nreq.lease_id=14192\ntry:\n\tresp= req.getResponse()\n\tprint(resp)\nexcept Exception,e:\n\tprint(e)\n
```

#### NodeJS

```javascript
TopClient = require('./topClient').TopClient;\nvar client = new TopClient({\n\t'appkey': 'appkey',\n\t'appsecret': 'secret',\n\t'url': 'http://gw.api.taobao.com/router/rest'\n});\n\nclient.execute('taobao.appstore.subscribe.get', {\n\t'nick':'tbtest110',\n\t'lease_id':'14192'\n}, function(error, response) {\n\tif (!error) console.log(response);\n\telse console.log(error);\n})\n
```

#### C/C++

```c
pTopRequest pRequest = alloc_top_request();\npTopResponse pResponse = NULL;\npTaobaoClient pClient = alloc_taobao_client(url, appkey, appsecret);\nset_api_name(pRequest,"taobao.appstore.subscribe.get");\nadd_param(pRequest,"nick","tbtest110");\nadd_param(pRequest,"lease_id","14192");\npResponse = top_execute(pClient,pRequest,NULL);\nprintf("ret code:%d\\n",pResponse->code);\nif(pResponse->code == 0){\n\tpTopResponseIterator ite = init_response_iterator(pResponse);\n\tpResultItem pResultItem = alloc_result_item();\n\twhile(parseNext(ite, pResultItem) == 0){\n\t\tprintf("%s:%s\\n",pResultItem->key,pResultItem->value);\n\t}\n\tdestroy_response_iterator(ite);\n\tdestroy_result_item(pResultItem);\n}\ndestroy_top_request(pRequest);\ndestroy_top_response(pResponse);\ndestroy_taobao_client(pClient);\n
```

#### Python3

```python
from datetime import datetime\nfrom topsdk.client import TopApiClient,TopException\nfrom topsdk.defaultability.defaultability import Defaultability\nfrom topsdk.defaultability.request.taobao_appstore_subscribe_get_request import *\n\nif __name__ == '__main__':\n    # create Client\n    client = TopApiClient(appkey='<your-appkey>', app_sercet='<your-appsecret>', top_gateway_url='<top-gateway-url>',verify_ssl=False)\n    ability = Defaultability(client=client)\n\n    # create domain\n\n    # create request\n    request = TaobaoAppstoreSubscribeGetRequest()\n    request.nick = 'tbtest110'\n    request.lease_id = 14192\n    try:\n        response = ability.taobao_appstore_subscribe_get(request)\n        print(response)\n    except TopException as e:\n        print(e)\n
```

#### GO

```go
package main;\n\nimport (\n    "fmt"\n    "topsdk"\n    "topsdk/defaultability"\n    "topsdk/defaultability/request"\n)\n\nfunc main() {\n    client := topsdk.NewDefaultTopClient("<your-appkey>","<your-appsecret>","<top-gateway-url>",20000,20000)\n    ability := defaultability.NewDefaultability(&client)\n\n\n    req := request.TaobaoAppstoreSubscribeGetRequest{}\n    req.SetNick("tbtest110")\n    req.SetLeaseId(14192)\n\n\n    resp, err := ability.TaobaoAppstoreSubscribeGet(&req)\n    if(err != nil) {\n        fmt.Println(err)\n    } else {\n        fmt.Println(resp.Body)\n    }\n}\n\n
```

#### PHP7

```php
<?php\nrequire "../vendor/autoload.php";\nuse Topsdk\\Topapi\\TopApiClient;\nuse Topsdk\\Topapi\\Defaultability\\Request\\TaobaoAppstoreSubscribeGetRequest;\nuse Topsdk\\Topapi\\Defaultability\\Defaultability;\n\n\n// create Client\n$client = new TopApiClient("<your-appkey>","<your-appsecret>","<top-gateway-url>");\n$ability = new Defaultability($client);\n\n// create domain\n\n// create request\n$request = new TaobaoAppstoreSubscribeGetRequest();\n$request->setNick("tbtest110");\n$request->setLeaseId(14192);\n\n$response = $ability->taobaoAppstoreSubscribeGet($request);\nvar_dump($response);\n\n
```

#### JAVA8

```java
import com.alibaba.fastjson.JSON;\nimport java.io.File;\nimport java.util.ArrayList;\nimport java.util.Date;\nimport com.taobao.top.TopApiClient;\nimport com.taobao.top.DefaultTopApiClient;\nimport com.taobao.top.TopFileItem;\nimport com.taobao.top.defaultability.Defaultability;\nimport com.taobao.top.defaultability.request.TaobaoAppstoreSubscribeGetRequest;\nimport com.taobao.top.defaultability.response.TaobaoAppstoreSubscribeGetResponse;\n\npublic class Main {\n\n    public static void main(String[] args) throws Exception {\n        // create Client\n        TopApiClient client = new DefaultTopApiClient("<your-appkey>","<your-appsecret>","<top-gateway-url>");\n        Defaultability apiPackage = new Defaultability(client);\n        // create domain\n\n        // create request\n        TaobaoAppstoreSubscribeGetRequest request = new TaobaoAppstoreSubscribeGetRequest();\n        request.setNick("tbtest110");\n        request.setLeaseId(14192);\n\n        TaobaoAppstoreSubscribeGetResponse response = apiPackage.taobaoAppstoreSubscribeGet(request);\n        if(!response.isSuccess()){\n            System.out.println(response.getSubMsg());\n        }\n        System.out.println(JSON.toJSONString(response));\n    }\n\n}
```

#### .NET6

```csharp
using System;\nusing System.Collections.Generic;\nusing Topsdk.Top;\nusing Topsdk.Top.Defaultability;\nusing Topsdk.Top.Defaultability.Request;\nusing Topsdk.Util;\n\n\nnamespace MyNamespace\n{\n    class MyClass\n    {\n        static void Main(string[] args)\n        {\n            // create Client\n            ITopApiClient client = new DefaultTopApiClient("<your-appkey>","<your-appsecret>","<top-gateway-url>",10000,20000);\n            Defaultability apiPackage = new Defaultability(client);\n\n\n            // create request\n            var request = new TaobaoAppstoreSubscribeGetRequest();\n            request.Nick = "tbtest110";\n            request.LeaseId = 14192;\n\n            var response = apiPackage.TaobaoAppstoreSubscribeGet(request);\n            if (response.isSuccess())\n            {\n                Console.WriteLine(response.Body);\n            }\n            else\n            {\n                Console.WriteLine(response.SubCode);\n            }\n\n        }\n    }\n}
```

### 响应示例

#### XML

```xml
<appstore_subscribe_get_response>\n    <user_subscribe>\n        <status>subscribeUser</status>\n        <start_date>2000-01-01 00:00:00</start_date>\n        <end_date>2000-01-31 00:00:00</end_date>\n        <version_no>1</version_no>\n    </user_subscribe>\n</appstore_subscribe_get_response>
```

#### JSON

```json
{\n    "appstore_subscribe_get_response":{\n        "user_subscribe":{\n            "status":"subscribeUser",\n            "start_date":"2000-01-01 00:00:00",\n            "end_date":"2000-01-31 00:00:00",\n            "version_no":1\n        }\n    }\n}
```

### 异常示例

#### XML

```xml
<error_response>\n    <code>50</code>\n    <msg>Remote service error</msg>\n    <sub_code>isv.invalid-parameter</sub_code>\n    <sub_msg>非法参数</sub_msg>\n</error_response>
```

#### JSON

```json
{\n\t"error_response":{\n\t\t"msg":"Remote service error",\n\t\t"code":50,\n\t\t"sub_msg":"非法参数",\n\t\t"sub_code":"isv.invalid-parameter"\n\t}\n}
```

### 错误码解释

| 错误码 | 错误消息 | 解决方案 |
|--------|----------|----------|
| 没有数据 | 没有数据 | - |

### API 工具

- [API测试工具](https://open.taobao.com/new/apitesttool?apiName=taobao.appstore.subscribe.get)
- [错误码查询工具](https://open.taobao.com/doc.htm?docId=1&docType=18)
- [SDK 下载](https://open.taobao.com/doc.htm?docId=101618&docType=1)

### 如何获得此API

| 拥有此API的权限组 | 可获得/可申请此API权限组的应用类型 |
|-------------------|-------------------------------------|
| (新)服务平台基础包 | 多种应用类型，包括商家后台系统、营销导购、客服工具、ERP软件等（共100+种应用类型） |

---

*本文档通过自动抓取自淘宝开放平台API文档生成*
*来源: https://open.taobao.com/api.htm?docId=285&docType=2*