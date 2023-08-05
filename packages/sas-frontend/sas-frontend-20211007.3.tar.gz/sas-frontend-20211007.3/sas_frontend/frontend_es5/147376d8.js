/*! For license information please see 147376d8.js.LICENSE.txt */
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[2179],{79332:function(n,e,t){t.d(e,{a:function(){return i}});t(94604);var i={properties:{animationConfig:{type:Object},entryAnimation:{observer:"_entryAnimationChanged",type:String},exitAnimation:{observer:"_exitAnimationChanged",type:String}},_entryAnimationChanged:function(){this.animationConfig=this.animationConfig||{},this.animationConfig.entry=[{name:this.entryAnimation,node:this}]},_exitAnimationChanged:function(){this.animationConfig=this.animationConfig||{},this.animationConfig.exit=[{name:this.exitAnimation,node:this}]},_copyProperties:function(n,e){for(var t in e)n[t]=e[t]},_cloneConfig:function(n){var e={isClone:!0};return this._copyProperties(e,n),e},_getAnimationConfigRecursive:function(n,e,t){var i;if(this.animationConfig)if(this.animationConfig.value&&"function"==typeof this.animationConfig.value)this._warn(this._logf("playAnimation","Please put 'animationConfig' inside of your components 'properties' object instead of outside of it."));else if(i=n?this.animationConfig[n]:this.animationConfig,Array.isArray(i)||(i=[i]),i)for(var o,a=0;o=i[a];a++)if(o.animatable)o.animatable._getAnimationConfigRecursive(o.type||n,e,t);else if(o.id){var r=e[o.id];r?(r.isClone||(e[o.id]=this._cloneConfig(r),r=e[o.id]),this._copyProperties(r,o)):e[o.id]=o}else t.push(o)},getAnimationConfig:function(n){var e={},t=[];for(var i in this._getAnimationConfigRecursive(n,e,t),e)t.push(e[i]);return t}}},96540:function(n,e,t){t.d(e,{t:function(){return o}});t(94604);var i={_configureAnimations:function(n){var e=[],t=[];if(n.length>0)for(var i,o=0;i=n[o];o++){var a=document.createElement(i.name);if(a.isNeonAnimation){var r;a.configure||(a.configure=function(n){return null}),r=a.configure(i),t.push({result:r,config:i,neonAnimation:a})}else console.warn(this.is+":",i.name,"not found!")}for(var s=0;s<t.length;s++){var l=t[s].result,c=t[s].config,u=t[s].neonAnimation;try{"function"!=typeof l.cancel&&(l=document.timeline.play(l))}catch(p){l=null,console.warn("Couldnt play","(",c.name,").",p)}l&&e.push({neonAnimation:u,config:c,animation:l})}return e},_shouldComplete:function(n){for(var e=!0,t=0;t<n.length;t++)if("finished"!=n[t].animation.playState){e=!1;break}return e},_complete:function(n){for(var e=0;e<n.length;e++)n[e].neonAnimation.complete(n[e].config);for(e=0;e<n.length;e++)n[e].animation.cancel()},playAnimation:function(n,e){var t=this.getAnimationConfig(n);if(t){this._active=this._active||{},this._active[n]&&(this._complete(this._active[n]),delete this._active[n]);var i=this._configureAnimations(t);if(0!=i.length){this._active[n]=i;for(var o=0;o<i.length;o++)i[o].animation.onfinish=function(){this._shouldComplete(i)&&(this._complete(i),delete this._active[n],this.fire("neon-animation-finish",e,{bubbles:!1}))}.bind(this)}else this.fire("neon-animation-finish",e,{bubbles:!1})}},cancelAnimation:function(){for(var n in this._active){var e=this._active[n];for(var t in e)e[t].animation.cancel()}this._active={}}},o=[t(79332).a,i]},51654:function(n,e,t){t.d(e,{Z:function(){return a},n:function(){return r}});t(94604);var i=t(75009),o=t(87156),a={hostAttributes:{role:"dialog",tabindex:"-1"},properties:{modal:{type:Boolean,value:!1},__readied:{type:Boolean,value:!1}},observers:["_modalChanged(modal, __readied)"],listeners:{tap:"_onDialogClick"},ready:function(){this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.__readied=!0},_modalChanged:function(n,e){e&&(n?(this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.noCancelOnOutsideClick=!0,this.noCancelOnEscKey=!0,this.withBackdrop=!0):(this.noCancelOnOutsideClick=this.noCancelOnOutsideClick&&this.__prevNoCancelOnOutsideClick,this.noCancelOnEscKey=this.noCancelOnEscKey&&this.__prevNoCancelOnEscKey,this.withBackdrop=this.withBackdrop&&this.__prevWithBackdrop))},_updateClosingReasonConfirmed:function(n){this.closingReason=this.closingReason||{},this.closingReason.confirmed=n},_onDialogClick:function(n){for(var e=(0,o.vz)(n).path,t=0,i=e.indexOf(this);t<i;t++){var a=e[t];if(a.hasAttribute&&(a.hasAttribute("dialog-dismiss")||a.hasAttribute("dialog-confirm"))){this._updateClosingReasonConfirmed(a.hasAttribute("dialog-confirm")),this.close(),n.stopPropagation();break}}}},r=[i.$,a]},50808:function(n,e,t){t(94604),t(65660),t(1656),t(47686),t(54242);var i=document.createElement("template");i.setAttribute("style","display: none;"),i.innerHTML='<dom-module id="paper-dialog-shared-styles">\n  <template>\n    <style>\n      :host {\n        display: block;\n        margin: 24px 40px;\n\n        background: var(--paper-dialog-background-color, var(--primary-background-color));\n        color: var(--paper-dialog-color, var(--primary-text-color));\n\n        @apply --paper-font-body1;\n        @apply --shadow-elevation-16dp;\n        @apply --paper-dialog;\n      }\n\n      :host > ::slotted(*) {\n        margin-top: 20px;\n        padding: 0 24px;\n      }\n\n      :host > ::slotted(.no-padding) {\n        padding: 0;\n      }\n\n      \n      :host > ::slotted(*:first-child) {\n        margin-top: 24px;\n      }\n\n      :host > ::slotted(*:last-child) {\n        margin-bottom: 24px;\n      }\n\n      /* In 1.x, this selector was `:host > ::content h2`. In 2.x <slot> allows\n      to select direct children only, which increases the weight of this\n      selector, so we have to re-define first-child/last-child margins below. */\n      :host > ::slotted(h2) {\n        position: relative;\n        margin: 0;\n\n        @apply --paper-font-title;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-top. */\n      :host > ::slotted(h2:first-child) {\n        margin-top: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-bottom. */\n      :host > ::slotted(h2:last-child) {\n        margin-bottom: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      :host > ::slotted(.paper-dialog-buttons),\n      :host > ::slotted(.buttons) {\n        position: relative;\n        padding: 8px 8px 8px 24px;\n        margin: 0;\n\n        color: var(--paper-dialog-button-color, var(--primary-color));\n\n        @apply --layout-horizontal;\n        @apply --layout-end-justified;\n      }\n    </style>\n  </template>\n</dom-module>',document.head.appendChild(i.content);var o,a,r,s=t(96540),l=t(51654),c=t(9672),u=t(50856);(0,c.k)({_template:(0,u.d)(o||(a=['\n    <style include="paper-dialog-shared-styles"></style>\n    <slot></slot>\n'],r||(r=a.slice(0)),o=Object.freeze(Object.defineProperties(a,{raw:{value:Object.freeze(r)}})))),is:"paper-dialog",behaviors:[l.n,s.t],listeners:{"neon-animation-finish":"_onNeonAnimationFinish"},_renderOpened:function(){this.cancelAnimation(),this.playAnimation("entry")},_renderClosed:function(){this.cancelAnimation(),this.playAnimation("exit")},_onNeonAnimationFinish:function(){this.opened?this._finishRenderOpened():this._finishRenderClosed()}})},28417:function(n,e,t){t(50808);var i=t(33367),o=t(93592),a=t(87156),r={getTabbableNodes:function(n){var e=[];return this._collectTabbableNodes(n,e)?o.H._sortByTabIndex(e):e},_collectTabbableNodes:function(n,e){if(n.nodeType!==Node.ELEMENT_NODE||!o.H._isVisible(n))return!1;var t,i=n,r=o.H._normalizedTabIndex(i),s=r>0;r>=0&&e.push(i),t="content"===i.localName||"slot"===i.localName?(0,a.vz)(i).getDistributedNodes():(0,a.vz)(i.shadowRoot||i.root||i).children;for(var l=0;l<t.length;l++)s=this._collectTabbableNodes(t[l],e)||s;return s}};function s(n){return s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(n){return typeof n}:function(n){return n&&"function"==typeof Symbol&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n},s(n)}function l(n,e){if(!(n instanceof e))throw new TypeError("Cannot call a class as a function")}function c(n,e){return c=Object.setPrototypeOf||function(n,e){return n.__proto__=e,n},c(n,e)}function u(n){var e=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(n){return!1}}();return function(){var t,i=d(n);if(e){var o=d(this).constructor;t=Reflect.construct(i,arguments,o)}else t=i.apply(this,arguments);return p(this,t)}}function p(n,e){if(e&&("object"===s(e)||"function"==typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return function(n){if(void 0===n)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return n}(n)}function d(n){return d=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},d(n)}var f=customElements.get("paper-dialog"),h={get _focusableNodes(){return r.getTabbableNodes(this)}},m=function(n){!function(n,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");n.prototype=Object.create(e&&e.prototype,{constructor:{value:n,writable:!0,configurable:!0}}),e&&c(n,e)}(t,n);var e=u(t);function t(){return l(this,t),e.apply(this,arguments)}return t}((0,i.P)([h],f));customElements.define("ha-paper-dialog",m)},22179:function(n,e,t){t.r(e);t(53918);var i,o=t(50856),a=t(28426),r=(t(28417),t(31206),t(1265));t(36436);function s(n){return s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(n){return typeof n}:function(n){return n&&"function"==typeof Symbol&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n},s(n)}function l(n,e){if(!(n instanceof e))throw new TypeError("Cannot call a class as a function")}function c(n,e){for(var t=0;t<e.length;t++){var i=e[t];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(n,i.key,i)}}function u(n,e){return u=Object.setPrototypeOf||function(n,e){return n.__proto__=e,n},u(n,e)}function p(n){var e=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(n){return!1}}();return function(){var t,i=f(n);if(e){var o=f(this).constructor;t=Reflect.construct(i,arguments,o)}else t=i.apply(this,arguments);return d(this,t)}}function d(n,e){if(e&&("object"===s(e)||"function"==typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return function(n){if(void 0===n)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return n}(n)}function f(n){return f=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},f(n)}var h=function(n){!function(n,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");n.prototype=Object.create(e&&e.prototype,{constructor:{value:n,writable:!0,configurable:!0}}),e&&u(n,e)}(s,n);var e,t,a,r=p(s);function s(){return l(this,s),r.apply(this,arguments)}return e=s,a=[{key:"template",get:function(){return(0,o.d)(i||(n=['\n      <style include="ha-style-dialog">\n        .error {\n          color: red;\n        }\n        @media all and (max-width: 500px) {\n          ha-paper-dialog {\n            margin: 0;\n            width: 100%;\n            max-height: calc(100% - var(--header-height));\n\n            position: fixed !important;\n            bottom: 0px;\n            left: 0px;\n            right: 0px;\n            overflow: scroll;\n            border-bottom-left-radius: 0px;\n            border-bottom-right-radius: 0px;\n          }\n        }\n\n        ha-paper-dialog {\n          border-radius: 2px;\n        }\n        ha-paper-dialog p {\n          color: var(--secondary-text-color);\n        }\n\n        .icon {\n          float: right;\n        }\n      </style>\n      <ha-paper-dialog\n        id="mp3dialog"\n        with-backdrop\n        opened="{{_opened}}"\n        on-opened-changed="_openedChanged"\n      >\n        <h2>\n          [[localize(\'ui.panel.mailbox.playback_title\')]]\n          <div class="icon">\n            <template is="dom-if" if="[[_loading]]">\n              <ha-circular-progress active></ha-circular-progress>\n            </template>\n            <ha-icon-button\n              id="delicon"\n              on-click="openDeleteDialog"\n              icon="hass:delete"\n            ></ha-icon-button>\n          </div>\n        </h2>\n        <div id="transcribe"></div>\n        <div>\n          <template is="dom-if" if="[[_errorMsg]]">\n            <div class="error">[[_errorMsg]]</div>\n          </template>\n          <audio id="mp3" preload="none" controls>\n            <source id="mp3src" src="" type="audio/mpeg" />\n          </audio>\n        </div>\n      </ha-paper-dialog>\n    '],e||(e=n.slice(0)),i=Object.freeze(Object.defineProperties(n,{raw:{value:Object.freeze(e)}}))));var n,e}},{key:"properties",get:function(){return{hass:Object,_currentMessage:Object,_errorMsg:String,_loading:{type:Boolean,value:!1},_opened:{type:Boolean,value:!1}}}}],(t=[{key:"showDialog",value:function(n){var e=this,t=n.hass,i=n.message;this.hass=t,this._errorMsg=null,this._currentMessage=i,this._opened=!0,this.$.transcribe.innerText=i.message;var o=i.platform,a=this.$.mp3;if(o.has_media){a.style.display="",this._showLoading(!0),a.src=null;var r="/api/mailbox/media/".concat(o.name,"/").concat(i.sha);this.hass.fetchWithAuth(r).then((function(n){return n.ok?n.blob():Promise.reject({status:n.status,statusText:n.statusText})})).then((function(n){e._showLoading(!1),a.src=window.URL.createObjectURL(n),a.play()})).catch((function(n){e._showLoading(!1),e._errorMsg="Error loading audio: ".concat(n.statusText)}))}else a.style.display="none",this._showLoading(!1)}},{key:"openDeleteDialog",value:function(){confirm(this.localize("ui.panel.mailbox.delete_prompt"))&&this.deleteSelected()}},{key:"deleteSelected",value:function(){var n=this._currentMessage;this.hass.callApi("DELETE","mailbox/delete/".concat(n.platform.name,"/").concat(n.sha)),this._dialogDone()}},{key:"_dialogDone",value:function(){this.$.mp3.pause(),this.setProperties({_currentMessage:null,_errorMsg:null,_loading:!1,_opened:!1})}},{key:"_openedChanged",value:function(n){n.detail.value||this._dialogDone()}},{key:"_showLoading",value:function(n){var e=this.$.delicon;if(n)this._loading=!0,e.style.display="none";else{var t=this._currentMessage.platform;this._loading=!1,e.style.display=t.can_delete?"":"none"}}}])&&c(e.prototype,t),a&&c(e,a),s}((0,r.Z)(a.H3));customElements.define("ha-dialog-show-audio-message",h)},36436:function(n,e,t){t(21384);var i=t(11654),o=document.createElement("template");o.setAttribute("style","display: none;"),o.innerHTML='<dom-module id="ha-style-dialog">\n<template>\n  <style>\n    '.concat(i.yu.cssText,"\n  </style>\n</template>\n</dom-module>"),document.head.appendChild(o.content)}}]);