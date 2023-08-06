import{_ as s,H as e,e as t,t as i,m as o,ak as a,ac as r,p as l,al as c,am as n,an as h,ao as d,aj as p,r as _,n as m}from"./main-6390c62f.js";import"./c.eba65a66.js";import"./c.cb429b34.js";import"./c.2aebbf52.js";import{a as y}from"./c.0a038163.js";import"./c.bf52eb52.js";import"./c.a90a1ee7.js";import"./c.83858ffa.js";import"./c.74e704c6.js";import{s as v}from"./c.f9f832f0.js";import{u as g}from"./c.eb7215b2.js";import"./c.c5caace7.js";import"./c.17912c8e.js";import"./c.f9fa7a78.js";import"./c.90aae75a.js";import"./c.aa022b79.js";import"./c.9f27b448.js";import"./c.d38ca8fe.js";import"./c.cd722ab9.js";import"./c.144b2b40.js";let u=s([m("hacs-install-dialog")],(function(s,e){return{F:class extends e{constructor(...e){super(...e),s(this)}},d:[{kind:"field",decorators:[t()],key:"repository",value:void 0},{kind:"field",decorators:[t()],key:"_repository",value:void 0},{kind:"field",decorators:[t()],key:"_toggle",value:()=>!0},{kind:"field",decorators:[t()],key:"_installing",value:()=>!1},{kind:"field",decorators:[t()],key:"_error",value:void 0},{kind:"field",decorators:[i()],key:"_version",value:void 0},{kind:"method",key:"shouldUpdate",value:function(s){return s.forEach((s,e)=>{"hass"===e&&(this.sidebarDocked='"docked"'===window.localStorage.getItem("dockedSidebar")),"repositories"===e&&(this._repository=this._getRepository(this.repositories,this.repository))}),s.has("sidebarDocked")||s.has("narrow")||s.has("active")||s.has("_toggle")||s.has("_error")||s.has("_version")||s.has("_repository")||s.has("_installing")}},{kind:"field",key:"_getRepository",value:()=>o((s,e)=>null==s?void 0:s.find(s=>s.id===e))},{kind:"field",key:"_getInstallPath",value:()=>o(s=>{let e=s.local_path;return"theme"===s.category&&(e=`${e}/${s.file_name}`),e})},{kind:"method",key:"firstUpdated",value:async function(){this._repository=this._getRepository(this.repositories,this.repository),this._repository.updated_info||(await a(this.hass,this._repository.id),this.repositories=await r(this.hass)),this._toggle=!1,this.hass.connection.subscribeEvents(s=>this._error=s.data,"hacs/error")}},{kind:"method",key:"render",value:function(){var s;if(!this.active||!this._repository)return l``;const e=this._getInstallPath(this._repository);return l`
      <hacs-dialog
        .active=${this.active}
        .narrow=${this.narrow}
        .hass=${this.hass}
        .secondary=${this.secondary}
        .title=${this._repository.name}
        dynamicHeight
      >
        <div class="content">
          ${"version"===this._repository.version_or_commit?l`<div class="beta-container">
                  <ha-formfield .label=${this.hacs.localize("dialog_install.show_beta")}>
                    <ha-switch
                      ?disabled=${this._toggle}
                      .checked=${this._repository.beta}
                      @change=${this._toggleBeta}
                    ></ha-switch>
                  </ha-formfield>
                </div>
                <div class="version-select-container">
                  <ha-paper-dropdown-menu
                    ?disabled=${this._toggle}
                    class="version-select-dropdown"
                    label="${this.hacs.localize("dialog_install.select_version")}"
                  >
                    <paper-listbox
                      id="version"
                      class="version-select-list"
                      slot="dropdown-content"
                      selected="0"
                      @iron-select=${this._versionSelectChanged}
                    >
                      ${this._repository.releases.map(s=>l`<paper-item .version=${s} class="version-select-item"
                            >${s}</paper-item
                          >`)}
                      ${"hacs/integration"===this._repository.full_name||this._repository.hide_default_branch?"":l`
                            <paper-item
                              .version=${this._repository.default_branch}
                              class="version-select-item"
                              >${this._repository.default_branch}</paper-item
                            >
                          `}
                    </paper-listbox>
                  </ha-paper-dropdown-menu>
                </div>`:""}
          ${this._repository.can_install?"":l`<ha-alert alert-type="error" .rtl=${y(this.hass)}>
                ${this.hacs.localize("confirm.home_assistant_version_not_correct",{haversion:this.hass.config.version,minversion:this._repository.homeassistant})}
              </ha-alert>`}
          <div class="note">
            ${this.hacs.localize("repository.note_installed")}
            <code>'${e}'</code>
            ${"plugin"===this._repository.category&&"storage"!==this.hacs.status.lovelace_mode?l`
                  <p>${this.hacs.localize("repository.lovelace_instruction")}</p>
                  <pre>
                url: ${c({repository:this._repository,skipTag:!0})}
                type: module
                </pre
                  >
                `:""}
            ${"integration"===this._repository.category?l`<p>${this.hacs.localize("dialog_install.restart")}</p>`:""}
          </div>
          ${null!==(s=this._error)&&void 0!==s&&s.message?l`<ha-alert alert-type="error" .rtl=${y(this.hass)}>
                ${this._error.message}
              </ha-alert>`:""}
        </div>
        <mwc-button
          slot="primaryaction"
          ?disabled=${!this._repository.can_install||this._toggle}
          @click=${this._installRepository}
        >
          ${this._installing?l`<ha-circular-progress active size="small"></ha-circular-progress>`:this.hacs.localize("common.download")}
        </mwc-button>
        <hacs-link slot="secondaryaction" .url="https://github.com/${this._repository.full_name}">
          <mwc-button> ${this.hacs.localize("common.repository")} </mwc-button>
        </hacs-link>
      </hacs-dialog>
    `}},{kind:"method",key:"_versionSelectChanged",value:function(s){s.currentTarget.selectedItem.version!==this._version&&(this._version=s.currentTarget.selectedItem.version)}},{kind:"method",key:"_toggleBeta",value:async function(){this._toggle=!0,await n(this.hass,this.repository),this.repositories=await r(this.hass),this._toggle=!1}},{kind:"method",key:"_installRepository",value:async function(){var s;if(this._installing=!0,this._repository){if("commit"!==(null===(s=this._repository)||void 0===s?void 0:s.version_or_commit)){const s=this._version||this._repository.available_version||this._repository.default_branch;await h(this.hass,this._repository.id,s)}else await d(this.hass,this._repository.id);this.hacs.log.debug(this._repository.category,"_installRepository"),this.hacs.log.debug(this.hacs.status.lovelace_mode,"_installRepository"),"plugin"===this._repository.category&&"storage"===this.hacs.status.lovelace_mode&&await g(this.hass,this._repository,this._version),this._installing=!1,this.dispatchEvent(new Event("hacs-secondary-dialog-closed",{bubbles:!0,composed:!0})),this.dispatchEvent(new Event("hacs-dialog-closed",{bubbles:!0,composed:!0})),"plugin"===this._repository.category&&"storage"===this.hacs.status.lovelace_mode&&v(this,{title:this.hacs.localize("common.reload"),text:l`${this.hacs.localize("dialog.reload.description")}</br>${this.hacs.localize("dialog.reload.confirm")}`,dismissText:this.hacs.localize("common.cancel"),confirmText:this.hacs.localize("common.reload"),confirm:()=>{p.location.href=p.location.href}})}}},{kind:"get",static:!0,key:"styles",value:function(){return[_`
        .version-select-dropdown {
          width: 100%;
        }
        .content {
          padding: 32px 8px;
        }
        .note {
          margin-bottom: -32px;
          margin-top: 12px;
        }
        .lovelace {
          margin-top: 8px;
        }
        paper-menu-button {
          color: var(--secondary-text-color);
          padding: 0;
        }
        paper-item {
          cursor: pointer;
        }
        paper-item-body {
          opacity: var(--dark-primary-opacity);
        }
        pre {
          white-space: pre-line;
          user-select: all;
        }
      `]}}]}}),e);export{u as HacsInstallDialog};
