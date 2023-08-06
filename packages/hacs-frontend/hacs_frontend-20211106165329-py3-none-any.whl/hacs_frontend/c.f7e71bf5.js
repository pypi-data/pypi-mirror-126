import{_ as e,g as t,e as i,i as o,p as n,I as a,J as l,K as r,r as c,n as s,m as d,L as u}from"./main-5345dc77.js";import"./c.fc64be97.js";import"./c.c196cc69.js";import"./c.170e6517.js";e([s("search-input")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[i()],key:"filter",value:void 0},{kind:"field",decorators:[i({type:Boolean,attribute:"no-label-float"})],key:"noLabelFloat",value:()=>!1},{kind:"field",decorators:[i({type:Boolean,attribute:"no-underline"})],key:"noUnderline",value:()=>!1},{kind:"field",decorators:[i({type:Boolean})],key:"autofocus",value:()=>!1},{kind:"field",decorators:[i({type:String})],key:"label",value:void 0},{kind:"method",key:"focus",value:function(){this.shadowRoot.querySelector("paper-input").focus()}},{kind:"field",decorators:[o("paper-input",!0)],key:"_input",value:void 0},{kind:"method",key:"render",value:function(){return n`
      <paper-input
        .autofocus=${this.autofocus}
        .label=${this.label||"Search"}
        .value=${this.filter}
        @value-changed=${this._filterInputChanged}
        .noLabelFloat=${this.noLabelFloat}
      >
        <slot name="prefix" slot="prefix">
          <ha-svg-icon class="prefix" .path=${a}></ha-svg-icon>
        </slot>
        ${this.filter&&n`
          <ha-icon-button
            slot="suffix"
            @click=${this._clearSearch}
            .label=${this.hass.localize("ui.common.clear")}
            .path=${l}
          ></ha-icon-button>
        `}
      </paper-input>
    `}},{kind:"method",key:"updated",value:function(e){e.has("noUnderline")&&(this.noUnderline||void 0!==e.get("noUnderline"))&&(this._input.inputElement.parentElement.shadowRoot.querySelector("div.unfocused-line").style.display=this.noUnderline?"none":"block")}},{kind:"method",key:"_filterChanged",value:async function(e){r(this,"value-changed",{value:String(e)})}},{kind:"method",key:"_filterInputChanged",value:async function(e){this._filterChanged(e.target.value)}},{kind:"method",key:"_clearSearch",value:async function(){this._filterChanged("")}},{kind:"get",static:!0,key:"styles",value:function(){return c`
      ha-svg-icon,
      ha-icon-button {
        color: var(--primary-text-color);
      }
      ha-icon-button {
        --mdc-icon-button-size: 24px;
      }
      ha-svg-icon.prefix {
        margin: 8px;
      }
    `}}]}}),t);const h=d((e,t)=>e.filter(e=>f(e.name).includes(f(t))||f(e.description).includes(f(t))||f(e.category).includes(f(t))||f(e.full_name).includes(f(t))||f(e.authors).includes(f(t))||f(e.domain).includes(f(t)))),f=d(e=>String(e||"").toLocaleLowerCase().replace(/-|_| /g,""));e([s("hacs-filter")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[i({attribute:!1})],key:"filters",value:void 0},{kind:"field",decorators:[i({attribute:!1})],key:"hacs",value:void 0},{kind:"method",key:"render",value:function(){var e;return n`
      <div class="filter">
        ${null===(e=this.filters)||void 0===e?void 0:e.map(e=>n`
            <ha-formfield
              class="checkbox"
              .label=${this.hacs.localize("common."+e.id)||e.value}
            >
              <ha-checkbox
                .checked=${e.checked||!1}
                .id=${e.id}
                @click=${this._filterClick}
              >
              </ha-checkbox>
            </ha-formfield>
          `)}
      </div>
    `}},{kind:"method",key:"_filterClick",value:function(e){const t=e.currentTarget;this.dispatchEvent(new CustomEvent("filter-change",{detail:{id:t.id},bubbles:!0,composed:!0}))}},{kind:"get",static:!0,key:"styles",value:function(){return[u,c`
        .filter {
          display: flex;
          border-bottom: 1px solid var(--divider-color);
          align-items: center;
          font-size: 16px;
          height: 32px;
          line-height: 4px;
          background-color: var(--sidebar-background-color);
          padding: 0 16px;
          box-sizing: border-box;
        }

        .checkbox:not(:first-child) {
          margin-left: 20px;
        }
      `]}}]}}),t);export{h as f};
