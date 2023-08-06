import{_ as i,H as a,e,p as o,Z as t,c as s,L as d,r as c,n}from"./main-5345dc77.js";import{c as l}from"./c.0be06691.js";i([n("hacs-dialog")],(function(i,a){return{F:class extends a{constructor(...a){super(...a),i(this)}},d:[{kind:"field",decorators:[e({type:Boolean})],key:"hideActions",value:()=>!1},{kind:"field",decorators:[e({type:Boolean})],key:"scrimClickAction",value:()=>!1},{kind:"field",decorators:[e({type:Boolean})],key:"escapeKeyAction",value:()=>!1},{kind:"field",decorators:[e({type:Boolean})],key:"noClose",value:()=>!1},{kind:"field",decorators:[e()],key:"title",value:void 0},{kind:"method",key:"render",value:function(){return this.active?o` <ha-dialog
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
    </ha-dialog>`:o``}},{kind:"method",key:"closeDialog",value:function(){this.active=!1,this.dispatchEvent(new CustomEvent("closed",{bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[t,s,d,c`
        ha-dialog {
          --mdc-dialog-max-width: var(--hacs-dialog-max-width, calc(100vw - 16px));
          --mdc-dialog-min-width: var(--hacs-dialog-min-width, 280px);
        }
        .primary {
          margin-left: 52px;
        }

        @media only screen and (min-width: 1280px) {
          ha-dialog {
            --mdc-dialog-max-width: var(--hacs-dialog-max-width, 990px);
          }
        }

        @media only screen and (max-width: 990px) {
          ha-dialog {
            --mdc-dialog-max-width: var(--hacs-dialog-max-width, 100vw);
            --mdc-dialog-min-width: var(--hacs-dialog-min-width, 100vw);
          }
        }
      `]}}]}}),a);
