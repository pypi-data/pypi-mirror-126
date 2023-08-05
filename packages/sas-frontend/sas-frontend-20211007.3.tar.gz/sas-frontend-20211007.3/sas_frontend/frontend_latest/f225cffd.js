/*! For license information please see f225cffd.js.LICENSE.txt */
"use strict";(self.webpackChunksas_frontend=self.webpackChunksas_frontend||[]).push([[89841],{89841:(e,r,o)=>{o.d(r,{Y:()=>f});var d=o(87480),t=o(32207),i=(o(66702),o(38103)),c=o(18601),a=o(14114);const n=Symbol("selection controller");class s{constructor(){this.selected=null,this.ordered=null,this.set=new Set}}class l{constructor(e){this.sets={},this.focusedSet=null,this.mouseIsDown=!1,this.updating=!1,e.addEventListener("keydown",(e=>{this.keyDownHandler(e)})),e.addEventListener("mousedown",(()=>{this.mousedownHandler()})),e.addEventListener("mouseup",(()=>{this.mouseupHandler()}))}static getController(e){const r=!("global"in e)||"global"in e&&e.global?document:e.getRootNode();let o=r[n];return void 0===o&&(o=new l(r),r[n]=o),o}keyDownHandler(e){const r=e.target;"checked"in r&&this.has(r)&&("ArrowRight"==e.key||"ArrowDown"==e.key?this.selectNext(r):"ArrowLeft"!=e.key&&"ArrowUp"!=e.key||this.selectPrevious(r))}mousedownHandler(){this.mouseIsDown=!0}mouseupHandler(){this.mouseIsDown=!1}has(e){return this.getSet(e.name).set.has(e)}selectPrevious(e){const r=this.getOrdered(e),o=r.indexOf(e),d=r[o-1]||r[r.length-1];return this.select(d),d}selectNext(e){const r=this.getOrdered(e),o=r.indexOf(e),d=r[o+1]||r[0];return this.select(d),d}select(e){e.click()}focus(e){if(this.mouseIsDown)return;const r=this.getSet(e.name),o=this.focusedSet;this.focusedSet=r,o!=r&&r.selected&&r.selected!=e&&r.selected.focus()}isAnySelected(e){const r=this.getSet(e.name);for(const e of r.set)if(e.checked)return!0;return!1}getOrdered(e){const r=this.getSet(e.name);return r.ordered||(r.ordered=Array.from(r.set),r.ordered.sort(((e,r)=>e.compareDocumentPosition(r)==Node.DOCUMENT_POSITION_PRECEDING?1:0))),r.ordered}getSet(e){return this.sets[e]||(this.sets[e]=new s),this.sets[e]}register(e){const r=e.name||e.getAttribute("name")||"",o=this.getSet(r);o.set.add(e),o.ordered=null}unregister(e){const r=this.getSet(e.name);r.set.delete(e),r.ordered=null,r.selected==e&&(r.selected=null)}update(e){if(this.updating)return;this.updating=!0;const r=this.getSet(e.name);if(e.checked){for(const o of r.set)o!=e&&(o.checked=!1);r.selected=e}if(this.isAnySelected(e))for(const e of r.set){if(void 0===e.formElementTabIndex)break;e.formElementTabIndex=e.checked?0:-1}this.updating=!1}}var m=o(98734),u=o(72774),_={NATIVE_CONTROL_SELECTOR:".mdc-radio__native-control"},h={DISABLED:"mdc-radio--disabled",ROOT:"mdc-radio"};const b=function(e){function r(o){return e.call(this,(0,d.__assign)((0,d.__assign)({},r.defaultAdapter),o))||this}return(0,d.__extends)(r,e),Object.defineProperty(r,"cssClasses",{get:function(){return h},enumerable:!1,configurable:!0}),Object.defineProperty(r,"strings",{get:function(){return _},enumerable:!1,configurable:!0}),Object.defineProperty(r,"defaultAdapter",{get:function(){return{addClass:function(){},removeClass:function(){},setNativeControlDisabled:function(){}}},enumerable:!1,configurable:!0}),r.prototype.setDisabled=function(e){var o=r.cssClasses.DISABLED;this.adapter.setNativeControlDisabled(e),e?this.adapter.addClass(o):this.adapter.removeClass(o)},r}(u.K);var p=o(59685),g=o(88668);class v extends c.Wg{constructor(){super(...arguments),this._checked=!1,this.useStateLayerCustomProperties=!1,this.global=!1,this.disabled=!1,this.value="on",this.name="",this.reducedTouchTarget=!1,this.mdcFoundationClass=b,this.formElementTabIndex=0,this.focused=!1,this.shouldRenderRipple=!1,this.rippleElement=null,this.rippleHandlers=new m.A((()=>(this.shouldRenderRipple=!0,this.ripple.then((e=>{this.rippleElement=e})),this.ripple)))}get checked(){return this._checked}set checked(e){var r,o;const d=this._checked;e!==d&&(this._checked=e,this.formElement&&(this.formElement.checked=e),null===(r=this._selectionController)||void 0===r||r.update(this),!1===e&&(null===(o=this.formElement)||void 0===o||o.blur()),this.requestUpdate("checked",d),this.dispatchEvent(new Event("checked",{bubbles:!0,composed:!0})))}_handleUpdatedValue(e){this.formElement.value=e}renderRipple(){return this.shouldRenderRipple?t.dy`<mwc-ripple unbounded accent
        .internalUseStateLayerCustomProperties="${this.useStateLayerCustomProperties}"
        .disabled="${this.disabled}"></mwc-ripple>`:""}get isRippleActive(){var e;return(null===(e=this.rippleElement)||void 0===e?void 0:e.isActive)||!1}connectedCallback(){super.connectedCallback(),this._selectionController=l.getController(this),this._selectionController.register(this),this._selectionController.update(this)}disconnectedCallback(){this._selectionController.unregister(this),this._selectionController=void 0}focus(){this.formElement.focus()}createAdapter(){return Object.assign(Object.assign({},(0,c.qN)(this.mdcRoot)),{setNativeControlDisabled:e=>{this.formElement.disabled=e}})}handleFocus(){this.focused=!0,this.handleRippleFocus()}handleClick(){this.formElement.focus()}handleBlur(){this.focused=!1,this.formElement.blur(),this.rippleHandlers.endFocus()}setFormData(e){this.name&&this.checked&&e.append(this.name,this.value)}render(){const e={"mdc-radio--touch":!this.reducedTouchTarget,"mdc-ripple-upgraded--background-focused":this.focused,"mdc-radio--disabled":this.disabled};return t.dy`
      <div class="mdc-radio ${(0,p.$)(e)}">
        <input
          tabindex="${this.formElementTabIndex}"
          class="mdc-radio__native-control"
          type="radio"
          name="${this.name}"
          aria-label="${(0,g.o)(this.ariaLabel)}"
          aria-labelledby="${(0,g.o)(this.ariaLabelledBy)}"
          .checked="${this.checked}"
          .value="${this.value}"
          ?disabled="${this.disabled}"
          @change="${this.changeHandler}"
          @focus="${this.handleFocus}"
          @click="${this.handleClick}"
          @blur="${this.handleBlur}"
          @mousedown="${this.handleRippleMouseDown}"
          @mouseenter="${this.handleRippleMouseEnter}"
          @mouseleave="${this.handleRippleMouseLeave}"
          @touchstart="${this.handleRippleTouchStart}"
          @touchend="${this.handleRippleDeactivate}"
          @touchcancel="${this.handleRippleDeactivate}">
        <div class="mdc-radio__background">
          <div class="mdc-radio__outer-circle"></div>
          <div class="mdc-radio__inner-circle"></div>
        </div>
        ${this.renderRipple()}
      </div>`}handleRippleMouseDown(e){const r=()=>{window.removeEventListener("mouseup",r),this.handleRippleDeactivate()};window.addEventListener("mouseup",r),this.rippleHandlers.startPress(e)}handleRippleTouchStart(e){this.rippleHandlers.startPress(e)}handleRippleDeactivate(){this.rippleHandlers.endPress()}handleRippleMouseEnter(){this.rippleHandlers.startHover()}handleRippleMouseLeave(){this.rippleHandlers.endHover()}handleRippleFocus(){this.rippleHandlers.startFocus()}changeHandler(){this.checked=this.formElement.checked}}(0,d.__decorate)([(0,t.IO)(".mdc-radio")],v.prototype,"mdcRoot",void 0),(0,d.__decorate)([(0,t.IO)("input")],v.prototype,"formElement",void 0),(0,d.__decorate)([(0,t.SB)()],v.prototype,"useStateLayerCustomProperties",void 0),(0,d.__decorate)([(0,t.Cb)({type:Boolean})],v.prototype,"global",void 0),(0,d.__decorate)([(0,t.Cb)({type:Boolean,reflect:!0})],v.prototype,"checked",null),(0,d.__decorate)([(0,t.Cb)({type:Boolean}),(0,a.P)((function(e){this.mdcFoundation.setDisabled(e)}))],v.prototype,"disabled",void 0),(0,d.__decorate)([(0,t.Cb)({type:String}),(0,a.P)((function(e){this._handleUpdatedValue(e)}))],v.prototype,"value",void 0),(0,d.__decorate)([(0,t.Cb)({type:String})],v.prototype,"name",void 0),(0,d.__decorate)([(0,t.Cb)({type:Boolean})],v.prototype,"reducedTouchTarget",void 0),(0,d.__decorate)([(0,t.Cb)({type:Number})],v.prototype,"formElementTabIndex",void 0),(0,d.__decorate)([(0,t.SB)()],v.prototype,"focused",void 0),(0,d.__decorate)([(0,t.SB)()],v.prototype,"shouldRenderRipple",void 0),(0,d.__decorate)([(0,t.GC)("mwc-ripple")],v.prototype,"ripple",void 0),(0,d.__decorate)([i.L,(0,t.Cb)({attribute:"aria-label"})],v.prototype,"ariaLabel",void 0),(0,d.__decorate)([i.L,(0,t.Cb)({attribute:"aria-labelledby"})],v.prototype,"ariaLabelledBy",void 0),(0,d.__decorate)([(0,t.hO)({passive:!0})],v.prototype,"handleRippleTouchStart",null);const k=t.iv`.mdc-touch-target-wrapper{display:inline}.mdc-radio{padding:calc((40px - 20px) / 2)}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.54)}.mdc-radio .mdc-radio__native-control:enabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__native-control:enabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:rgba(0, 0, 0, 0.38)}.mdc-radio .mdc-radio__background::before{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786)}.mdc-radio .mdc-radio__background::before{top:calc(-1 * (40px - 20px) / 2);left:calc(-1 * (40px - 20px) / 2);width:40px;height:40px}.mdc-radio .mdc-radio__native-control{top:calc((40px - 40px) / 2);right:calc((40px - 40px) / 2);left:calc((40px - 40px) / 2);width:40px;height:40px}@media screen and (forced-colors: active),(-ms-high-contrast: active){.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:GrayText}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:GrayText}}.mdc-radio{display:inline-block;position:relative;flex:0 0 auto;box-sizing:content-box;width:20px;height:20px;cursor:pointer;will-change:opacity,transform,border-color,color}.mdc-radio__background{display:inline-block;position:relative;box-sizing:border-box;width:20px;height:20px}.mdc-radio__background::before{position:absolute;transform:scale(0, 0);border-radius:50%;opacity:0;pointer-events:none;content:"";transition:opacity 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__outer-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;border-width:2px;border-style:solid;border-radius:50%;transition:border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__inner-circle{position:absolute;top:0;left:0;box-sizing:border-box;width:100%;height:100%;transform:scale(0, 0);border-width:10px;border-style:solid;border-radius:50%;transition:transform 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1),border-color 120ms 0ms cubic-bezier(0.4, 0, 0.6, 1)}.mdc-radio__native-control{position:absolute;margin:0;padding:0;opacity:0;cursor:inherit;z-index:1}.mdc-radio--touch{margin-top:4px;margin-bottom:4px;margin-right:4px;margin-left:4px}.mdc-radio--touch .mdc-radio__native-control{top:calc((40px - 48px) / 2);right:calc((40px - 48px) / 2);left:calc((40px - 48px) / 2);width:48px;height:48px}.mdc-radio__native-control:checked+.mdc-radio__background,.mdc-radio__native-control:disabled+.mdc-radio__background{transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__outer-circle{transition:border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio--disabled{cursor:default;pointer-events:none}.mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__inner-circle{transform:scale(0.5);transition:transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1),border-color 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}.mdc-radio__native-control:disabled+.mdc-radio__background,[aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background{cursor:default}.mdc-radio__native-control:focus+.mdc-radio__background::before{transform:scale(1);opacity:.12;transition:opacity 120ms 0ms cubic-bezier(0, 0, 0.2, 1),transform 120ms 0ms cubic-bezier(0, 0, 0.2, 1)}:host{display:inline-block;outline:none}.mdc-radio{vertical-align:bottom}.mdc-radio .mdc-radio__native-control:enabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-unchecked-color, rgba(0, 0, 0, 0.54))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:not(:checked)+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control:checked+.mdc-radio__background .mdc-radio__outer-circle,.mdc-radio .mdc-radio__native-control:disabled:checked+.mdc-radio__background .mdc-radio__outer-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}.mdc-radio [aria-disabled=true] .mdc-radio__native-control+.mdc-radio__background .mdc-radio__inner-circle,.mdc-radio .mdc-radio__native-control:disabled+.mdc-radio__background .mdc-radio__inner-circle{border-color:var(--mdc-radio-disabled-color, rgba(0, 0, 0, 0.38))}`;let f=class extends v{};f.styles=[k],f=(0,d.__decorate)([(0,t.Mo)("mwc-radio")],f)}}]);
//# sourceMappingURL=f225cffd.js.map