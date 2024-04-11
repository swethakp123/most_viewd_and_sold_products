/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

publicWidget.registry.soldproducts = publicWidget.Widget.extend({
       selector: '.sold_products_snippet',
       start: function() {
       var self = this

        jsonrpc('/most_sold_products').then( function (data){
                data[0].is_active=true
                self.$el.find('#sold_products').html(renderToElement("sold_products.sold_snippet_carousel",{data:data}))

        })

    },
});

publicWidget.registry.viewedproducts = publicWidget.Widget.extend({
       selector: '.viewed_products_snippet',
       start: function() {
       var self = this

        jsonrpc('/most_viewed_products').then( function (data){
                data[0].is_active=true
                self.$el.find('#view_products').html(renderToElement("viewed_products.view_snippet_carousel",{data:data}))

        })

    },
});