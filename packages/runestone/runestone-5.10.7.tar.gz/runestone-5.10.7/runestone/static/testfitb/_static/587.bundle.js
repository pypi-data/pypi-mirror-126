(self.webpackChunkWebComponents=self.webpackChunkWebComponents||[]).push([[587],{2568:(e,t,o)=>{"use strict";o.d(t,{Z:()=>i});var s=o(21294);class i{constructor(e){this.component_ready_promise=new Promise((e=>this._component_ready_resolve_fn=e)),this.optional=!1,void 0===window.allComponents&&(window.allComponents=[]),window.allComponents.push(this),e&&(this.sid=e.sid,this.graderactive=e.graderactive,this.showfeedback=!0,e.timed&&(this.isTimed=!0),e.enforceDeadline&&(this.deadline=e.deadline),$(e.orig).data("optional")?this.optional=!0:this.optional=!1,e.selector_id&&(this.selector_id=e.selector_id),void 0!==e.assessmentTaken?this.assessmentTaken=e.assessmentTaken:this.assessmentTaken=!0,void 0!==e.timedWrapper?this.timedWrapper=e.timedWrapper:location.href.indexOf("doAssignment")>=0?this.timedWrapper=$("h1#assignment_name").text():this.timedWrapper=null,$(e.orig).data("question_label")&&(this.question_label=$(e.orig).data("question_label"))),this.jsonHeaders=new Headers({"Content-type":"application/json; charset=utf-8",Accept:"application/json"})}async logBookEvent(e){if(this.graderactive)return;let t;return e.course=eBookConfig.course,e.clientLoginStatus=eBookConfig.isLoggedIn,e.timezoneoffset=(new Date).getTimezoneOffset()/60,this.percent&&(e.percent=this.percent),eBookConfig.useRunestoneServices&&eBookConfig.logLevel>0&&(t=this.postLogMessage(e)),this.isTimed&&!eBookConfig.debug||console.log("logging event "+JSON.stringify(e)),this.selector_id&&(e.div_id=this.selector_id.replace("-toggleSelectedQuestion",""),e.event="selectquestion",e.act="interaction",this.postLogMessage(e)),"function"==typeof s.j.updateProgress&&"edit"!=e.act&&0==this.optional&&s.j.updateProgress(e.div_id),t}async postLogMessage(e){var t;let o=new Request(eBookConfig.ajaxURL+"hsblog",{method:"POST",headers:this.jsonHeaders,body:JSON.stringify(e)});try{let e=await fetch(o);if(!e.ok)throw new Error("Failed to save the log entry");t=e.json()}catch(e){this.isTimed&&alert(`Error: Your action was not saved! The error was ${e}`),console.log(`Error: ${e}`)}return t}async logRunEvent(e){let t="done";if(!this.graderactive){if(e.course=eBookConfig.course,e.clientLoginStatus=eBookConfig.isLoggedIn,e.timezoneoffset=(new Date).getTimezoneOffset()/60,(this.forceSave||"to_save"in e==0)&&(e.save_code="True"),eBookConfig.useRunestoneServices&&eBookConfig.logLevel>0){let o=new Request(eBookConfig.ajaxURL+"runlog.json",{method:"POST",headers:this.jsonHeaders,body:JSON.stringify(e)}),s=await fetch(o);if(!s.ok)throw new Error("Failed to log the run");t=await s.json()}return this.isTimed&&!eBookConfig.debug||console.log("running "+JSON.stringify(e)),"function"==typeof s.j.updateProgress&&0==this.optional&&s.j.updateProgress(e.div_id),t}}async checkServer(e,t=!1){let o=this;if(this.checkServerComplete=new Promise((function(e,t){o.csresolver=e})),this.useRunestoneServices||this.graderactive){let t={};if(t.div_id=this.divid,t.course=eBookConfig.course,t.event=e,this.graderactive&&this.deadline&&(t.deadline=this.deadline,t.rawdeadline=this.rawdeadline,t.tzoff=this.tzoff),this.sid&&(t.sid=this.sid),!eBookConfig.practice_mode&&this.assessmentTaken){let e=new Request(eBookConfig.ajaxURL+"getAssessResults",{method:"POST",body:JSON.stringify(t),headers:this.jsonHeaders});try{let o=await fetch(e);t=await o.json(),this.repopulateFromStorage(t),this.csresolver("server")}catch(e){try{this.checkLocalStorage()}catch(e){console.log(e)}}}else this.loadData({}),this.csresolver("not taken")}else this.checkLocalStorage(),this.csresolver("local");t&&this.indicate_component_ready()}indicate_component_ready(){this.containerDiv.classList.add("runestone-component-ready"),this._component_ready_resolve_fn()}loadData(e){return null}repopulateFromStorage(e){null!==e&&this.shouldUseServer(e)?(this.restoreAnswers(e),this.setLocalStorage(e)):this.checkLocalStorage()}shouldUseServer(e){if("T"===e.correct||0===localStorage.length||!0===this.graderactive||this.isTimed)return!0;let t,o=localStorage.getItem(this.localStorageKey());if(null===o)return!0;try{t=JSON.parse(o)}catch(e){return console.log(e.message),localStorage.removeItem(this.localStorageKey()),!0}if(e.answer==t.answer)return!0;let s=new Date(t.timestamp);return new Date(e.timestamp)>=s}localStorageKey(){return eBookConfig.email+":"+eBookConfig.course+":"+this.divid+"-given"}addCaption(e){if(!this.isTimed){var t=document.createElement("p");this.question_label?(this.caption=`Activity: ${this.question_label} ${this.caption}  <span class="runestone_caption_divid">(${this.divid})</span>`,$(t).html(this.caption),$(t).addClass(`${e}_caption`)):($(t).html(this.caption+" ("+this.divid+")"),$(t).addClass(`${e}_caption`),$(t).addClass(`${e}_caption_text`)),this.capDiv=t,this.containerDiv.appendChild(t)}}hasUserActivity(){return this.isAnswered}checkCurrentAnswer(){console.log("Each component should provide an implementation of checkCurrentAnswer")}async logCurrentAnswer(){console.log("Each component should provide an implementation of logCurrentAnswer")}renderFeedback(){console.log("Each component should provide an implementation of renderFeedback")}disableInteraction(){console.log("Each component should provide an implementation of disableInteraction")}toString(){return`${this.constructor.name}: ${this.divid}`}queueMathJax(e){"2"===MathJax.version.substring(0,1)?MathJax.Hub.Queue(["Typeset",MathJax.Hub,e]):MathJax.typesetPromise([e])}}window.RunestoneBase=i}}]);
//# sourceMappingURL=587.bundle.js.map?v=5446280573cc393bc926