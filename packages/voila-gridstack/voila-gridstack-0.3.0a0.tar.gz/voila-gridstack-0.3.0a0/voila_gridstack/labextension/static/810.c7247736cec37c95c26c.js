"use strict";(self.webpackChunk_voila_dashboards_jupyterlab_gridstack=self.webpackChunk_voila_dashboards_jupyterlab_gridstack||[]).push([[810],{810:(e,t,o)=>{o.r(t),o.d(t,{default:()=>te});var i=o(938),s=o(575),n=o(754),d=o(766),l=o(835),r=o(464),a=o(677),h=o(797),c=o(271),g=o(936);const m=new g.LabIcon({name:"@voila-dashboards/jupyterlab-gridstack:icon-compact",svgstr:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">\n    <g class="jp-icon3" stroke="#616161" stroke-width="1">\n        <rect stroke-dasharray="2" width="22" height="22" x="1" y="1" />\n        <rect class="jp-icon3" fill="#616161" width="8" height="8" x="1" y="1" />\n        <path d="M 22 22 L 10 10" />\n        <path class="jp-icon3" fill="#616161" d="M 10 10 L 11 14 L 14 11 L 10 10" stroke-linecap="round"\n            stroke-linejoin="round" />\n    </g>\n</svg>'}),u=new g.LabIcon({name:"@voila-dashboards/jupyterlab-gridstack:icon-dashboard",svgstr:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">\n    <g class="jp-icon3" fill="#616161">\n        <rect width="6" height="9" x="2" y="1" />\n        <rect width="12" height="9" x="10" y="1" />\n        <rect width="7" height="9" x="15" y="12" />\n        <rect width="11" height="9" x="2" y="12" />\n    </g>\n</svg>'});class p extends l.ReactWidget{constructor(e){super(),this._panel=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:m,onClick:()=>{this._panel.compact()},tooltip:"Compact the grid towards the top left corner"})}}class _ extends l.ReactWidget{constructor(e){super(),this._panel=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:g.saveIcon,onClick:()=>{this._panel.save()},tooltip:"Save the layout"})}}class v extends l.ReactWidget{constructor(e){super(),this._panel=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:g.editIcon,onClick:()=>{this._panel.info()},tooltip:"Edit grid parameters"})}}var f=o(249);class C extends l.ReactWidget{constructor(e){super(),this._path=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:g.launcherIcon,onClick:()=>{const e=f.PageConfig.getBaseUrl(),t=window.open(`${e}voila/render/${this._path+"?voila-template=gridstack"}`,"_blank");null==t||t.focus()},tooltip:"Open with Voilà Gridstack in a New Browser Tab"})}}class y extends l.ReactWidget{constructor(e){super(),this._model=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:g.undoIcon,onClick:()=>{this._model.sharedModel.undo()},tooltip:"Undo changes"})}}class w extends l.ReactWidget{constructor(e){super(),this._model=e}render(){return c.createElement(l.ToolbarButtonComponent,{icon:g.redoIcon,onClick:()=>{this._model.sharedModel.redo()},tooltip:"Redo changes"})}}class b extends a.DocumentWidget{constructor(e,t){super({context:e,content:t}),this.title.label=e.localPath,this.title.closable=!0,this.title.iconClass="jp-MaterialIcon jp-VoilaIcon",this.addClass("jp-NotebookPanel"),this.toolbar.addItem("save",new _(this.content)),this.toolbar.addItem("edit",new v(this.content)),this.toolbar.addItem("undo",new y(this.context.model)),this.toolbar.addItem("redo",new w(this.context.model)),this.toolbar.addItem("compact",new p(this.content)),this.toolbar.addItem("voila",new C(this.context.path))}undo(){this.context.model.sharedModel.undo()}redo(){this.context.model.sharedModel.redo()}}const k=new h.Token("@voila-dashboards/jupyterlab-gridstack:IVoilaGridstackTracker");var x=o(706),I=o(168),M=o(519),E=o(850),W=o(211),N=o(667);o(43);class j extends x.Layout{constructor(e){super(),this._gridItems=[],this._gridItemChanged=new I.Signal(this),this._margin=e.cellMargin,this._cellHeight=e.defaultCellHeight,this._columns=e.maxColumns,this._helperMessage=document.createElement("div"),this._helperMessage.appendChild(document.createElement("p")).textContent="Drag and drop cells here to start building the dashboard.",this._helperMessage.className="jp-grid-helper",this._gridHost=document.createElement("div"),this._gridHost.className="grid-stack",this._grid=N.GridStack.init({float:!0,column:this._columns,margin:this._margin,cellHeight:this._cellHeight,styleInHead:!0,disableOneColumnMode:!0,draggable:{handle:".grid-item-toolbar"},resizable:{autoHide:!0,handles:"e, se, s, sw, w"},alwaysShowResizeHandle:/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)},this._gridHost),this._updateBackgroundSize(),this._grid.on("change",((e,t)=>{this._onChange(e,t)})),this._grid.on("removed",((e,t)=>{t.length<=1&&this._onRemoved(e,t)})),this._grid.on("resizestop",((e,t)=>{window.dispatchEvent(new Event("resize"))}))}get gridItemChanged(){return this._gridItemChanged}dispose(){this._grid.destroy(),super.dispose()}init(){super.init(),this.parent.node.appendChild(this._gridHost),window.dispatchEvent(new Event("resize"))}onUpdateRequest(e){var t;const o=null===(t=this._grid)||void 0===t?void 0:t.getGridItems();null==o||o.forEach((e=>{this._grid.removeWidget(e,!0,!1),this._grid.addWidget(e)}))}onResize(e){this._prepareGrid()}onFitRequest(e){this._prepareGrid()}iter(){return new E.ArrayIterator(this._gridItems)}removeWidget(e){}get margin(){return this._margin}set margin(e){this._margin!==e&&(this._margin=e,this._grid.margin(this._margin),this.parent.update())}get cellHeight(){var e;return null!==(e=this._grid.getCellHeight(!0))&&void 0!==e?e:this._cellHeight}set cellHeight(e){this._cellHeight!==e&&(this._cellHeight=e,this._grid.cellHeight(this._cellHeight),this._updateBackgroundSize(),this.parent.update())}get columns(){return this._columns}set columns(e){this._columns!==e&&(this._columns=e,this._grid.column(e),this._updateBackgroundSize(),this.parent.update())}get grid(){return this._grid}get gridWidgets(){return this._gridItems}get gridItems(){var e;return null!==(e=this._grid.getGridItems())&&void 0!==e?e:[]}addGridItem(e,t,o){const i={id:e,x:o.col,y:o.row,width:o.width,height:o.height,locked:o.locked,autoPosition:!1};null!==o.row&&null!==o.col||(i.autoPosition=!0),this._gridItems.push(t),1===this._gridItems.length&&this.parent.node.removeChild(this._helperMessage),W.MessageLoop.sendMessage(t,x.Widget.Msg.BeforeAttach),this._grid.addWidget(t.node,i),W.MessageLoop.sendMessage(t,x.Widget.Msg.AfterAttach),this.updateGridItem(e,o)}updateGridItem(e,t){const o=this._grid.getGridItems(),i=null==o?void 0:o.find((t=>{var o;return(null===(o=t.gridstackNode)||void 0===o?void 0:o.id)===e}));this._grid.update(i,{x:t.col,y:t.row,w:t.width,h:t.height,locked:t.locked})}removeGridItem(e){const t=this._grid.getGridItems(),o=null==t?void 0:t.find((t=>{var o;return(null===(o=t.gridstackNode)||void 0===o?void 0:o.id)===e}));o&&(this._gridItems=this._gridItems.filter((t=>t.cellId!==e)),this._grid.removeWidget(o,!0,!1)),0===this._gridItems.length&&this._gridHost.insertAdjacentElement("beforebegin",this._helperMessage)}_onChange(e,t){this._gridItemChanged.emit(null!=t?t:[])}_onRemoved(e,t){t.forEach((e=>{}))}_updateBackgroundSize(){this._gridHost.style.backgroundSize=`100px ${this.cellHeight}px, calc(100% / ${this.columns} + 0px) 100px, 20px 20px, 20px 20px`}_prepareGrid(){const e=this.parent.node.getBoundingClientRect();if(this._gridHost.style.minHeight=`${e.height}px`,0===this._gridItems.length){const t=this._helperMessage.getBoundingClientRect(),o=0===t.height?18:t.height,i=0===t.width?350:t.width;this._helperMessage.style.top=(e.height-o)/2+"px",this._helperMessage.style.left=(e.width-i)/2+"px",this._gridHost.insertAdjacentElement("beforebegin",this._helperMessage)}this._grid.onParentResize()}}class S extends l.ReactWidget{constructor(e){super(),this._info=e}get info(){return this._info}render(){return c.createElement("form",{className:"jp-Input-Dialog jp-Dialog-body"},c.createElement("div",{className:"row"},c.createElement("label",{className:"col-25"},"Name:"),c.createElement("input",{type:"text",name:"name",className:"jp-mod-styled col-75",value:this._info.name,onChange:e=>{this._info.name=e.target.value,this.update()}})),c.createElement("div",{className:"row"},c.createElement("label",{className:"col-25"},"Type:"),c.createElement("input",{type:"text",name:"name",className:"jp-mod-styled col-75",value:this._info.type,disabled:!0})),c.createElement("div",{className:"row"},c.createElement("label",{className:"col-25"},"Cell Margin:"),c.createElement("input",{type:"number",name:"margin",className:"jp-mod-styled col-75",value:this._info.cellMargin,onChange:e=>{this._info.cellMargin=parseInt(e.target.value,10),this.update()}})),c.createElement("div",{className:"row"},c.createElement("label",{className:"col-25"},"Cell Height:")," ",c.createElement("input",{type:"number",name:"height",className:"jp-mod-styled col-75",value:this._info.defaultCellHeight,onChange:e=>{const t=parseInt(e.target.value,10);this._info.defaultCellHeight=t<40?40:t,this.update()}})),c.createElement("div",{className:"row"},c.createElement("label",{className:"col-25"},"Number of columns:")," ",c.createElement("input",{type:"number",name:"columns",className:"jp-mod-styled col-75",value:this._info.maxColumns,onChange:e=>{let t=parseInt(e.target.value,10);t=t>12?12:t,t=t<1?1:t,this._info.maxColumns=t,this.update()},disabled:!0})))}}class L extends x.Widget{constructor(e){super(),this._shadowWidget=null,this._scrollIntervalId=null,this.removeClass("lm-Widget"),this.removeClass("p-Widget"),this.addClass("grid-editor"),this._model=e,this.layout=new j(this._model.info),this.layout.gridItemChanged.connect(this._onGridItemChange,this),this._model.ready.connect((()=>{this._initGridItems(),this._model.cellRemoved.connect(this._removeCell,this),this._model.cellPinned.connect(this._lockCell,this),this._model.contentChanged.connect(this._updateGridItems,this)}))}compact(){this.layout.grid.compact()}dispose(){this.isDisposed||(this._shadowWidget&&this._resetShadowWidget(),I.Signal.clearData(this),super.dispose())}onAfterAttach(e){super.onAfterAttach(e),this.node.addEventListener("lm-dragenter",this,!0),this.node.addEventListener("lm-dragleave",this,!0),this.node.addEventListener("lm-dragover",this,!0),this.node.addEventListener("lm-drop",this,!0),this.node.addEventListener("lm-dragend",this,!0)}onBeforeDetach(e){super.onBeforeDetach(e),this.node.removeEventListener("lm-dragenter",this,!0),this.node.removeEventListener("lm-dragleave",this,!0),this.node.removeEventListener("lm-dragover",this,!0),this.node.removeEventListener("lm-drop",this,!0),this.node.removeEventListener("lm-dragend",this,!0)}handleEvent(e){if(e.type&&"copy"===e.proposedAction)switch(e.type){case"lm-dragenter":this._evtDragEnter(e);break;case"lm-dragleave":this._evtDragLeave(e);break;case"lm-dragover":this._evtDragOver(e);break;case"lm-drop":this._evtDrop(e)}}get gridWidgets(){return this.layout.gridWidgets}infoEditor(){const e=new S(this._model.info);(0,l.showDialog)({title:"Edit grid parameters",body:e}).then((t=>{t.button.accept&&(this._model.info=e.info,this.layout&&(this.layout.margin=e.info.cellMargin,this.layout.cellHeight=e.info.defaultCellHeight,this.layout.columns=e.info.maxColumns))}))}_initGridItems(){const e=this._model.cells;for(let t=0;t<(null==e?void 0:e.length);t++){const o=e.get(t);this._model.execute(o);const i=this._model.getCellInfo(o.id);if(i&&!i.hidden&&0!==o.value.text.length){const e=this._model.createCell(o,i.locked);this.layout.addGridItem(o.id,e,i)}}this._model.executed=!0}_removeCell(e,t){this.layout.removeGridItem(t.id)}_lockCell(e,t){this.layout.updateGridItem(t.id,t.info)}_updateGridItems(){var e;this.layout.gridItems.forEach((e=>{var t,o;let i=!1;for(let s=0;s<(null===(t=this._model.cells)||void 0===t?void 0:t.length);s++)if((null===(o=e.gridstackNode)||void 0===o?void 0:o.id)===this._model.cells.get(s).id){i=!0;break}!i&&e.gridstackNode&&(this._model.hideCell(e.gridstackNode.id),this.layout.removeGridItem(e.gridstackNode.id))}));for(let t=0;t<(null===(e=this._model.cells)||void 0===e?void 0:e.length);t++){const e=this._model.cells.get(t),o=this._model.getCellInfo(e.id),i=this.layout.gridItems,s=null==i?void 0:i.find((t=>{var o;return(null===(o=t.gridstackNode)||void 0===o?void 0:o.id)===e.id}));if(!s&&o&&!o.hidden&&0!==e.value.text.length){if("code"===e.type&&e.executionCount&&0!==e.outputs.length){const t=e.outputs;let i=!1;for(let e=0;e<t.length;e++)if("error"===t.get(e).type){i=!0;break}if(i)continue;const s=this._model.createCell(e,o.locked);this.layout.addGridItem(e.id,s,o);continue}if("code"!==e.type){const t=this._model.createCell(e,o.locked);this.layout.addGridItem(e.id,t,o);continue}}s&&o&&!o.hidden&&0!==e.value.text.length?this.layout.updateGridItem(e.id,o):(s&&o&&!o.hidden&&0===e.value.text.length||s&&(null==o?void 0:o.hidden))&&(this._model.hideCell(e.id),this.layout.removeGridItem(e.id))}}_onGridItemChange(e,t){null===this._shadowWidget&&t.forEach((e=>{var t,o,i,s,n;this._model.setCellInfo(e.id,{hidden:!1,col:null!==(t=e.x)&&void 0!==t?t:0,row:null!==(o=e.y)&&void 0!==o?o:0,width:null!==(i=e.w)&&void 0!==i?i:2,height:null!==(s=e.h)&&void 0!==s?s:2,locked:null===(n=e.locked)||void 0===n||n})}))}_evtDragEnter(e){const t=this._isDroppable(e);if(t.droppable){e.preventDefault(),e.stopPropagation();const t=e.source.parent.content.activeCell,o=this.layout.gridItems.find((e=>{var o;return(null===(o=e.gridstackNode)||void 0===o?void 0:o.id)===t.model.id})),i=Math.floor((e.offsetY+this.node.scrollTop)/this.layout.cellHeight),s=Math.floor(this.layout.columns*e.offsetX/this.node.offsetWidth);let n=2,d=2;if("code"===t.model.type){const e=t.outputArea.node.getBoundingClientRect(),o=this.layout.columns-s;n=Math.min(o,Math.ceil(e.width/this.layout.grid.cellWidth())),d=Math.ceil((e.height+40)/this.layout.cellHeight)}else{const e=t.node.getBoundingClientRect(),o=this.layout.columns-s;n=Math.min(o,Math.ceil(e.width/this.layout.grid.cellWidth())),d=Math.ceil((e.height+40)/this.layout.cellHeight)}this._resetShadowWidget(),this.layout.grid.el.style.pointerEvents="none",o?(this._shadowWidget=o,this.layout.grid.update(o,{x:s,y:i,w:n,h:d})):this._shadowWidget=this.layout.grid.addWidget('<div class="grid-stack-item grid-stack-placeholder"><div class="grid-stack-item-content placeholder-content"></div></div>',{x:s,y:i,w:n,h:d})}else t.reason&&this._setErrorMessage(t.reason)}_evtDragLeave(e){this.removeClass("pr-DropTarget"),this._isPointerOnWidget(e)||(this._scrollIntervalId&&(clearInterval(this._scrollIntervalId),this._scrollIntervalId=null),this._resetShadowWidget()),e.preventDefault(),e.stopPropagation()}_evtDragOver(e){var t,o;if(this.addClass("pr-DropTarget"),e.dropAction="copy",this._scrollIfNeeded(e),this._shadowWidget){const i=e.source.parent.content.activeCell,s=Math.floor(this.layout.columns*e.offsetX/this.node.offsetWidth),n=Math.floor((e.offsetY+this.node.scrollTop)/this.layout.cellHeight);let d=2;if("code"===i.model.type){const e=i.outputArea.node.getBoundingClientRect(),t=this.layout.columns-s;d=Math.min(t,Math.ceil(e.width/this.layout.grid.cellWidth()))}else{const e=i.node.getBoundingClientRect(),t=this.layout.columns-s;d=Math.min(t,Math.ceil(e.width/this.layout.grid.cellWidth()))}this._shadowWidget.classList.contains("grid-stack-placeholder")||(d=Math.min(d,null!==(o=null===(t=this._shadowWidget.gridstackNode)||void 0===t?void 0:t.w)&&void 0!==o?o:this.layout.columns)),this.layout.grid.update(this._shadowWidget,{x:s,y:n,w:d})}e.preventDefault(),e.stopPropagation()}_evtDrop(e){if(e.preventDefault(),e.stopPropagation(),this._scrollIntervalId&&(clearInterval(this._scrollIntervalId),this._scrollIntervalId=null),this._resetShadowWidget(),"copy"===e.proposedAction){if(e.source.activeCell instanceof M.Cell){const t=e.source.parent.content.activeCell;if(!t)return;const o=Math.floor((e.offsetY+this.node.scrollTop)/this.layout.cellHeight),i=Math.floor(this.layout.columns*e.offsetX/this.node.offsetWidth);let s=1,n=1;if("code"===t.model.type){const e=t.outputArea.node.getBoundingClientRect(),o=this.layout.columns-i;s=Math.min(o,Math.ceil(e.width/this.layout.grid.cellWidth())),n=Math.ceil((e.height+40)/this.layout.cellHeight)}else{const e=t.node.getBoundingClientRect(),o=this.layout.columns-i;s=Math.min(o,Math.ceil(e.width/this.layout.grid.cellWidth())),n=Math.ceil((e.height+40)/this.layout.cellHeight)}const d=this.layout.gridItems,r=null==d?void 0:d.find((e=>{var o;return(null===(o=e.gridstackNode)||void 0===o?void 0:o.id)===(null==t?void 0:t.model.id)})),a=this._model.getCellInfo(t.model.id);if(!r&&(null==a?void 0:a.hidden))if("code"===t.model.type&&t.model.executionCount&&0!==t.model.outputs.length){const e=t.model.outputs;for(let t=0;t<e.length;t++)if("error"===e.get(t).type)return void(0,l.showErrorMessage)("Cell error","It is not possible to add cells with execution errors.");a.hidden=!1,a.col=i,a.row=o,a.width=s,a.height=n,a.locked=!1!==a.locked,this._model.setCellInfo(t.model.id,a);const d=this._model.createCell(t.model,a.locked);this.layout.addGridItem(t.model.id,d,a)}else if("code"!==t.model.type&&0!==t.model.value.text.length){a.hidden=!1,a.col=i,a.row=o,a.width=s,a.height=n,a.locked=!1!==a.locked,this._model.setCellInfo(t.model.id,a);const e=this._model.createCell(t.model,a.locked);this.layout.addGridItem(t.model.id,e,a)}else(0,l.showErrorMessage)("Empty cell","It is not possible to add empty cells.");else r&&a?(a.hidden=!1,a.col=i,a.row=o,a.width=Math.min(s,a.width),a.locked=!1!==a.locked,this._model.setCellInfo(t.model.id,a),this.layout.updateGridItem(t.model.id,a)):a||(0,l.showErrorMessage)("Wrong notebook","It is not possible to add cells from another notebook.")}this.removeClass("pr-DropTarget")}}_isDroppable(e){if("copy"!==e.proposedAction)return{droppable:!1};if(e.source.activeCell instanceof M.Cell){const t=e.source.parent.content.activeCell;if(!t)return{droppable:!1};const o=this.layout.gridItems,i=null==o?void 0:o.find((e=>{var o;return(null===(o=e.gridstackNode)||void 0===o?void 0:o.id)===(null==t?void 0:t.model.id)})),s=this._model.getCellInfo(t.model.id);if(!i&&(null==s?void 0:s.hidden)){if("code"===t.model.type&&t.model.executionCount&&0!==t.model.outputs.length){const e=t.model.outputs;for(let t=0;t<e.length;t++)if("error"===e.get(t).type)return{droppable:!1,reason:"GridStack Error: cells with execution errors."};return{droppable:!0}}return"code"!==t.model.type&&0!==t.model.value.text.length?{droppable:!0}:{droppable:!1,reason:"GridStack Error: empty cells."}}if(i&&s)return{droppable:!0};if(!s)return{droppable:!1,reason:"GridStack Error: cells from another notebook."}}return{droppable:!1}}_scrollIfNeeded(e){this._scrollIntervalId&&(clearInterval(this._scrollIntervalId),this._scrollIntervalId=null);const t=this.node.getBoundingClientRect();return e.clientY<t.top+40?(this._scrollIntervalId=setInterval((()=>{this.node.scrollBy({top:-20})}),10),!0):e.clientY>t.bottom-40&&(this._scrollIntervalId=setInterval((()=>{this.node.scrollBy({top:20})}),10),!0)}_isPointerOnWidget(e){const t=this.node.getBoundingClientRect();return e.clientX>t.left&&e.clientX<t.right-5&&e.clientY>t.top&&e.clientY<t.bottom}_resetShadowWidget(){var e,t;if(this._shadowWidget){if(this._shadowWidget.classList.contains("grid-stack-placeholder"))this.layout.grid.removeWidget(this._shadowWidget,!0,!1);else{const o=this._model.getCellInfo(null===(e=this._shadowWidget.gridstackNode)||void 0===e?void 0:e.id);o&&this.layout.updateGridItem(null===(t=this._shadowWidget.gridstackNode)||void 0===t?void 0:t.id,o)}this._shadowWidget=null,this.layout.grid.el.style.pointerEvents="auto"}}_setErrorMessage(e){const t=document.body.querySelector(".lm-mod-drag-image");if(t){let o=t.querySelector(".grid-stack-error");o||(o=t.appendChild(document.createElement("div")),o.className="grid-stack-error"),o.innerHTML=`<p>${e}</p>`}}}var D,H=o(881),R=o(355),B=o(661);!function(e){e[e.CLOSED=0]="CLOSED",e[e.LOCKED=1]="LOCKED",e[e.UNLOCKED=2]="UNLOCKED"}(D||(D={}));class G{constructor(e){this._cellId="",this._cellId=e.cellId,this._isLocked=e.isLocked,this._stateChanged=new I.Signal(this)}get cellId(){return this._cellId}get isLocked(){return this._isLocked}get stateChanged(){return this._stateChanged}dispose(){I.Signal.clearData(this)}close(){this._stateChanged.emit(D.CLOSED)}lock(){this._isLocked=!0,this._stateChanged.emit(D.LOCKED)}unlock(){this._isLocked=!1,this._stateChanged.emit(D.UNLOCKED)}}const T=new g.LabIcon({name:"@voila-dashboards/jupyterlab-gridstack:icon-delete",svgstr:'<svg width="16" height="16" version="1.1" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg">\n <g class="jp-icon3" transform="matrix(.03125 0 0 .03125 1.7764 0)" fill="#616161">\n  <path d="m156.37 30.906h85.57v14.398h30.902v-16.414c0.00391-15.93-12.949-28.891-28.871-28.891h-89.633c-15.922 0-28.875 12.961-28.875 28.891v16.414h30.906z"/>\n  <path d="m344.21 167.75h-290.11c-7.9492 0-14.207 6.7812-13.566 14.707l24.254 299.91c1.3516 16.742 15.316 29.637 32.094 29.637h204.54c16.777 0 30.742-12.895 32.094-29.641l24.254-299.9c0.64453-7.9258-5.6133-14.707-13.562-14.707zm-219.86 312.26c-0.32422 0.0195-0.64844 0.0312-0.96875 0.0312-8.1016 0-14.902-6.3086-15.406-14.504l-15.199-246.21c-0.52344-8.5195 5.957-15.852 14.473-16.375 8.4883-0.51562 15.852 5.9492 16.375 14.473l15.195 246.21c0.52734 8.5195-5.9531 15.848-14.469 16.375zm90.434-15.422c0 8.5312-6.918 15.449-15.453 15.449-8.5352 0-15.453-6.918-15.453-15.449v-246.21c0-8.5352 6.918-15.453 15.453-15.453 8.5312 0 15.453 6.918 15.453 15.453zm90.758-245.3-14.512 246.21c-0.48047 8.2109-7.293 14.543-15.41 14.543-0.30469 0-0.61328-8e-3 -0.92188-0.0234-8.5195-0.5039-15.02-7.8164-14.516-16.336l14.508-246.21c0.5-8.5195 7.7891-15.02 16.332-14.516 8.5195 0.5 15.02 7.8164 14.52 16.336z"/>\n  <path d="m397.65 120.06-10.148-30.422c-2.6758-8.0195-10.184-13.43-18.641-13.43h-339.41c-8.4531 0-15.965 5.4102-18.637 13.43l-10.148 30.422c-1.957 5.8672 0.58984 11.852 5.3438 14.836 1.9375 1.2148 4.2305 1.9453 6.75 1.9453h372.8c2.5195 0 4.8164-0.73047 6.75-1.9492 4.7539-2.9844 7.3008-8.9688 5.3438-14.832z"/>\n </g>\n</svg>\n'}),A=new g.LabIcon({name:"@voila-dashboards/jupyterlab-gridstack:icon-pin",svgstr:'<svg width="16" height="16" version="1.1" viewBox="0 0 17 17"  xmlns="http://www.w3.org/2000/svg">\n\t<g class="jp-icon3" transform="matrix(.03125 0 0 .03125 1.7764 0)" fill="#616161">\n\t\t<path d="M298.028 214.267L285.793 96H328c13.255 0 24-10.745 24-24V24c0-13.255-10.745-24-24-24H56C42.745 0 32 10.745 32 24v48c0 13.255 10.745 24 24 24h42.207L85.972 214.267C37.465 236.82 0 277.261 0 328c0 13.255 10.745 24 24 24h136v104.007c0 1.242.289 2.467.845 3.578l24 48c2.941 5.882 11.364 5.893 14.311 0l24-48a8.008 8.008 0 0 0 .845-3.578V352h136c13.255 0 24-10.745 24-24-.001-51.183-37.983-91.42-85.973-113.733z"/>\n\t</g>\n</svg>'}),P=new g.LabIcon({name:"@voila-dashboards/jupyterlab-gridstack:icon-unPin",svgstr:'<svg width="16" height="16" version="1.1" viewBox="0 0 24 24"  xmlns="http://www.w3.org/2000/svg">\n\t<g class="jp-icon3" fill="#616161">\n\t\t<path d="M9 9l7 7h-3v4l-1 3l-1-3v-4H6v-3l3-3V9zm8-7v2l-2 1v5l3 3v2.461L12.27 9.73L9 6.46V5L7 4V2h10z"/>\n\t\t<path d="M2.27 2.27L1 3.54L20.46 23l1.27-1.27L11 11z"/>\n\t</g>\n</svg>'});class O extends l.ReactWidget{constructor(e){super(),this._stateChanged=(e,t)=>{this.update()},this.addClass("grid-item-toolbar"),this._model=e,this._model.stateChanged.connect(this._stateChanged)}dispose(){this._model.stateChanged.disconnect(this._stateChanged),super.dispose()}render(){return c.createElement(c.Fragment,null,this._model.isLocked?c.createElement("button",{className:"bp3-button bp3-minimal jp-toolbar-button pin",onClick:()=>this._model.unlock()},c.createElement(P.react,{className:"jp-react-button"})):c.createElement("button",{className:"bp3-button bp3-minimal jp-toolbar-button pin",onClick:()=>this._model.lock()},c.createElement(A.react,{className:"jp-react-button"})),c.createElement("div",{className:"grid-item-toolbar-spacer"}),c.createElement("button",{className:"bp3-button bp3-minimal jp-toolbar-button trash-can",onClick:()=>this._model.close()},c.createElement(T.react,{className:"jp-react-button"})))}}class F extends x.Panel{constructor(e,t){super(),this.removeClass("lm-Widget"),this.removeClass("p-Widget"),this.addClass("grid-stack-item"),this._model=new G(t);const o=new x.Panel;o.addClass("grid-stack-item-content"),this._toolbar=new O(this._model),o.addWidget(this._toolbar),e.addClass("grid-item-widget"),o.addWidget(e),this.addWidget(o)}dispose(){this.isDisposed||(this._toolbar.dispose(),this._model.dispose(),super.dispose())}get cellId(){return this._model.cellId}get isLocked(){return this._model.isLocked}get stateChanged(){return this._model.stateChanged}}const z="grid_default";class V{constructor(e){this._mutex=(0,R.createMutex)(),this._itemChanged=(e,t)=>{switch(t){case D.CLOSED:this.hideCell(e.cellId),e.stateChanged.disconnect(this._itemChanged),e.dispose();break;case D.LOCKED:this.lockCell(e.cellId,!0);break;case D.UNLOCKED:this.lockCell(e.cellId,!1)}},this._ystate=new B.Map,this._context=e.context,this.rendermime=e.rendermime,this.contentFactory=e.contentFactory,this.mimeTypeService=e.mimeTypeService,this._editorConfig=e.editorConfig,this._notebookConfig=e.notebookConfig,this._ready=new I.Signal(this),this._cellRemoved=new I.Signal(this),this._cellPinned=new I.Signal(this),this._stateChanged=new I.Signal(this),this._contentChanged=new I.Signal(this),this._info={name:"grid",type:"grid",maxColumns:12,cellMargin:2,defaultCellHeight:40},this._context.sessionContext.ready.then((()=>{this._checkMetadata(),this._checkCellsMetadata();const e=this._context.model.sharedModel;this._ystate=e.ystate,!0!==this._ystate.get("executed")&&e.transact((()=>{this._ystate.set("executed",!1)}),!1),this._context.save().then((e=>{this._ready.emit(null)}))})),this._context.model.contentChanged.connect(this._updateCells,this)}get ready(){return this._ready}get cellRemoved(){return this._cellRemoved}get cellPinned(){return this._cellPinned}get stateChanged(){return this._stateChanged}get contentChanged(){return this._contentChanged}get editorConfig(){return this._editorConfig}set editorConfig(e){this._editorConfig=e}get notebookConfig(){return this._notebookConfig}set notebookConfig(e){this._notebookConfig=e}set executed(e){this._ystate.set("executed",e)}get info(){return this._info}set info(e){this._info=e,this._mutex((()=>{const e=this._context.model.sharedModel.getMetadata();e.extensions.jupyter_dashboards.views[z]=this._info,this._context.model.sharedModel.setMetadata(e),this._context.model.dirty=!0}))}get cells(){return this._context.model.cells}get deletedCells(){return this._context.model.deletedCells}getCellInfo(e){var t;for(let o=0;o<(null===(t=this._context.model.cells)||void 0===t?void 0:t.length);o++){const t=this._context.model.cells.get(o);if(t.id===e)return t.sharedModel.getMetadata().extensions.jupyter_dashboards.views[z]}}setCellInfo(e,t){var o;for(let i=0;i<(null===(o=this._context.model.cells)||void 0===o?void 0:o.length);i++){const o=this._context.model.cells.get(i);if(o.id===e){this._mutex((()=>{const e=o.sharedModel.getMetadata().extensions;e.jupyter_dashboards.views[z]=t,o.sharedModel.setMetadata({extensions:e}),this._context.model.dirty=!0}));break}}}hideCell(e){var t;for(let o=0;o<(null===(t=this._context.model.cells)||void 0===t?void 0:t.length);o++){const t=this._context.model.cells.get(o);if(t.id===e){this._mutex((()=>{const o=t.sharedModel.getMetadata().extensions;o.jupyter_dashboards.views[z].hidden=!0,t.sharedModel.setMetadata({extensions:o}),this._context.model.dirty=!0,this._cellRemoved.emit({id:e,info:o.jupyter_dashboards.views[z]})}));break}}}lockCell(e,t){var o;for(let i=0;i<(null===(o=this._context.model.cells)||void 0===o?void 0:o.length);i++){const o=this._context.model.cells.get(i);if(o.id===e){this._mutex((()=>{const i=o.sharedModel.getMetadata().extensions;i.jupyter_dashboards.views[z].locked=t,o.sharedModel.setMetadata({extensions:i}),this._context.model.dirty=!0,this._cellPinned.emit({id:e,info:i.jupyter_dashboards.views[z]})}));break}}}createCell(e,t){let o;switch(e.type){case"code":{const t=new M.CodeCell({model:e,rendermime:this.rendermime,contentFactory:this.contentFactory,editorConfig:this._editorConfig.code,updateEditorOnShow:!0});o=new H.SimplifiedOutputArea({model:t.outputArea.model,rendermime:t.outputArea.rendermime,contentFactory:t.outputArea.contentFactory});break}case"markdown":{const t=new M.MarkdownCell({model:e,rendermime:this.rendermime,contentFactory:this.contentFactory,editorConfig:this._editorConfig.markdown,updateEditorOnShow:!1});t.inputHidden=!1,t.rendered=!0,K.removeElements(t.node,"jp-Collapser"),K.removeElements(t.node,"jp-InputPrompt"),o=t;break}default:{const t=new M.RawCell({model:e,contentFactory:this.contentFactory,editorConfig:this._editorConfig.raw,updateEditorOnShow:!1});t.inputHidden=!1,K.removeElements(t.node,"jp-Collapser"),K.removeElements(t.node,"jp-InputPrompt"),o=t;break}}const i={cellId:e.id,cellWidget:o,isLocked:t},s=new F(o,i);return s.stateChanged.connect(this._itemChanged),s}execute(e){if("code"!==e.type||this._ystate.get("executed"))return;const t=new M.CodeCell({model:e,rendermime:this.rendermime,contentFactory:this.contentFactory,editorConfig:this._editorConfig.code,updateEditorOnShow:!0});H.SimplifiedOutputArea.execute(e.value.text,t.outputArea,this._context.sessionContext).then((t=>{"execute_reply"===(null==t?void 0:t.header.msg_type)&&"ok"===t.content.status&&(e.executionCount=t.content.execution_count)})).catch((e=>console.error(e)))}_updateCells(){this._mutex((()=>{this._checkCellsMetadata(),this._contentChanged.emit(null)}))}_checkMetadata(){var e;let t=this._context.model.sharedModel.getMetadata().extensions;var o;t?t.jupyter_dashboards?(o=t.jupyter_dashboards.views[z])&&"name"in o&&"type"in o&&"maxColumns"in o&&"cellMargin"in o&&"defaultCellHeight"in o?this._info=null===(e=t.jupyter_dashboards)||void 0===e?void 0:e.views[z]:t.jupyter_dashboards.views[z]=this._info:t.jupyter_dashboards={version:1,activeView:z,views:{grid_default:this._info}}:t={jupyter_dashboards:{version:1,activeView:z,views:{grid_default:this._info}}},this._mutex((()=>{this._context.model.sharedModel.updateMetadata({extensions:t})}))}_checkCellsMetadata(){var e;for(let t=0;t<(null===(e=this._context.model.cells)||void 0===e?void 0:e.length);t++){const e=this._context.model.cells.get(t);this._checkCellMetadata(e)}}_checkCellMetadata(e){let t=e.sharedModel.getMetadata().extensions;var o;t?t.jupyter_dashboards?(o=t.jupyter_dashboards.views[z])&&"hidden"in o&&"row"in o&&"col"in o&&"width"in o&&"height"in o&&"locked"in o||(t.jupyter_dashboards.views[z]={hidden:!0,row:null,col:null,width:2,height:2,locked:!0},this._mutex((()=>{e.sharedModel.setMetadata({extensions:t})}))):(t.jupyter_dashboards={activeView:z,views:{grid_default:{hidden:!0,row:null,col:null,width:2,height:2,locked:!0}}},this._mutex((()=>{e.sharedModel.setMetadata({extensions:t})}))):(t={jupyter_dashboards:{activeView:z,views:{grid_default:{hidden:!0,row:null,col:null,width:2,height:2,locked:!0}}}},this._mutex((()=>{e.sharedModel.setMetadata({extensions:t})})))}}var K;!function(e){e.removeElements=function(e,t){const o=e.getElementsByClassName(t);for(let e=0;e<o.length;e++)o[e].remove()}}(K||(K={}));class U extends x.Panel{constructor(e){super(),this.addClass("jp-Notebook"),this.addClass("jp-NotebookPanel-notebook"),this.addClass("grid-panel"),this.node.dataset.jpUndoer="true",this._context=e.context,this.rendermime=e.rendermime,this.contentFactory=e.contentFactory,this.mimeTypeService=e.mimeTypeService,this._editorConfig=e.editorConfig,this._notebookConfig=e.notebookConfig;const t=new V({context:this._context,rendermime:this.rendermime,contentFactory:this.contentFactory,mimeTypeService:this.mimeTypeService,editorConfig:this._editorConfig,notebookConfig:this._notebookConfig});this._gridstackWidget=new L(t),this.addWidget(this._gridstackWidget)}dispose(){this._gridstackWidget=void 0,I.Signal.clearData(this),super.dispose()}get editorConfig(){return this._editorConfig}set editorConfig(e){this._editorConfig=e}get notebookConfig(){return this._notebookConfig}set notebookConfig(e){this._notebookConfig=e}get gridWidgets(){var e,t;return null!==(t=null===(e=this._gridstackWidget)||void 0===e?void 0:e.gridWidgets)&&void 0!==t?t:[]}onUpdateRequest(e){var t;null===(t=this._gridstackWidget)||void 0===t||t.update()}compact(){(0,l.showDialog)({title:"Compact the grid layout",body:"Only unlocked cell will move.",buttons:[l.Dialog.okButton()]}).then((e=>{var t;null===(t=this._gridstackWidget)||void 0===t||t.compact()}))}info(){var e;null===(e=this._gridstackWidget)||void 0===e||e.infoEditor()}revert(){this._context.model.dirty?(0,l.showDialog)({title:"Reload Notebook from Disk",body:"Are you sure you want to reload the Notebook from the disk?",buttons:[l.Dialog.cancelButton(),l.Dialog.warnButton({label:"Reload"})]}).then((e=>{e.button.accept&&!this._context.isDisposed&&this._context.revert()})):this._context.isDisposed||this._context.revert()}save(){this._context.save()}}class $ extends a.ABCWidgetFactory{constructor(e){super(e),this.rendermime=e.rendermime,this.contentFactory=e.contentFactory||s.NotebookPanel.defaultContentFactory,this.mimeTypeService=e.mimeTypeService,this._editorConfig=e.editorConfig||s.StaticNotebook.defaultEditorConfig,this._notebookConfig=e.notebookConfig||s.StaticNotebook.defaultNotebookConfig}get editorConfig(){return this._editorConfig}set editorConfig(e){this._editorConfig=e}get notebookConfig(){return this._notebookConfig}set notebookConfig(e){this._notebookConfig=e}createNewWidget(e,t){const o={context:e,rendermime:t?t.content.rendermime:this.rendermime.clone({resolver:e.urlResolver}),contentFactory:this.contentFactory,mimeTypeService:this.mimeTypeService,editorConfig:t?t.content.editorConfig:this._editorConfig,notebookConfig:t?t.content.notebookConfig:this._notebookConfig};return new b(e,new U(o))}}class Y{constructor(e){this._commands=e}createNew(e){const t=new l.ToolbarButton({tooltip:"Open with Voilà GridStack editor",icon:u,onClick:()=>{this._commands.execute("docmanager:open",{path:e.context.path,factory:"Voila GridStack",options:{mode:"split-right",ref:e.id}}).then((t=>{t instanceof x.Widget&&e.content.disposed.connect((()=>{t.dispose()}))}))}});return e.toolbar.insertAfter("voila","jupyterlab-gridstack",t),t}}class q{createNew(e){const t=new l.ToolbarButton({tooltip:"Open with Voilà Gridstack in a New Browser Tab",icon:g.launcherIcon,onClick:()=>{const t=f.PageConfig.getBaseUrl(),o=window.open(`${t}voila/render/${e.context.path}?voila-template=gridstack`,"_blank");null==o||o.focus()}});return e.toolbar.insertAfter("cellType","voila",t),t}}const X={id:"@voila-dashboards/jupyterlab-gridstack:editor",autoStart:!0,provides:k,requires:[s.NotebookPanel.IContentFactory,r.IMainMenu,d.IEditorServices,n.IRenderMimeRegistry],optional:[i.ILayoutRestorer],activate:(e,t,o,i,n,d)=>{const r=new l.WidgetTracker({namespace:"jupyterlab-gridstack"});d&&d.restore(r,{command:"docmanager:open",args:e=>({path:e.context.path,factory:"Voila GridStack"}),name:e=>e.context.path,when:e.serviceManager.ready});const a=new $({name:"Voila GridStack",fileTypes:["notebook"],modelName:"notebook",preferKernel:!0,canStartKernel:!0,rendermime:n,contentFactory:t,editorConfig:s.StaticNotebook.defaultEditorConfig,notebookConfig:s.StaticNotebook.defaultNotebookConfig,mimeTypeService:i.mimeTypeService});return a.widgetCreated.connect(((t,o)=>{o.context.pathChanged.connect((()=>{r.save(o)})),r.add(o),o.update(),e.commands.notifyCommandChanged()})),o.editMenu.undoers.add({tracker:r,undo:e=>e.undo(),redo:e=>e.redo()}),e.docRegistry.addWidgetFactory(a),e.docRegistry.addWidgetExtension("Notebook",new q),e.docRegistry.addWidgetExtension("Notebook",new Y(e.commands)),r}};var J=o(728),Q=o(292);function*Z(e){for(const t of e.gridWidgets)t instanceof Q.WidgetRenderer&&(yield t)}const ee={id:"@voila-dashboards/jupyterlab-gridstack:widgets",autoStart:!0,optional:[k,J.IJupyterWidgetRegistry],activate:(e,t,o)=>{o&&(null==t||t.forEach((e=>{(0,Q.registerWidgetManager)(e.context,e.content.rendermime,Z(e.content))})),null==t||t.widgetAdded.connect(((e,t)=>{(0,Q.registerWidgetManager)(t.context,t.content.rendermime,Z(t.content))})),console.log(ee.id,"activated"))}},te=[X,ee]}}]);