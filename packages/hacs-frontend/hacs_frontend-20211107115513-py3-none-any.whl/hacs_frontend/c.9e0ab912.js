import{_ as o,H as s,e as t,t as i,p as a,b as e,a3 as r,a4 as c,a5 as n,a6 as d,c as h,d as l,r as p,n as m}from"./main-42851b08.js";import{a as u}from"./c.0a038163.js";import"./c.7db9a0c7.js";import"./c.bee36bb6.js";import"./c.21bf2a97.js";import"./c.c72401a7.js";import"./c.31401eee.js";import"./c.9f27b448.js";import"./c.f195f0b2.js";import"./c.70e07439.js";import"./c.4cf801d0.js";import"./c.0c8dac2c.js";import"./c.2f9eddfe.js";import"./c.28cc9784.js";import"./c.a34115ef.js";import"./c.3944d22b.js";import"./c.1dfe664d.js";let y=o([m("hacs-custom-repositories-dialog")],(function(o,s){return{F:class extends s{constructor(...s){super(...s),o(this)}},d:[{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[i()],key:"_progress",value:()=>!1},{kind:"field",decorators:[i()],key:"_addRepositoryData",value:()=>({category:void 0,repository:void 0})},{kind:"method",key:"shouldUpdate",value:function(o){return o.has("narrow")||o.has("active")||o.has("_error")||o.has("_addRepositoryData")||o.has("_progress")||o.has("repositories")}},{kind:"method",key:"render",value:function(){var o,s;if(!this.active)return a``;const t=null===(o=this.repositories)||void 0===o?void 0:o.filter(o=>o.custom),i=[{type:"string",name:"repository"},{type:"select",name:"category",optional:!0,options:this.hacs.configuration.categories.map(o=>[o,this.hacs.localize("common."+o)])}];return a`
      <hacs-dialog
        .active=${this.active}
        .hass=${this.hass}
        .title=${this.hacs.localize("dialog_custom_repositories.title")}
        scrimClickAction
        escapeKeyAction
      >
        <div class="content">
          <div class="list">
            ${null!==(s=this._error)&&void 0!==s&&s.message?a`<ha-alert alert-type="error" .rtl=${u(this.hass)}>
                  ${this._error.message}
                </ha-alert>`:""}
            ${null==t?void 0:t.filter(o=>this.hacs.configuration.categories.includes(o.category)).map(o=>a`<ha-settings-row
                  @click=${()=>this._showReopsitoryInfo(String(o.id))}
                >
                  ${this.narrow?"":a`<ha-svg-icon slot="prefix" .path=${e}></ha-svg-icon>`}
                  <span slot="heading">${o.name}</span>
                  <span slot="description">${o.full_name} (${o.category})</span>

                  <mwc-icon-button
                    @click=${s=>{s.stopPropagation(),this._removeRepository(o.id)}}
                  >
                    <ha-svg-icon class="delete" .path=${r}></ha-svg-icon>
                  </mwc-icon-button>
                </ha-settings-row>`)}
          </div>
          <ha-form
            ?narrow=${this.narrow}
            .data=${this._addRepositoryData}
            .schema=${i}
            .computeLabel=${o=>"category"===o.name?this.hacs.localize("dialog_custom_repositories.category"):this.hacs.localize("common.repository")}
            @value-changed=${this._valueChanged}
          >
          </ha-form>
        </div>
        <mwc-button
          slot="primaryaction"
          raised
          .disabled=${void 0===this._addRepositoryData.category||void 0===this._addRepositoryData.repository}
          @click=${this._addRepository}
        >
          ${this._progress?a`<ha-circular-progress active size="small"></ha-circular-progress>`:this.hacs.localize("common.add")}
        </mwc-button>
      </hacs-dialog>
    `}},{kind:"method",key:"firstUpdated",value:function(){this.hass.connection.subscribeEvents(o=>this._error=o.data,"hacs/error")}},{kind:"method",key:"_valueChanged",value:function(o){this._addRepositoryData=o.detail.value}},{kind:"method",key:"_addRepository",value:async function(){this._error=void 0,this._progress=!0,this._addRepositoryData.category?this._addRepositoryData.repository?(await c(this.hass,this._addRepositoryData.repository,this._addRepositoryData.category),this.repositories=await n(this.hass),this._progress=!1):this._error={message:this.hacs.localize("dialog_custom_repositories.no_repository")}:this._error={message:this.hacs.localize("dialog_custom_repositories.no_category")}}},{kind:"method",key:"_removeRepository",value:async function(o){this._error=void 0,await d(this.hass,o),this.repositories=await n(this.hass)}},{kind:"method",key:"_showReopsitoryInfo",value:async function(o){this.dispatchEvent(new CustomEvent("hacs-dialog-secondary",{detail:{type:"repository-info",repository:o},bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[h,l,p`
        .list {
          position: relative;
          max-height: 870px;
          overflow: auto;
        }
        ha-form {
          display: block;
          padding: 25px 0;
        }
        ha-form[narrow] {
          bottom: 0;
          position: absolute;
          width: calc(100% - 48px);
        }
        ha-svg-icon {
          --mdc-icon-size: 36px;
        }
        ha-svg-icon:not(.delete) {
          margin-right: 4px;
        }
        ha-settings-row {
          cursor: pointer;
          padding: 0;
        }
        .delete {
          color: var(--hcv-color-error);
        }
      `]}}]}}),s);export{y as HacsCustomRepositoriesDialog};
