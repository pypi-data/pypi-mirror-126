import{_ as e,H as t,e as i,p as o,Z as s,c as a,L as c,n}from"./main-6390c62f.js";import{c as l}from"./c.144b2b40.js";e([n("hacs-dialog")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[i({type:Boolean})],key:"hideActions",value:()=>!1},{kind:"field",decorators:[i({type:Boolean})],key:"scrimClickAction",value:()=>!1},{kind:"field",decorators:[i({type:Boolean})],key:"escapeKeyAction",value:()=>!1},{kind:"field",decorators:[i({type:Boolean})],key:"noClose",value:()=>!1},{kind:"field",decorators:[i()],key:"title",value:void 0},{kind:"method",key:"render",value:function(){return this.active?o`<ha-dialog
      ?open=${this.active}
      ?scrimClickAction=${this.scrimClickAction}
      ?escapeKeyAction=${this.escapeKeyAction}
      @closed=${this.closeDialog}
      ?hideActions=${this.hideActions}
      .heading=${this.noClose?this.title:l(this.hass,this.title)}
    >
      <div class="content scroll" ?narrow=${this.narrow}>
        <slot></slot>
      </div>
      <slot class="primary" name="primaryaction" slot="primaryAction"></slot>
      <slot class="secondary" name="secondaryaction" slot="secondaryAction"></slot>
    </ha-dialog>`:o``}},{kind:"method",key:"closeDialog",value:function(){this.active=!1,this.dispatchEvent(new CustomEvent("closed",{bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[s,a,c]}}]}}),t);
