/*! For license information please see 58f3802f.js.LICENSE.txt */
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[242],{21157:function(n,e,t){var l;t(94604);var i,a,o=(0,t(50856).d)(l||(i=['\n/* Most common used flex styles*/\n<dom-module id="iron-flex">\n  <template>\n    <style>\n      .layout.horizontal,\n      .layout.vertical {\n        display: -ms-flexbox;\n        display: -webkit-flex;\n        display: flex;\n      }\n\n      .layout.inline {\n        display: -ms-inline-flexbox;\n        display: -webkit-inline-flex;\n        display: inline-flex;\n      }\n\n      .layout.horizontal {\n        -ms-flex-direction: row;\n        -webkit-flex-direction: row;\n        flex-direction: row;\n      }\n\n      .layout.vertical {\n        -ms-flex-direction: column;\n        -webkit-flex-direction: column;\n        flex-direction: column;\n      }\n\n      .layout.wrap {\n        -ms-flex-wrap: wrap;\n        -webkit-flex-wrap: wrap;\n        flex-wrap: wrap;\n      }\n\n      .layout.no-wrap {\n        -ms-flex-wrap: nowrap;\n        -webkit-flex-wrap: nowrap;\n        flex-wrap: nowrap;\n      }\n\n      .layout.center,\n      .layout.center-center {\n        -ms-flex-align: center;\n        -webkit-align-items: center;\n        align-items: center;\n      }\n\n      .layout.center-justified,\n      .layout.center-center {\n        -ms-flex-pack: center;\n        -webkit-justify-content: center;\n        justify-content: center;\n      }\n\n      .flex {\n        -ms-flex: 1 1 0.000000001px;\n        -webkit-flex: 1;\n        flex: 1;\n        -webkit-flex-basis: 0.000000001px;\n        flex-basis: 0.000000001px;\n      }\n\n      .flex-auto {\n        -ms-flex: 1 1 auto;\n        -webkit-flex: 1 1 auto;\n        flex: 1 1 auto;\n      }\n\n      .flex-none {\n        -ms-flex: none;\n        -webkit-flex: none;\n        flex: none;\n      }\n    </style>\n  </template>\n</dom-module>\n/* Basic flexbox reverse styles */\n<dom-module id="iron-flex-reverse">\n  <template>\n    <style>\n      .layout.horizontal-reverse,\n      .layout.vertical-reverse {\n        display: -ms-flexbox;\n        display: -webkit-flex;\n        display: flex;\n      }\n\n      .layout.horizontal-reverse {\n        -ms-flex-direction: row-reverse;\n        -webkit-flex-direction: row-reverse;\n        flex-direction: row-reverse;\n      }\n\n      .layout.vertical-reverse {\n        -ms-flex-direction: column-reverse;\n        -webkit-flex-direction: column-reverse;\n        flex-direction: column-reverse;\n      }\n\n      .layout.wrap-reverse {\n        -ms-flex-wrap: wrap-reverse;\n        -webkit-flex-wrap: wrap-reverse;\n        flex-wrap: wrap-reverse;\n      }\n    </style>\n  </template>\n</dom-module>\n/* Flexbox alignment */\n<dom-module id="iron-flex-alignment">\n  <template>\n    <style>\n      /**\n       * Alignment in cross axis.\n       */\n      .layout.start {\n        -ms-flex-align: start;\n        -webkit-align-items: flex-start;\n        align-items: flex-start;\n      }\n\n      .layout.center,\n      .layout.center-center {\n        -ms-flex-align: center;\n        -webkit-align-items: center;\n        align-items: center;\n      }\n\n      .layout.end {\n        -ms-flex-align: end;\n        -webkit-align-items: flex-end;\n        align-items: flex-end;\n      }\n\n      .layout.baseline {\n        -ms-flex-align: baseline;\n        -webkit-align-items: baseline;\n        align-items: baseline;\n      }\n\n      /**\n       * Alignment in main axis.\n       */\n      .layout.start-justified {\n        -ms-flex-pack: start;\n        -webkit-justify-content: flex-start;\n        justify-content: flex-start;\n      }\n\n      .layout.center-justified,\n      .layout.center-center {\n        -ms-flex-pack: center;\n        -webkit-justify-content: center;\n        justify-content: center;\n      }\n\n      .layout.end-justified {\n        -ms-flex-pack: end;\n        -webkit-justify-content: flex-end;\n        justify-content: flex-end;\n      }\n\n      .layout.around-justified {\n        -ms-flex-pack: distribute;\n        -webkit-justify-content: space-around;\n        justify-content: space-around;\n      }\n\n      .layout.justified {\n        -ms-flex-pack: justify;\n        -webkit-justify-content: space-between;\n        justify-content: space-between;\n      }\n\n      /**\n       * Self alignment.\n       */\n      .self-start {\n        -ms-align-self: flex-start;\n        -webkit-align-self: flex-start;\n        align-self: flex-start;\n      }\n\n      .self-center {\n        -ms-align-self: center;\n        -webkit-align-self: center;\n        align-self: center;\n      }\n\n      .self-end {\n        -ms-align-self: flex-end;\n        -webkit-align-self: flex-end;\n        align-self: flex-end;\n      }\n\n      .self-stretch {\n        -ms-align-self: stretch;\n        -webkit-align-self: stretch;\n        align-self: stretch;\n      }\n\n      .self-baseline {\n        -ms-align-self: baseline;\n        -webkit-align-self: baseline;\n        align-self: baseline;\n      }\n\n      /**\n       * multi-line alignment in main axis.\n       */\n      .layout.start-aligned {\n        -ms-flex-line-pack: start;  /* IE10 */\n        -ms-align-content: flex-start;\n        -webkit-align-content: flex-start;\n        align-content: flex-start;\n      }\n\n      .layout.end-aligned {\n        -ms-flex-line-pack: end;  /* IE10 */\n        -ms-align-content: flex-end;\n        -webkit-align-content: flex-end;\n        align-content: flex-end;\n      }\n\n      .layout.center-aligned {\n        -ms-flex-line-pack: center;  /* IE10 */\n        -ms-align-content: center;\n        -webkit-align-content: center;\n        align-content: center;\n      }\n\n      .layout.between-aligned {\n        -ms-flex-line-pack: justify;  /* IE10 */\n        -ms-align-content: space-between;\n        -webkit-align-content: space-between;\n        align-content: space-between;\n      }\n\n      .layout.around-aligned {\n        -ms-flex-line-pack: distribute;  /* IE10 */\n        -ms-align-content: space-around;\n        -webkit-align-content: space-around;\n        align-content: space-around;\n      }\n    </style>\n  </template>\n</dom-module>\n/* Non-flexbox positioning helper styles */\n<dom-module id="iron-flex-factors">\n  <template>\n    <style>\n      .flex,\n      .flex-1 {\n        -ms-flex: 1 1 0.000000001px;\n        -webkit-flex: 1;\n        flex: 1;\n        -webkit-flex-basis: 0.000000001px;\n        flex-basis: 0.000000001px;\n      }\n\n      .flex-2 {\n        -ms-flex: 2;\n        -webkit-flex: 2;\n        flex: 2;\n      }\n\n      .flex-3 {\n        -ms-flex: 3;\n        -webkit-flex: 3;\n        flex: 3;\n      }\n\n      .flex-4 {\n        -ms-flex: 4;\n        -webkit-flex: 4;\n        flex: 4;\n      }\n\n      .flex-5 {\n        -ms-flex: 5;\n        -webkit-flex: 5;\n        flex: 5;\n      }\n\n      .flex-6 {\n        -ms-flex: 6;\n        -webkit-flex: 6;\n        flex: 6;\n      }\n\n      .flex-7 {\n        -ms-flex: 7;\n        -webkit-flex: 7;\n        flex: 7;\n      }\n\n      .flex-8 {\n        -ms-flex: 8;\n        -webkit-flex: 8;\n        flex: 8;\n      }\n\n      .flex-9 {\n        -ms-flex: 9;\n        -webkit-flex: 9;\n        flex: 9;\n      }\n\n      .flex-10 {\n        -ms-flex: 10;\n        -webkit-flex: 10;\n        flex: 10;\n      }\n\n      .flex-11 {\n        -ms-flex: 11;\n        -webkit-flex: 11;\n        flex: 11;\n      }\n\n      .flex-12 {\n        -ms-flex: 12;\n        -webkit-flex: 12;\n        flex: 12;\n      }\n    </style>\n  </template>\n</dom-module>\n<dom-module id="iron-positioning">\n  <template>\n    <style>\n      .block {\n        display: block;\n      }\n\n      [hidden] {\n        display: none !important;\n      }\n\n      .invisible {\n        visibility: hidden !important;\n      }\n\n      .relative {\n        position: relative;\n      }\n\n      .fit {\n        position: absolute;\n        top: 0;\n        right: 0;\n        bottom: 0;\n        left: 0;\n      }\n\n      body.fullbleed {\n        margin: 0;\n        height: 100vh;\n      }\n\n      .scroll {\n        -webkit-overflow-scrolling: touch;\n        overflow: auto;\n      }\n\n      /* fixed position */\n      .fixed-bottom,\n      .fixed-left,\n      .fixed-right,\n      .fixed-top {\n        position: fixed;\n      }\n\n      .fixed-top {\n        top: 0;\n        left: 0;\n        right: 0;\n      }\n\n      .fixed-right {\n        top: 0;\n        right: 0;\n        bottom: 0;\n      }\n\n      .fixed-bottom {\n        right: 0;\n        bottom: 0;\n        left: 0;\n      }\n\n      .fixed-left {\n        top: 0;\n        bottom: 0;\n        left: 0;\n      }\n    </style>\n  </template>\n</dom-module>\n'],a||(a=i.slice(0)),l=Object.freeze(Object.defineProperties(i,{raw:{value:Object.freeze(a)}}))));o.setAttribute("style","display: none;"),document.head.appendChild(o.content)},33760:function(n,e,t){t.d(e,{U:function(){return a}});t(94604);var l=t(51644),i=t(26110),a=[l.P,i.a,{hostAttributes:{role:"option",tabindex:"0"}}]},97968:function(n,e,t){t(65660),t(15495),t(1656),t(47686);var l=document.createElement("template");l.setAttribute("style","display: none;"),l.innerHTML="<dom-module id=\"paper-item-shared-styles\">\n  <template>\n    <style>\n      :host, .paper-item {\n        display: block;\n        position: relative;\n        min-height: var(--paper-item-min-height, 48px);\n        padding: 0px 16px;\n      }\n\n      .paper-item {\n        @apply --paper-font-subhead;\n        border:none;\n        outline: none;\n        background: white;\n        width: 100%;\n        text-align: left;\n      }\n\n      :host([hidden]), .paper-item[hidden] {\n        display: none !important;\n      }\n\n      :host(.iron-selected), .paper-item.iron-selected {\n        font-weight: var(--paper-item-selected-weight, bold);\n\n        @apply --paper-item-selected;\n      }\n\n      :host([disabled]), .paper-item[disabled] {\n        color: var(--paper-item-disabled-color, var(--disabled-text-color));\n\n        @apply --paper-item-disabled;\n      }\n\n      :host(:focus), .paper-item:focus {\n        position: relative;\n        outline: 0;\n\n        @apply --paper-item-focused;\n      }\n\n      :host(:focus):before, .paper-item:focus:before {\n        @apply --layout-fit;\n\n        background: currentColor;\n        content: '';\n        opacity: var(--dark-divider-opacity);\n        pointer-events: none;\n\n        @apply --paper-item-focused-before;\n      }\n    </style>\n  </template>\n</dom-module>",document.head.appendChild(l.content)},53973:function(n,e,t){t(94604),t(65660),t(97968);var l,i,a,o=t(9672),s=t(50856),r=t(33760);(0,o.k)({_template:(0,s.d)(l||(i=['\n    <style include="paper-item-shared-styles">\n      :host {\n        @apply --layout-horizontal;\n        @apply --layout-center;\n        @apply --paper-font-subhead;\n\n        @apply --paper-item;\n      }\n    </style>\n    <slot></slot>\n'],a||(a=i.slice(0)),l=Object.freeze(Object.defineProperties(i,{raw:{value:Object.freeze(a)}})))),is:"paper-item",behaviors:[r.U]})},51095:function(n,e,t){t(94604),t(1656);var l,i,a,o=t(78161),s=t(9672),r=t(50856);(0,s.k)({_template:(0,r.d)(l||(i=["\n    <style>\n      :host {\n        display: block;\n        padding: 8px 0;\n\n        background: var(--paper-listbox-background-color, var(--primary-background-color));\n        color: var(--paper-listbox-color, var(--primary-text-color));\n\n        @apply --paper-listbox;\n      }\n    </style>\n\n    <slot></slot>\n"],a||(a=i.slice(0)),l=Object.freeze(Object.defineProperties(i,{raw:{value:Object.freeze(a)}})))),is:"paper-listbox",behaviors:[o.i],hostAttributes:{role:"listbox"}})}}]);