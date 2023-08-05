(self["webpackChunkWebComponents"] = self["webpackChunkWebComponents"] || []).push([["runestone_selectquestion_js_selectone_js"],{

/***/ 21823:
/*!***********************************************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./runestone/selectquestion/css/selectquestion.css ***!
  \***********************************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ 94015);
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/api.js */ 23645);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".toggle-preview {\n    border: 4px solid;\n    border-radius: 10px;\n    background-color: azure;\n    padding-top: 10px;\n    box-shadow: 10px 5px 5px gray;\n}\n", "",{"version":3,"sources":["webpack://./runestone/selectquestion/css/selectquestion.css"],"names":[],"mappings":"AAAA;IACI,iBAAiB;IACjB,mBAAmB;IACnB,uBAAuB;IACvB,iBAAiB;IACjB,6BAA6B;AACjC","sourcesContent":[".toggle-preview {\n    border: 4px solid;\n    border-radius: 10px;\n    background-color: azure;\n    padding-top: 10px;\n    box-shadow: 10px 5px 5px gray;\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ 40141:
/*!*********************************************************!*\
  !*** ./runestone/selectquestion/css/selectquestion.css ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ 93379);
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_selectquestion_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../../../node_modules/css-loader/dist/cjs.js!./selectquestion.css */ 21823);

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_selectquestion_css__WEBPACK_IMPORTED_MODULE_1__.default, options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_selectquestion_css__WEBPACK_IMPORTED_MODULE_1__.default.locals || {});

/***/ }),

/***/ 72773:
/*!************************************************!*\
  !*** ./runestone/common/js/renderComponent.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "renderRunestoneComponent": () => (/* binding */ renderRunestoneComponent),
/* harmony export */   "createTimedComponent": () => (/* binding */ createTimedComponent)
/* harmony export */ });
/* harmony import */ var _webpack_index_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../webpack.index.js */ 36350);


async function renderRunestoneComponent(componentSrc, whereDiv, moreOpts) {
    /**
     *  The easy part is adding the componentSrc to the existing div.
     *  The tedious part is calling the right functions to turn the
     *  source into the actual component.
     */
    let patt = /..\/_images/g;
    componentSrc = componentSrc.replace(
        patt,
        `${eBookConfig.app}/books/published/${eBookConfig.basecourse}/_images`
    );
    jQuery(`#${whereDiv}`).html(componentSrc);

    if (typeof window.edList === "undefined") {
        window.edList = {};
    }

    let componentKind = $($(`#${whereDiv} [data-component]`)[0]).data(
        "component"
    );
    // Import the JavaScript for this component before proceeding.
    await (0,_webpack_index_js__WEBPACK_IMPORTED_MODULE_0__.runestone_import)(componentKind);
    let opt = {};
    opt.orig = jQuery(`#${whereDiv} [data-component]`)[0];
    if (opt.orig) {
        opt.lang = $(opt.orig).data("lang");
        opt.useRunestoneServices = true;
        opt.graderactive = false;
        opt.python3 = true;
        if (typeof moreOpts !== "undefined") {
            for (let key in moreOpts) {
                opt[key] = moreOpts[key];
            }
        }
    }

    if (typeof component_factory === "undefined") {
        alert(
            "Error:  Missing the component factory!  Clear you browser cache."
        );
    } else {
        if (
            !window.component_factory[componentKind] &&
            !jQuery(`#${whereDiv}`).html()
        ) {
            jQuery(`#${whereDiv}`).html(
                `<p>Preview not available for ${componentKind}</p>`
            );
        } else {
            let res = window.component_factory[componentKind](opt);
            if (componentKind === "activecode") {
                if (moreOpts.multiGrader) {
                    window.edList[
                        `${moreOpts.gradingContainer} ${res.divid}`
                    ] = res;
                } else {
                    window.edList[res.divid] = res;
                }
            }
        }
    }
}

function createTimedComponent(componentSrc, moreOpts) {
    /* The important distinction is that the component does not really need to be rendered
    into the page, in fact, due to the async nature of getting the source the list of questions
    is made and the original html is replaced by the look of the exam.
    */

    let patt = /..\/_images/g;
    componentSrc = componentSrc.replace(
        patt,
        `${eBookConfig.app}/books/published/${eBookConfig.basecourse}/_images`
    );

    let componentKind = $($(componentSrc).find("[data-component]")[0]).data(
        "component"
    );

    let origId = $(componentSrc).find("[data-component]").first().attr("id");

    // Double check -- if the component source is not in the DOM, then briefly add it
    // and call the constructor.
    let hdiv;
    if (!document.getElementById(origId)) {
        hdiv = $("<div/>", {
            css: { display: "none" },
        }).appendTo("body");
        hdiv.html(componentSrc);
    }
    // at this point hdiv is a jquery object

    let ret;
    let opts = {
        orig: document.getElementById(origId),
        timed: true,
    };
    if (typeof moreOpts !== "undefined") {
        for (let key in moreOpts) {
            opts[key] = moreOpts[key];
        }
    }

    if (componentKind in window.component_factory) {
        ret = window.component_factory[componentKind](opts);
    }

    let rdict = {};
    rdict.question = ret;
    return rdict;
}


/***/ }),

/***/ 63931:
/*!**************************************************!*\
  !*** ./runestone/selectquestion/js/selectone.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ SelectOne)
/* harmony export */ });
/* harmony import */ var _common_js_renderComponent_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../common/js/renderComponent.js */ 72773);
/* harmony import */ var _common_js_runestonebase_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../common/js/runestonebase.js */ 2568);
/* harmony import */ var _css_selectquestion_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../css/selectquestion.css */ 40141);
/**
 * *******************************
 * |docname| - SelectOne Component
 * *******************************
 */




class SelectOne extends _common_js_runestonebase_js__WEBPACK_IMPORTED_MODULE_1__.default {
    /**
     * constructor --
     * Making an instance of a selectone is a bit more complicated because it is
     * a kind of meta directive.  That is, go to the server and randomly select
     * a question to display in this spot.  Or, if a student has already seen this question
     * in the context of an exam retrieve the question they saw in the first place.
     * Making an API call and waiting for the response is handled asynchronously.
     * But lots of code is not written with that assumption.  So we do the initialization in
     * two parts.
     * 1. Create the object with the usual constructor
     * 2. call initialize, which returns a promise.  When that promise is resolved
     * the "replacement" component will replace the original selectone component in the DOM.
     *
     * @param  {} opts
     */
    constructor(opts) {
        super(opts);
        this.origOpts = opts;
        this.questions = $(opts.orig).data("questionlist");
        this.proficiency = $(opts.orig).data("proficiency");
        this.minDifficulty = $(opts.orig).data("minDifficulty");
        this.maxDifficulty = $(opts.orig).data("maxDifficulty");
        this.points = $(opts.orig).data("points");
        this.autogradable = $(opts.orig).data("autogradable");
        this.not_seen_ever = $(opts.orig).data("not_seen_ever");
        this.selector_id = $(opts.orig).first().attr("id");
        this.primaryOnly = $(opts.orig).data("primary");
        this.ABExperiment = $(opts.orig).data("ab");
        this.toggleOptions = $(opts.orig).data("toggleoptions");
        this.toggleLabels = $(opts.orig).data("togglelabels");
        opts.orig.id = this.selector_id;
    }
    /**
     * initialize --
     * initialize is used so that the constructor does not have to be async.
     * Constructors should definitely not return promises that would seriously
     * mess things up.
     * @return {Promise} Will resolve after component from DB is reified
     */
    async initialize() {
        let self = this;
        let data = { selector_id: this.selector_id };
        if (this.questions) {
            data.questions = this.questions;
        } else if (this.proficiency) {
            data.proficiency = this.proficiency;
        }
        if (this.minDifficulty) {
            data.minDifficulty = this.minDifficulty;
        }
        if (this.maxDifficulty) {
            data.maxDifficulty = this.maxDifficulty;
        }
        if (this.points) {
            data.points = this.points;
        }
        if (this.autogradable) {
            data.autogradable = this.autogradable;
        }
        if (this.not_seen_ever) {
            data.not_seen_ever = this.not_seen_ever;
        }
        if (this.primaryOnly) {
            data.primary = this.primaryOnly;
        }
        if (this.ABExperiment) {
            data.AB = this.ABExperiment;
        }
        if (this.timedWrapper) {
            data.timedWrapper = this.timedWrapper;
        }
        if (this.toggleOptions) {
            data.toggleOptions = this.toggleOptions;
        }
        if (this.toggleLabels) {
            data.toggleLabels = this.toggleLabels;
        }
        let opts = this.origOpts;
        let selectorId = this.selector_id;
        console.log("getting question source");
        let request = new Request("/runestone/ajax/get_question_source", {
            method: "POST",
            headers: this.jsonHeaders,
            body: JSON.stringify(data),
        });
        let response = await fetch(request);
        let htmlsrc = await response.json();
        if (htmlsrc.indexOf("No preview") >= 0) {
            alert(
                `Error: Not able to find a question for ${selectorId} based on the criteria`
            );
            throw new Error(`Unable to find a question for ${selectorId}`);
        }
        let res;
        if (opts.timed) {
            // timed components are not rendered immediately, only when the student
            // starts the assessment and visits this particular entry.
            res = (0,_common_js_renderComponent_js__WEBPACK_IMPORTED_MODULE_0__.createTimedComponent)(htmlsrc, {
                timed: true,
                selector_id: selectorId,
                assessmentTaken: opts.assessmentTaken,
            });
            // replace the entry in the timed assessment's list of components
            // with the component created by createTimedComponent
            for (let component of opts.rqa) {
                if (component.question == self) {
                    component.question = res.question;
                    break;
                }
            }
            self.realComponent = res.question;
            self.containerDiv = res.question.containerDiv;
            self.realComponent.selectorId = selectorId;
        } else {
            if (data.toggleOptions) {
                var toggleLabels = data.toggleLabels.replace("togglelabels:", "").trim();
                if (toggleLabels) {
                    toggleLabels = toggleLabels.split(",");
                    for (var t = 0; t < toggleLabels.length; t++) {
                        toggleLabels[t] = toggleLabels[t].trim();
                    }
                }
                var toggleQuestions = this.questions.split(", ");
                var toggleUI = "";
                // check so that only the first toggle select question on the assignments page has a preview panel created, then all toggle select previews use this same panel
                if (!document.getElementById("component-preview")) {
                    toggleUI +=
                        '<div id="component-preview" class="col-md-6 toggle-preview" style="z-index: 999;">' +
                            '<div id="toggle-buttons"></div>' +
                            '<div id="toggle-preview"></div>' +
                        '</div>';
                }
                // dropdown menu containing the question options
                toggleUI +=
                    '<label for="' +
                    selectorId +
                    '-toggleQuestion" style="margin-left: 10px">Toggle Question:</label><select id="' +
                    selectorId +
                    '-toggleQuestion">';
                var i;
                var toggleQuestionHTMLSrc;
                var toggleQuestionSubstring;
                var toggleQuestionType;
                var toggleQuestionTypes = [];
                for (i = 0; i < toggleQuestions.length; i++) {
                    toggleQuestionHTMLSrc = await this.getToggleSrc(
                        toggleQuestions[i]
                    );
                    toggleQuestionSubstring = toggleQuestionHTMLSrc.split(
                        'data-component="'
                    )[1];
                    switch (
                        toggleQuestionSubstring.slice(
                            0,
                            toggleQuestionSubstring.indexOf('"')
                        )
                    ) {
                        case "activecode":
                            toggleQuestionType = "Active Write Code";
                            break;
                        case "clickablearea":
                            toggleQuestionType = "Clickable Area";
                            break;
                        case "dragndrop":
                            toggleQuestionType = "Drag n Drop";
                            break;
                        case "fillintheblank":
                            toggleQuestionType = "Fill in the Blank";
                            break;
                        case "multiplechoice":
                            toggleQuestionType = "Multiple Choice";
                            break;
                        case "parsons":
                            toggleQuestionType = "Parsons Mixed-Up Code";
                            break;
                        case "shortanswer":
                            toggleQuestionType = "Short Answer";
                            break;
                    }
                    toggleQuestionTypes[i] = toggleQuestionType;
                    toggleUI +=
                        '<option value="' +
                        toggleQuestions[i] +
                        '">';
                    if (toggleLabels) {
                        if (toggleLabels[i]) {
                            toggleUI += toggleLabels[i];
                        }
                        else {
                            toggleUI += toggleQuestionType +
                            " - " +
                            toggleQuestions[i];
                        }
                    }
                    else {
                        toggleUI += toggleQuestionType +
                        " - " +
                        toggleQuestions[i];
                    }
                    if ((i == 0) && (data.toggleOptions.includes("lock"))) {
                        toggleUI += " (only this question will be graded)";
                    }
                    toggleUI += "</option>";
                }
                toggleUI +=
                    '</select><div id="' +
                    selectorId +
                    '-toggleSelectedQuestion">';
                var toggleFirstID = htmlsrc.split('id="')[1];
                toggleFirstID = toggleFirstID.split('"')[0];
                htmlsrc = toggleUI + htmlsrc + "</div>";
            }
            // just render this component on the page in its usual place
            await (0,_common_js_renderComponent_js__WEBPACK_IMPORTED_MODULE_0__.renderRunestoneComponent)(htmlsrc, selectorId, {
                selector_id: selectorId,
                useRunestoneServices: true,
            });
            if (data.toggleOptions) {
                $("#component-preview").hide();
                var toggleQuestionSelect = document.getElementById(
                    selectorId + "-toggleQuestion"
                );
                for (i = 0; i < toggleQuestionSelect.options.length; i++) {
                    if (
                        toggleQuestionSelect.options[i].value == toggleFirstID
                    ) {
                        toggleQuestionSelect.value = toggleFirstID;
                        $("#" + selectorId).data(
                            "toggle_current",
                            toggleFirstID
                        );
                        $("#" + selectorId).data(
                            "toggle_current_type",
                            toggleQuestionTypes[0]
                        );
                        break;
                    }
                }
                toggleQuestionSelect.addEventListener(
                    "change",
                    async function () {
                        await this.togglePreview(
                            toggleQuestionSelect.parentElement.id,
                            data.toggleOptions,
                            toggleQuestionTypes
                        );
                    }.bind(this)
                );
            }
        }
        return response;
    }

    // retrieve html source of a question, for use in various toggle functionalities
    async getToggleSrc(toggleQuestionID) {
        let request = new Request(
            "/runestone/admin/htmlsrc?acid=" + toggleQuestionID,
            {
                method: "GET",
            }
        );
        let response = await fetch(request);
        let htmlsrc = await response.json();
        return htmlsrc;
    }

    // on changing the value of toggle select dropdown, render selected question in preview panel, add appropriate buttons, then make preview panel visible
    async togglePreview(parentID, toggleOptions, toggleQuestionTypes) {
        $("#toggle-buttons").html("");
        var parentDiv = document.getElementById(parentID);
        var toggleQuestionSelect = parentDiv.getElementsByTagName("select")[0];
        var selectedQuestion =
            toggleQuestionSelect.options[toggleQuestionSelect.selectedIndex]
                .value;
        var htmlsrc = await this.getToggleSrc(selectedQuestion);
        (0,_common_js_renderComponent_js__WEBPACK_IMPORTED_MODULE_0__.renderRunestoneComponent)(htmlsrc, "toggle-preview", {
            selector_id: "toggle-preview",
            useRunestoneServices: true,
        });

        // add "Close Preview" button to the preview panel
        let closeButton = document.createElement("button");
        $(closeButton).text("Close Preview");
        $(closeButton).addClass("btn btn-default");
        $(closeButton).click(function (event) {
            $("#toggle-preview").html("");
            toggleQuestionSelect.value = $("#" + parentID).data(
                "toggle_current"
            );
            $("#component-preview").hide();
        });
        $("#toggle-buttons").append(closeButton);

        // if "lock" is not in toggle options, then allow adding more buttons to the preview panel 
        if (!(toggleOptions.includes("lock"))) {
            let setButton = document.createElement("button");
            $(setButton).text("Select this Problem");
            $(setButton).addClass("btn btn-primary");
            $(setButton).click(
                async function () {
                    await this.toggleSet(parentID, selectedQuestion, htmlsrc, toggleQuestionTypes);
                    $("#component-preview").hide();
                }.bind(this)
            );
            $("#toggle-buttons").append(setButton);

            // if "transfer" in toggle options, and if current question type is Parsons and selected question type is active code, then add "Transfer" button to preview panel
            if (toggleOptions.includes("transfer")) {
                var currentType = $("#" + parentID).data("toggle_current_type");
                var selectedType = toggleQuestionTypes[toggleQuestionSelect.selectedIndex];
                if ((currentType == "Parsons Mixed-Up Code") && (selectedType == "Active Write Code")) {
                    let transferButton = document.createElement("button");
                    $(transferButton).text("Transfer Response");
                    $(transferButton).addClass("btn btn-primary");
                    $(transferButton).click(
                        async function () {
                            await this.toggleTransfer(parentID, selectedQuestion, htmlsrc, toggleQuestionTypes);
                        }.bind(this)
                    );
                    $("#toggle-buttons").append(transferButton);
                }
            }
        }

        $("#component-preview").show();
    }

    // on clicking "Select this Problem" button, close preview panel, replace current question in assignments page with selected question, and send request to update grading database
    async toggleSet(parentID, selectedQuestion, htmlsrc, toggleQuestionTypes) {
        var selectorId = parentID + "-toggleSelectedQuestion";
        var toggleQuestionSelect = document.getElementById(parentID).getElementsByTagName("select")[0];
        document.getElementById(selectorId).innerHTML = ""; // need to check whether this is even necessary
        await (0,_common_js_renderComponent_js__WEBPACK_IMPORTED_MODULE_0__.renderRunestoneComponent)(htmlsrc, selectorId, {
            selector_id: selectorId,
            useRunestoneServices: true,
        });
        let request = new Request(
            "/runestone/ajax/update_selected_question?metaid=" +
                parentID +
                "&selected=" +
                selectedQuestion,
            {}
        );
        await fetch(request);
        $("#toggle-preview").html("");
        $("#" + parentID).data("toggle_current", selectedQuestion);
        $("#" + parentID).data("toggle_current_type", toggleQuestionTypes[toggleQuestionSelect.selectedIndex]);
    }

    // on clicking "Transfer" button, extract the current text and indentation of the Parsons blocks in the answer space, then paste that into the selected active code question
    async toggleTransfer(parentID, selectedQuestion, htmlsrc, toggleQuestionTypes) {
        // retrieve all Parsons lines within the answer space and loop through this list
        var currentParsons = document.getElementById(parentID + "-toggleSelectedQuestion").querySelectorAll("div[class^='answer']")[0].getElementsByClassName("prettyprint lang-py");
        var currentParsonsClass;
        var currentBlockIndent;
        var indentCount
        var indent;
        var parsonsLine;
        var parsonsLines = ``;
        var count;
        for (var p = 0; p < currentParsons.length; p++) {
            indentCount = 0;
            indent = "";
            // for Parsons blocks that have built-in indentation in their lines
            currentParsonsClass = currentParsons[p].classList[2];
            if (currentParsonsClass) {
                if (currentParsonsClass.includes("indent")) {
                    indentCount = parseInt(indentCount) + parseInt(currentParsonsClass.slice(6,currentParsonsClass.length));
                }
            }
            // for Parsons answer spaces with vertical lines that allow student to define their own line indentation
            currentBlockIndent = currentParsons[p].parentElement.parentElement.style.left;
            if (currentBlockIndent) {
                indentCount = parseInt(indentCount) + parseInt(currentBlockIndent.slice(0,currentBlockIndent.indexOf("px")) / 30);
            }
            for (var d = 0; d < indentCount; d++) {
                indent += "    ";
            }
            // retrieve each text snippet of each Parsons line and loop through this list
            parsonsLine = currentParsons[p].getElementsByTagName("span");
            count = 0;
            for (var l = 0; l < parsonsLine.length; l++) {
                if (parsonsLine[l].childNodes[0].nodeName == "#text") { // Parsons blocks have differing amounts of hierarchy levels (spans within spans)
                    if ((p == 0) && (count == 0)) { // need different check than l == 0 because the l numbering doesn't align with location within line due to inconsistent span heirarchy
                        parsonsLines += indent + parsonsLine[l].innerHTML;
                        count++;
                    }
                    else if (count != 0) {
                        parsonsLines += parsonsLine[l].innerHTML;
                        count++;
                    }
                    else {
                        parsonsLines = parsonsLines + `
                            ` + indent + parsonsLine[l].innerHTML;
                        parsonsLines = parsonsLines.replace("                            ", "");
                        count++;
                    }
                }
            }
        }
        // replace all existing code within selected active code question with extracted Parsons text
        var htmlsrcFormer = htmlsrc.slice(0, htmlsrc.indexOf("<textarea") + htmlsrc.split("<textarea")[1].indexOf(">") + 10);
        var htmlsrcLatter = htmlsrc.slice(htmlsrc.indexOf("</textarea>"), htmlsrc.length);
        htmlsrc = htmlsrcFormer + parsonsLines + htmlsrcLatter;

        await this.toggleSet(parentID, selectedQuestion, htmlsrc, toggleQuestionTypes);
        $("#component-preview").hide();
    }
}

/*
 * When the page is loaded and the login checks are complete find and render
 * each selectquestion component that is not part of a timedAssessment.
 **/
$(document).bind("runestone:login-complete", async function () {
    let selQuestions = document.querySelectorAll(
        "[data-component=selectquestion]"
    );
    for (let cq of selQuestions) {
        try {
            if ($(cq).closest("[data-component=timedAssessment]").length == 0) {
                // If this element exists within a timed component, don't render it here
                let tmp = new SelectOne({ orig: cq });
                await tmp.initialize();
            }
        } catch (err) {
            console.log(`Error rendering New Exercise ${cq.id}
                         Details: ${err}`);
            console.log(err.stack);
        }
    }
});


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9XZWJDb21wb25lbnRzLy4vcnVuZXN0b25lL3NlbGVjdHF1ZXN0aW9uL2Nzcy9zZWxlY3RxdWVzdGlvbi5jc3MiLCJ3ZWJwYWNrOi8vV2ViQ29tcG9uZW50cy8uL3J1bmVzdG9uZS9zZWxlY3RxdWVzdGlvbi9jc3Mvc2VsZWN0cXVlc3Rpb24uY3NzP2Q4MmYiLCJ3ZWJwYWNrOi8vV2ViQ29tcG9uZW50cy8uL3J1bmVzdG9uZS9jb21tb24vanMvcmVuZGVyQ29tcG9uZW50LmpzIiwid2VicGFjazovL1dlYkNvbXBvbmVudHMvLi9ydW5lc3RvbmUvc2VsZWN0cXVlc3Rpb24vanMvc2VsZWN0b25lLmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7QUFDNEg7QUFDN0I7QUFDL0YsOEJBQThCLG1GQUEyQixDQUFDLHdHQUFxQztBQUMvRjtBQUNBLDJEQUEyRCx3QkFBd0IsMEJBQTBCLDhCQUE4Qix3QkFBd0Isb0NBQW9DLEdBQUcsU0FBUyxrSEFBa0gsWUFBWSxhQUFhLGFBQWEsYUFBYSxhQUFhLDJDQUEyQyx3QkFBd0IsMEJBQTBCLDhCQUE4Qix3QkFBd0Isb0NBQW9DLEdBQUcscUJBQXFCO0FBQ3BsQjtBQUNBLGlFQUFlLHVCQUF1QixFQUFDOzs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDUHdEO0FBQy9GLFlBQXNHOztBQUV0Rzs7QUFFQTtBQUNBOztBQUVBLGFBQWEsMEdBQUcsQ0FBQyw0RkFBTzs7OztBQUl4QixpRUFBZSxtR0FBYyxNQUFNLEU7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDWjBCOztBQUV0RDtBQUNQO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxXQUFXLGdCQUFnQixtQkFBbUIsdUJBQXVCO0FBQ3JFO0FBQ0EsZUFBZSxTQUFTOztBQUV4QjtBQUNBO0FBQ0E7O0FBRUEsZ0NBQWdDLFNBQVM7QUFDekM7QUFDQTtBQUNBO0FBQ0EsVUFBVSxtRUFBZ0I7QUFDMUI7QUFDQSwwQkFB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QUNBO0FBQ0E7QUFDQTtBQUNBLDJCQUEyQixpQkFBaUI7QUFDNUM7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDJCQUEyQix3QkFBd0I7QUFDbkQsdUVBQXVFO0FBQ3ZFLG1EQUFtRDtBQUNuRDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLHlDQUF5QyxXQUFXO0FBQ3BEO0FBQ0E7QUFDQSxTQUFTO0FBQ1Qsd0RBQXdEO0FBQ3hELG9DQUFvQyxJQUFJO0FBQ3hDO0FBQ0E7QUFDQTtBQUNBLENBQUMiLCJmaWxlIjoicnVuZXN0b25lX3NlbGVjdHF1ZXN0aW9uX2pzX3NlbGVjdG9uZV9qcy5idW5kbGUuanM/dj02NjA0ZWI1Y2NiY2Q4OTdiZTA3NCIsInNvdXJjZXNDb250ZW50IjpbIi8vIEltcG9ydHNcbmltcG9ydCBfX19DU1NfTE9BREVSX0FQSV9TT1VSQ0VNQVBfSU1QT1JUX19fIGZyb20gXCIuLi8uLi8uLi9ub2RlX21vZHVsZXMvY3NzLWxvYWRlci9kaXN0L3J1bnRpbWUvY3NzV2l0aE1hcHBpbmdUb1N0cmluZy5qc1wiO1xuaW1wb3J0IF9fX0NTU19MT0FERVJfQVBJX0lNUE9SVF9fXyBmcm9tIFwiLi4vLi4vLi4vbm9kZV9tb2R1bGVzL2Nzcy1sb2FkZXIvZGlzdC9ydW50aW1lL2FwaS5qc1wiO1xudmFyIF9fX0NTU19MT0FERVJfRVhQT1JUX19fID0gX19fQ1NTX0xPQURFUl9BUElfSU1QT1JUX19fKF9fX0NTU19MT0FERVJfQVBJX1NPVVJDRU1BUF9JTVBPUlRfX18pO1xuLy8gTW9kdWxlXG5fX19DU1NfTE9BREVSX0VYUE9SVF9fXy5wdXNoKFttb2R1bGUuaWQsIFwiLnRvZ2dsZS1wcmV2aWV3IHtcXG4gICAgYm9yZGVyOiA0cHggc29saWQ7XFxuICAgIGJvcmRlci1yYWRpdXM6IDEwcHg7XFxuICAgIGJhY2tncm91bmQtY29sb3I6IGF6dXJlO1xcbiAgICBwYWRkaW5nLXRvcDogMTBweDtcXG4gICAgYm94LXNoYWRvdzogMTBweCA1cHggNXB4IGdyYXk7XFxufVxcblwiLCBcIlwiLHtcInZlcnNpb25cIjozLFwic291cmNlc1wiOltcIndlYnBhY2s6Ly8uL3J1bmVzdG9uZS9zZWxlY3RxdWVzdGlvbi9jc3Mvc2VsZWN0cXVlc3Rpb24uY3NzXCJdLFwibmFtZXNcIjpbXSxcIm1hcHBpbmdzXCI6XCJBQUFBO0lBQ0ksaUJBQWlCO0lBQ2pCLG1CQUFtQjtJQUNuQix1QkFBdUI7SUFDdkIsaUJBQWlCO0lBQ2pCLDZCQUE2QjtBQUNqQ1wiLFwic291cmNlc0NvbnRlbnRcIjpbXCIudG9nZ2xlLXByZXZpZXcge1xcbiAgICBib3JkZXI6IDRweCBzb2xpZDtcXG4gICAgYm9yZGVyLXJhZGl1czogMTBweDtcXG4gICAgYmFja2dyb3VuZC1jb2xvcjogYXp1cmU7XFxuICAgIHBhZGRpbmctdG9wOiAxMHB4O1xcbiAgICBib3gtc2hhZG93OiAxMHB4IDVweCA1cHggZ3JheTtcXG59XFxuXCJdLFwic291cmNlUm9vdFwiOlwiXCJ9XSk7XG4vLyBFeHBvcnRzXG5leHBvcnQgZGVmYXVsdCBfX19DU1NfTE9BREVSX0VYUE9SVF9fXztcbiIsImltcG9ydCBhcGkgZnJvbSBcIiEuLi8uLi8uLi9ub2RlX21vZHVsZXMvc3R5bGUtbG9hZGVyL2Rpc3QvcnVudGltZS9pbmplY3RTdHlsZXNJbnRvU3R5bGVUYWcuanNcIjtcbiAgICAgICAgICAgIGltcG9ydCBjb250ZW50IGZyb20gXCIhIS4uLy4uLy4uL25vZGVfbW9kdWxlcy9jc3MtbG9hZGVyL2Rpc3QvY2pzLmpzIS4vc2VsZWN0cXVlc3Rpb24uY3NzXCI7XG5cbnZhciBvcHRpb25zID0ge307XG5cbm9wdGlvbnMuaW5zZXJ0ID0gXCJoZWFkXCI7XG5vcHRpb25zLnNpbmdsZXRvbiA9IGZhbHNlO1xuXG52YXIgdXBkYXRlID0gYXBpKGNvbnRlbnQsIG9wdGlvbnMpO1xuXG5cblxuZXhwb3J0IGRlZmF1bHQgY29udGVudC5sb2NhbHMgfHwge307IiwiaW1wb3J0IHsgcnVuZXN0b25lX2ltcG9ydCB9IGZyb20gXCIuLi8uLi8uLi93ZWJwYWNrLmluZGV4LmpzXCI7XG5cbmV4cG9ydCBhc3luYyBmdW5jdGlvbiByZW5kZXJSdW5lc3RvbmVDb21wb25lbnQoY29tcG9uZW50U3JjLCB3aGVyZURpdiwgbW9yZU9wdHMpIHtcbiAgICAvKipcbiAgICAgKiAgVGhlIGVhc3kgcGFydCBpcyBhZGRpbmcgdGhlIGNvbXBvbmVudFNyYyB0byB0aGUgZXhpc3RpbmcgZGl2LlxuICAgICAqICBUaGUgdGVkaW91cyBwYXJ0IGlzIGNhbGxpbmcgdGhlIHJpZ2h0IGZ1bmN0aW9ucyB0byB0dXJuIHRoZVxuICAgICAqICBzb3VyY2UgaW50byB0aGUgYWN0dWFsIGNvbXBvbmVudC5cbiAgICAgKi9cbiAgICBsZXQgcGF0dCA9IC8uLlxcL19pbWFnZXMvZztcbiAgICBjb21wb25lbnRTcmMgPSBjb21wb25lbnRTcmMucmVwbGFjZShcbiAgICAgICAgcGF0dCxcbiAgICAgICAgYCR7ZUJvb2tDb25maWcuYXBwfS9ib29rcy9wdWJsaXNoZWQvJHtlQm9va0NvbmZpZy5iYXNlY291cnNlfS9faW1hZ2VzYFxuICAgICk7XG4gICAgalF1ZXJ5KGAjJHt3aGVyZURpdn1gKS5odG1sKGNvbXBvbmVudFNyYyk7XG5cbiAgICBpZiAodHlwZW9mIHdpbmRvdy5lZExpc3QgPT09IFwidW5kZWZpbmVkXCIpIHtcbiAgICAgICAgd2luZG93LmVkTGlzdCA9IHt9O1xuICAgIH1cblxuICAgIGxldCBjb21wb25lbnRLaW5kID0gJCgkKGAjJHt3aGVyZURpdn0gW2RhdGEtY29tcG9uZW50XWApWzBdKS5kYXRhKFxuICAgICAgICBcImNvbXBvbmVudFwiXG4gICAgKTtcbiAgICAvLyBJbXBvcnQgdGhlIEphdmFTY3JpcHQgZm9yIHRoaXMgY29tcG9uZW50IGJlZm9yZSBwcm9jZWVkaW5nLlxuICAgIGF3YWl0IHJ1bmVzdG9uZV9pbXBvcnQoY29tcG9uZW50S2luZCk7XG4gICAgbGV0IG9wdCA9IHt9O1xuICAgIG9wdC5vcmlnID0galF1ZXJ5KGAjJHt3aGVyZURpdn0gW2RhdGEtY29tcG9uZW50XWApWzBdO1xuICAgIGlmIChvcHQub3JpZykge1xuICAgICAgICBvcHQubGFuZyA9ICQob3B0Lm9yaWcpLmRhdGEoXCJsYW5nXCIpO1xuICAgICAgICBvcHQudXNlUnVuZXN0b25lU2VydmljZXMgPSB0cnVlO1xuICAgICAgICBvcHQuZ3JhZGVyYWN0aXZlID0gZmFsc2U7XG4gICAgICAgIG9wdC5weXRob24zID0gdHJ1ZTtcbiAgICAgICAgaWYgKHR5cGVvZiBtb3JlT3B0cyAhPT0gXCJ1bmRlZmluZWRcIikge1xuICAgICAgICAgICAgZm9yIChsZXQga2V5IGluIG1vcmVPcHRzKSB7XG4gICAgICAgICAgICAgICAgb3B0W2tleV0gPSBtb3JlT3B0c1trZXldO1xuICAgICAgICAgICAgfVxuICAgICAgICB9XG4gICAgfVxuXG4gICAgaWYgKHR5cGVvZiBjb21wb25lbnRfZmFjdG9yeSA9PT0gXCJ1bmRlZmluZWRcIikge1xuICAgICAgICBhbGVydChcbiAgICAgICAgICAgIFwiRXJyb3I6ICBNaXNzaW5nIHRoZSBjb21wb25lbnQgZmFjdG9yeSEgIENsZWFyIHlvdSBicm93c2VyIGNhY2hlLlwiXG4gICAgICAgICk7XG4gICAgfSBlbHNlIHtcbiAgICAgICAgaWYgKFxuICAgICAgICAgICAgIXdpbmRvdy5jb21wb25lbnRfZmFjdG9yeVtjb21wb25lbnRLaW5kXSAmJlxuICAgICAgICAgICAgIWpRdWVyeShgIyR7d2hlcmVEaXZ9YCkuaHRtbCgpXG4gICAgICAgICkge1xuICAgICAgICAgICAgalF1ZXJ5KGAjJHt3aGVyZURpdn1gKS5odG1sKFxuICAgICAgICAgICAgICAgIGA8cD5QcmV2aWV3IG5vdCBhdmFpbGFibGUgZm9yICR7Y29tcG9uZW50S2luZH08L3A+YFxuICAgICAgICAgICAgKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIGxldCByZXMgPSB3aW5kb3cuY29tcG9uZW50X2ZhY3RvcnlbY29tcG9uZW50S2luZF0ob3B0KTtcbiAgICAgICAgICAgIGlmIChjb21wb25lbnRLaW5kID09PSBcImFjdGl2ZWNvZGVcIikge1xuICAgICAgICAgICAgICAgIGlmIChtb3JlT3B0cy5tdWx0aUdyYWRlcikge1xuICAgICAgICAgICAgICAgICAgICB3aW5kb3cuZWRMaXN0W1xuICAgICAgICAgICAgICAgICAgICAgICAgYCR7bW9yZU9wdHMuZ3JhZGluZ0NvbnRhaW5lcn0gJHtyZXMuZGl2aWR9YFxuICAgICAgICAgICAgICAgICAgICBdID0gcmVzO1xuICAgICAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgICAgIHdpbmRvdy5lZExpc3RbcmVzLmRpdmlkXSA9IHJlcztcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9XG59XG5cbmV4cG9ydCBmdW5jdGlvbiBjcmVhdGVUaW1lZENvbXBvbmVudChjb21wb25lbnRTcmMsIG1vcmVPcHRzKSB7XG4gICAgLyogVGhlIGltcG9ydGFudCBkaXN0aW5jdGlvbiBpcyB0aGF0IHRoZSBjb21wb25lbnQgZG9lcyBub3QgcmVhbGx5IG5lZWQgdG8gYmUgcmVuZGVyZWRcbiAgICBpbnRvIHRoZSBwYWdlLCBpbiBmYWN0LCBkdWUgdG8gdGhlIGFzeW5jIG5hdHVyZSBvZiBnZXR0aW5nIHRoZSBzb3VyY2UgdGhlIGxpc3Qgb2YgcXVlc3Rpb25zXG4gICAgaXMgbWFkZSBhbmQgdGhlIG9yaWdpbmFsIGh0bWwgaXMgcmVwbGFjZWQgYnkgdGhlIGxvb2sgb2YgdGhlIGV4YW0uXG4gICAgKi9cblxuICAgIGxldCBwYXR0ID0gLy4uXFwvX2ltYWdlcy9nO1xuICAgIGNvbXBvbmVudFNyYyA9IGNvbXBvbmVudFNyYy5yZXBsYWNlKFxuICAgICAgICBwYXR0LFxuICAgICAgICBgJHtlQm9va0NvbmZpZy5hcHB9L2Jvb2tzL3B1Ymxpc2hlZC8ke2VCb29rQ29uZmlnLmJhc2Vjb3Vyc2V9L19pbWFnZXNgXG4gICAgKTtcblxuICAgIGxldCBjb21wb25lbnRLaW5kID0gJCgkKGNvbXBvbmVudFNyYykuZmluZChcIltkYXRhLWNvbXBvbmVudF1cIilbMF0pLmRhdGEoXG4gICAgICAgIFwiY29tcG9uZW50XCJcbiAgICApO1xuXG4gICAgbGV0IG9yaWdJZCA9ICQoY29tcG9uZW50U3JjKS5maW5kKFwiW2RhdGEtY29tcG9uZW50XVwiKS5maXJzdCgpLmF0dHIoXCJpZFwiKTtcblxuICAgIC8vIERvdWJsZSBjaGVjayAtLSBpZiB0aGUgY29tcG9uZW50IHNvdXJjZSBpcyBub3QgaW4gdGhlIERPTSwgdGhlbiBicmllZmx5IGFkZCBpdFxuICAgIC8vIGFuZCBjYWxsIHRoZSBjb25zdHJ1Y3Rvci5cbiAgICBsZXQgaGRpdjtcbiAgICBpZiAoIWRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG9yaWdJZCkpIHtcbiAgICAgICAgaGRpdiA9ICQoXCI8ZGl2Lz5cIiwge1xuICAgICAgICAgICAgY3NzOiB7IGRpc3BsYXk6IFwibm9uZVwiIH0sXG4gICAgICAgIH0pLmFwcGVuZFRvKFwiYm9keVwiKTtcbiAgICAgICAgaGRpdi5odG1sKGNvbXBvbmVudFNyYyk7XG4gICAgfVxuICAgIC8vIGF0IHRoaXMgcG9pbnQgaGRpdiBpcyBhIGpxdWVyeSBvYmplY3RcblxuICAgIGxldCByZXQ7XG4gICAgbGV0IG9wdHMgPSB7XG4gICAgICAgIG9yaWc6IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG9yaWdJZCksXG4gICAgICAgIHRpbWVkOiB0cnVlLFxuICAgIH07XG4gICAgaWYgKHR5cGVvZiBtb3JlT3B0cyAhPT0gXCJ1bmRlZmluZWRcIikge1xuICAgICAgICBmb3IgKGxldCBrZXkgaW4gbW9yZU9wdHMpIHtcbiAgICAgICAgICAgIG9wdHNba2V5XSA9IG1vcmVPcHRzW2tleV07XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBpZiAoY29tcG9uZW50S2luZCBpbiB3aW5kb3cuY29tcG9uZW50X2ZhY3RvcnkpIHtcbiAgICAgICAgcmV0ID0gd2luZG93LmNvbXBvbmVudF9mYWN0b3J5W2NvbXBvbmVudEtpbmRdKG9wdHMpO1xuICAgIH1cblxuICAgIGxldCByZGljdCA9IHt9O1xuICAgIHJkaWN0LnF1ZXN0aW9uID0gcmV0O1xuICAgIHJldHVybiByZGljdDtcbn1cbiIsIi8qKlxuICogKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKlxuICogfGRvY25hbWV8IC0gU2VsZWN0T25lIENvbXBvbmVudFxuICogKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKlxuICovXG5pbXBvcnQge1xuICAgIHJlbmRlclJ1bmVzdG9uZUNvbXBvbmVudCxcbiAgICBjcmVhdGVUaW1lZENvbXBvbmVudCxcbn0gZnJvbSBcIi4uLy4uL2NvbW1vbi9qcy9yZW5kZXJDb21wb25lbnQuanNcIjtcbmltcG9ydCBSdW5lc3RvbmVCYXNlIGZyb20gXCIuLi8uLi9jb21tb24vanMvcnVuZXN0b25lYmFzZS5qc1wiO1xuaW1wb3J0IFwiLi4vY3NzL3NlbGVjdHF1ZXN0aW9uLmNzc1wiO1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBTZWxlY3RPbmUgZXh0ZW5kcyBSdW5lc3RvbmVCYXNlIHtcbiAgICAvKipcbiAgICAgKiBjb25zdHJ1Y3RvciAtLVxuICAgICAqIE1ha2luZyBhbiBpbnN0YW5jZSBvZiBhIHNlbGVjdG9uZSBpcyBhIGJpdCBtb3JlIGNvbXBsaWNhdGVkIGJlY2F1c2UgaXQgaXNcbiAgICAgKiBhIGtpbmQgb2YgbWV0YSBkaXJlY3RpdmUuICBUaGF0IGlzLCBnbyB0byB0aGUgc2VydmVyIGFuZCByYW5kb21seSBzZWxlY3RcbiAgICAgKiBhIHF1ZXN0aW9uIHRvIGRpc3BsYXkgaW4gdGhpcyBzcG90LiAgT3IsIGlmIGEgc3R1ZGVudCBoYXMgYWxyZWFkeSBzZWVuIHRoaXMgcXVlc3Rpb25cbiAgICAgKiBpbiB0aGUgY29udGV4dCBvZiBhbiBleGFtIHJldHJpZXZlIHRoZSBxdWVzdGlvbiB0aGV5IHNhdyBpbiB0aGUgZmlyc3QgcGxhY2UuXG4gICAgICogTWFraW5nIGFuIEFQSSBjYWxsIGFuZCB3YWl0aW5nIGZvciB0aGUgcmVzcG9uc2UgaXMgaGFuZGxlZCBhc3luY2hyb25vdXNseS5cbiAgICAgKiBCdXQgbG90cyBvZiBjb2RlIGlzIG5vdCB3cml0dGVuIHdpdGggdGhhdCBhc3N1bXB0aW9uLiAgU28gd2UgZG8gdGhlIGluaXRpYWxpemF0aW9uIGluXG4gICAgICogdHdvIHBhcnRzLlxuICAgICAqIDEuIENyZWF0ZSB0aGUgb2JqZWN0IHdpdGggdGhlIHVzdWFsIGNvbnN0cnVjdG9yXG4gICAgICogMi4gY2FsbCBpbml0aWFsaXplLCB3aGljaCByZXR1cm5zIGEgcHJvbWlzZS4gIFdoZW4gdGhhdCBwcm9taXNlIGlzIHJlc29sdmVkXG4gICAgICogdGhlIFwicmVwbGFjZW1lbnRcIiBjb21wb25lbnQgd2lsbCByZXBsYWNlIHRoZSBvcmlnaW5hbCBzZWxlY3RvbmUgY29tcG9uZW50IGluIHRoZSBET00uXG4gICAgICpcbiAgICAgKiBAcGFyYW0gIHt9IG9wdHNcbiAgICAgKi9cbiAgICBjb25zdHJ1Y3RvcihvcHRzKSB7XG4gICAgICAgIHN1cGVyKG9wdHMpO1xuICAgICAgICB0aGlzLm9yaWdPcHRzID0gb3B0cztcbiAgICAgICAgdGhpcy5xdWVzdGlvbnMgPSAkKG9wdHMub3JpZykuZGF0YShcInF1ZXN0aW9ubGlzdFwiKTtcbiAgICAgICAgdGhpcy5wcm9maWNpZW5jeSA9ICQob3B0cy5vcmlnKS5kYXRhKFwicHJvZmljaWVuY3lcIik7XG4gICAgICAgIHRoaXMubWluRGlmZmljdWx0eSA9ICQob3B0cy5vcmlnKS5kYXRhKFwibWluRGlmZmljdWx0eVwiKTtcbiAgICAgICAgdGhpcy5tYXhEaWZmaWN1bHR5ID0gJChvcHRzLm9yaWcpLmRhdGEoXCJtYXhEaWZmaWN1bHR5XCIpO1xuICAgICAgICB0aGlzLnBvaW50cyA9ICQob3B0cy5vcmlnKS5kYXRhKFwicG9pbnRzXCIpO1xuICAgICAgICB0aGlzLmF1dG9ncmFkYWJsZSA9ICQob3B0cy5vcmlnKS5kYXRhKFwiYXV0b2dyYWRhYmxlXCIpO1xuICAgICAgICB0aGlzLm5vdF9zZWVuX2V2ZXIgPSAkKG9wdHMub3JpZykuZGF0YShcIm5vdF9zZWVuX2V2ZXJcIik7XG4gICAgICAgIHRoaXMuc2VsZWN0b3JfaWQgPSAkKG9wdHMub3JpZykuZmlyc3QoKS5hdHRyKFwiaWRcIik7XG4gICAgICAgIHRoaXMucHJpbWFyeU9ubHkgPSAkKG9wdHMub3JpZykuZGF0YShcInByaW1hcnlcIik7XG4gICAgICAgIHRoaXMuQUJFeHBlcmltZW50ID0gJChvcHRzLm9yaWcpLmRhdGEoXCJhYlwiKTtcbiAgICAgICAgdGhpcy50b2dnbGVPcHRpb25zID0gJChvcHRzLm9yaWcpLmRhdGEoXCJ0b2dnbGVvcHRpb25zXCIpO1xuICAgICAgICB0aGlzLnRvZ2dsZUxhYmVscyA9ICQob3B0cy5vcmlnKS5kYXRhKFwidG9nZ2xlbGFiZWxzXCIpO1xuICAgICAgICBvcHRzLm9yaWcuaWQgPSB0aGlzLnNlbGVjdG9yX2lkO1xuICAgIH1cbiAgICAvKipcbiAgICAgKiBpbml0aWFsaXplIC0tXG4gICAgICogaW5pdGlhbGl6ZSBpcyB1c2VkIHNvIHRoYXQgdGhlIGNvbnN0cnVjdG9yIGRvZXMgbm90IGhhdmUgdG8gYmUgYXN5bmMuXG4gICAgICogQ29uc3RydWN0b3JzIHNob3VsZCBkZWZpbml0ZWx5IG5vdCByZXR1cm4gcHJvbWlzZXMgdGhhdCB3b3VsZCBzZXJpb3VzbHlcbiAgICAgKiBtZXNzIHRoaW5ncyB1cC5cbiAgICAgKiBAcmV0dXJuIHtQcm9taXNlfSBXaWxsIHJlc29sdmUgYWZ0ZXIgY29tcG9uZW50IGZyb20gREIgaXMgcmVpZmllZFxuICAgICAqL1xuICAgIGFzeW5jIGluaXRpYWxpemUoKSB7XG4gICAgICAgIGxldCBzZWxmID0gdGhpcztcbiAgICAgICAgbGV0IGRhdGEgPSB7IHNlbGVjdG9yX2lkOiB0aGlzLnNlbGVjdG9yX2lkIH07XG4gICAgICAgIGlmICh0aGlzLnF1ZXN0aW9ucykge1xuICAgICAgICAgICAgZGF0YS5xdWVzdGlvbnMgPSB0aGlzLnF1ZXN0aW9ucztcbiAgICAgICAgfSBlbHNlIGlmICh0aGlzLnByb2ZpY2llbmN5KSB7XG4gICAgICAgICAgICBkYXRhLnByb2ZpY2llbmN5ID0gdGhpcy5wcm9maWNpZW5jeTtcbiAgICAgICAgfVxuICAgICAgICBpZiAodGhpcy5taW5EaWZmaWN1bHR5KSB7XG4gICAgICAgICAgICBkYXRhLm1pbkRpZmZpY3VsdHkgPSB0aGlzLm1pbkRpZmZpY3VsdHk7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKHRoaXMubWF4RGlmZmljdWx0eSkge1xuICAgICAgICAgICAgZGF0YS5tYXhEaWZmaWN1bHR5ID0gdGhpcy5tYXhEaWZmaWN1bHR5O1xuICAgICAgICB9XG4gICAgICAgIGlmICh0aGlzLnBvaW50cykge1xuICAgICAgICAgICAgZGF0YS5wb2ludHMgPSB0aGlzLnBvaW50cztcbiAgICAgICAgfVxuICAgICAgICBpZiAodGhpcy5hdXRvZ3JhZGFibGUpIHtcbiAgICAgICAgICAgIGRhdGEuYXV0b2dyYWRhYmxlID0gdGhpcy5hdXRvZ3JhZGFibGU7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKHRoaXMubm90X3NlZW5fZXZlcikge1xuICAgICAgICAgICAgZGF0YS5ub3Rfc2Vlbl9ldmVyID0gdGhpcy5ub3Rfc2Vlbl9ldmVyO1xuICAgICAgICB9XG4gICAgICAgIGlmICh0aGlzLnByaW1hcnlPbmx5KSB7XG4gICAgICAgICAgICBkYXRhLnByaW1hcnkgPSB0aGlzLnByaW1hcnlPbmx5O1xuICAgICAgICB9XG4gICAgICAgIGlmICh0aGlzLkFCRXhwZXJpbWVudCkge1xuICAgICAgICAgICAgZGF0YS5BQiA9IHRoaXMuQUJFeHBlcmltZW50O1xuICAgICAgICB9XG4gICAgICAgIGlmICh0aGlzLnRpbWVkV3JhcHBlcikge1xuICAgICAgICAgICAgZGF0YS50aW1lZFdyYXBwZXIgPSB0aGlzLnRpbWVkV3JhcHBlcjtcbiAgICAgICAgfVxuICAgICAgICBpZiAodGhpcy50b2dnbGVPcHRpb25zKSB7XG4gICAgICAgICAgICBkYXRhLnRvZ2dsZU9wdGlvbnMgPSB0aGlzLnRvZ2dsZU9wdGlvbnM7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKHRoaXMudG9nZ2xlTGFiZWxzKSB7XG4gICAgICAgICAgICBkYXRhLnRvZ2dsZUxhYmVscyA9IHRoaXMudG9nZ2xlTGFiZWxzO1xuICAgICAgICB9XG4gICAgICAgIGxldCBvcHRzID0gdGhpcy5vcmlnT3B0cztcbiAgICAgICAgbGV0IHNlbGVjdG9ySWQgPSB0aGlzLnNlbGVjdG9yX2lkO1xuICAgICAgICBjb25zb2xlLmxvZyhcImdldHRpbmcgcXVlc3Rpb24gc291cmNlXCIpO1xuICAgICAgICBsZXQgcmVxdWVzdCA9IG5ldyBSZXF1ZXN0KFwiL3J1bmVzdG9uZS9hamF4L2dldF9xdWVzdGlvbl9zb3VyY2VcIiwge1xuICAgICAgICAgICAgbWV0aG9kOiBcIlBPU1RcIixcbiAgICAgICAgICAgIGhlYWRlcnM6IHRoaXMuanNvbkhlYWRlcnMsXG4gICAgICAgICAgICBib2R5OiBKU09OLnN0cmluZ2lmeShkYXRhKSxcbiAgICAgICAgfSk7XG4gICAgICAgIGxldCByZXNwb25zZSA9IGF3YWl0IGZldGNoKHJlcXVlc3QpO1xuICAgICAgICBsZXQgaHRtbHNyYyA9IGF3YWl0IHJlc3BvbnNlLmpzb24oKTtcbiAgICAgICAgaWYgKGh0bWxzcmMuaW5kZXhPZihcIk5vIHByZXZpZXdcIikgPj0gMCkge1xuICAgICAgICAgICAgYWxlcnQoXG4gICAgICAgICAgICAgICAgYEVycm9yOiBOb3QgYWJsZSB0byBmaW5kIGEgcXVlc3Rpb24gZm9yICR7c2VsZWN0b3JJZH0gYmFzZWQgb24gdGhlIGNyaXRlcmlhYFxuICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcihgVW5hYmxlIHRvIGZpbmQgYSBxdWVzdGlvbiBmb3IgJHtzZWxlY3RvcklkfWApO1xuICAgICAgICB9XG4gICAgICAgIGxldCByZXM7XG4gICAgICAgIGlmIChvcHRzLnRpbWVkKSB7XG4gICAgICAgICAgICAvLyB0aW1lZCBjb21wb25lbnRzIGFyZSBub3QgcmVuZGVyZWQgaW1tZWRpYXRlbHksIG9ubHkgd2hlbiB0aGUgc3R1ZGVudFxuICAgICAgICAgICAgLy8gc3RhcnRzIHRoZSBhc3Nlc3NtZW50IGFuZCB2aXNpdHMgdGhpcyBwYXJ0aWN1bGFyIGVudHJ5LlxuICAgICAgICAgICAgcmVzID0gY3JlYXRlVGltZWRDb21wb25lbnQoaHRtbHNyYywge1xuICAgICAgICAgICAgICAgIHRpbWVkOiB0cnVlLFxuICAgICAgICAgICAgICAgIHNlbGVjdG9yX2lkOiBzZWxlY3RvcklkLFxuICAgICAgICAgICAgICAgIGFzc2Vzc21lbnRUYWtlbjogb3B0cy5hc3Nlc3NtZW50VGFrZW4sXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIC8vIHJlcGxhY2UgdGhlIGVudHJ5IGluIHRoZSB0aW1lZCBhc3Nlc3NtZW50J3MgbGlzdCBvZiBjb21wb25lbnRzXG4gICAgICAgICAgICAvLyB3aXRoIHRoZSBjb21wb25lbnQgY3JlYXRlZCBieSBjcmVhdGVUaW1lZENvbXBvbmVudFxuICAgICAgICAgICAgZm9yIChsZXQgY29tcG9uZW50IG9mIG9wdHMucnFhKSB7XG4gICAgICAgICAgICAgICAgaWYgKGNvbXBvbmVudC5xdWVzdGlvbiA9PSBzZWxmKSB7XG4gICAgICAgICAgICAgICAgICAgIGNvbXBvbmVudC5xdWVzdGlvbiA9IHJlcy5xdWVzdGlvbjtcbiAgICAgICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICAgICAgc2VsZi5yZWFsQ29tcG9uZW50ID0gcmVzLnF1ZXN0aW9uO1xuICAgICAgICAgICAgc2VsZi5jb250YWluZXJEaXYgPSByZXMucXVlc3Rpb24uY29udGFpbmVyRGl2O1xuICAgICAgICAgICAgc2VsZi5yZWFsQ29tcG9uZW50LnNlbGVjdG9ySWQgPSBzZWxlY3RvcklkO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgaWYgKGRhdGEudG9nZ2xlT3B0aW9ucykge1xuICAgICAgICAgICAgICAgIHZhciB0b2dnbGVMYWJlbHMgPSBkYXRhLnRvZ2dsZUxhYmVscy5yZXBsYWNlKFwidG9nZ2xlbGFiZWxzOlwiLCBcIlwiKS50cmltKCk7XG4gICAgICAgICAgICAgICAgaWYgKHRvZ2dsZUxhYmVscykge1xuICAgICAgICAgICAgICAgICAgICB0b2dnbGVMYWJlbHMgPSB0b2dnbGVMYWJlbHMuc3BsaXQoXCIsXCIpO1xuICAgICAgICAgICAgICAgICAgICBmb3IgKHZhciB0ID0gMDsgdCA8IHRvZ2dsZUxhYmVscy5sZW5ndGg7IHQrKykge1xuICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlTGFiZWxzW3RdID0gdG9nZ2xlTGFiZWxzW3RdLnRyaW0oKTtcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICB2YXIgdG9nZ2xlUXVlc3Rpb25zID0gdGhpcy5xdWVzdGlvbnMuc3BsaXQoXCIsIFwiKTtcbiAgICAgICAgICAgICAgICB2YXIgdG9nZ2xlVUkgPSBcIlwiO1xuICAgICAgICAgICAgICAgIC8vIGNoZWNrIHNvIHRoYXQgb25seSB0aGUgZmlyc3QgdG9nZ2xlIHNlbGVjdCBxdWVzdGlvbiBvbiB0aGUgYXNzaWdubWVudHMgcGFnZSBoYXMgYSBwcmV2aWV3IHBhbmVsIGNyZWF0ZWQsIHRoZW4gYWxsIHRvZ2dsZSBzZWxlY3QgcHJldmlld3MgdXNlIHRoaXMgc2FtZSBwYW5lbFxuICAgICAgICAgICAgICAgIGlmICghZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJjb21wb25lbnQtcHJldmlld1wiKSkge1xuICAgICAgICAgICAgICAgICAgICB0b2dnbGVVSSArPVxuICAgICAgICAgICAgICAgICAgICAgICAgJzxkaXYgaWQ9XCJjb21wb25lbnQtcHJldmlld1wiIGNsYXNzPVwiY29sLW1kLTYgdG9nZ2xlLXByZXZpZXdcIiBzdHlsZT1cInotaW5kZXg6IDk5OTtcIj4nICtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnPGRpdiBpZD1cInRvZ2dsZS1idXR0b25zXCI+PC9kaXY+JyArXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJzxkaXYgaWQ9XCJ0b2dnbGUtcHJldmlld1wiPjwvZGl2PicgK1xuICAgICAgICAgICAgICAgICAgICAgICAgJzwvZGl2Pic7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIC8vIGRyb3Bkb3duIG1lbnUgY29udGFpbmluZyB0aGUgcXVlc3Rpb24gb3B0aW9uc1xuICAgICAgICAgICAgICAgIHRvZ2dsZVVJICs9XG4gICAgICAgICAgICAgICAgICAgICc8bGFiZWwgZm9yPVwiJyArXG4gICAgICAgICAgICAgICAgICAgIHNlbGVjdG9ySWQgK1xuICAgICAgICAgICAgICAgICAgICAnLXRvZ2dsZVF1ZXN0aW9uXCIgc3R5bGU9XCJtYXJnaW4tbGVmdDogMTBweFwiPlRvZ2dsZSBRdWVzdGlvbjo8L2xhYmVsPjxzZWxlY3QgaWQ9XCInICtcbiAgICAgICAgICAgICAgICAgICAgc2VsZWN0b3JJZCArXG4gICAgICAgICAgICAgICAgICAgICctdG9nZ2xlUXVlc3Rpb25cIj4nO1xuICAgICAgICAgICAgICAgIHZhciBpO1xuICAgICAgICAgICAgICAgIHZhciB0b2dnbGVRdWVzdGlvbkhUTUxTcmM7XG4gICAgICAgICAgICAgICAgdmFyIHRvZ2dsZVF1ZXN0aW9uU3Vic3RyaW5nO1xuICAgICAgICAgICAgICAgIHZhciB0b2dnbGVRdWVzdGlvblR5cGU7XG4gICAgICAgICAgICAgICAgdmFyIHRvZ2dsZVF1ZXN0aW9uVHlwZXMgPSBbXTtcbiAgICAgICAgICAgICAgICBmb3IgKGkgPSAwOyBpIDwgdG9nZ2xlUXVlc3Rpb25zLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgICAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uSFRNTFNyYyA9IGF3YWl0IHRoaXMuZ2V0VG9nZ2xlU3JjKFxuICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25zW2ldXG4gICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uU3Vic3RyaW5nID0gdG9nZ2xlUXVlc3Rpb25IVE1MU3JjLnNwbGl0KFxuICAgICAgICAgICAgICAgICAgICAgICAgJ2RhdGEtY29tcG9uZW50PVwiJ1xuICAgICAgICAgICAgICAgICAgICApWzFdO1xuICAgICAgICAgICAgICAgICAgICBzd2l0Y2ggKFxuICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25TdWJzdHJpbmcuc2xpY2UoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgMCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblN1YnN0cmluZy5pbmRleE9mKCdcIicpXG4gICAgICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgICkge1xuICAgICAgICAgICAgICAgICAgICAgICAgY2FzZSBcImFjdGl2ZWNvZGVcIjpcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGUgPSBcIkFjdGl2ZSBXcml0ZSBDb2RlXCI7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICAgICAgICAgICAgICBjYXNlIFwiY2xpY2thYmxlYXJlYVwiOlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uVHlwZSA9IFwiQ2xpY2thYmxlIEFyZWFcIjtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgICAgICAgICAgICAgIGNhc2UgXCJkcmFnbmRyb3BcIjpcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGUgPSBcIkRyYWcgbiBEcm9wXCI7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICAgICAgICAgICAgICBjYXNlIFwiZmlsbGludGhlYmxhbmtcIjpcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGUgPSBcIkZpbGwgaW4gdGhlIEJsYW5rXCI7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICAgICAgICAgICAgICBjYXNlIFwibXVsdGlwbGVjaG9pY2VcIjpcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGUgPSBcIk11bHRpcGxlIENob2ljZVwiO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgICAgICAgICAgICAgY2FzZSBcInBhcnNvbnNcIjpcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGUgPSBcIlBhcnNvbnMgTWl4ZWQtVXAgQ29kZVwiO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgICAgICAgICAgICAgY2FzZSBcInNob3J0YW5zd2VyXCI6XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25UeXBlID0gXCJTaG9ydCBBbnN3ZXJcIjtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblR5cGVzW2ldID0gdG9nZ2xlUXVlc3Rpb25UeXBlO1xuICAgICAgICAgICAgICAgICAgICB0b2dnbGVVSSArPVxuICAgICAgICAgICAgICAgICAgICAgICAgJzxvcHRpb24gdmFsdWU9XCInICtcbiAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uc1tpXSArXG4gICAgICAgICAgICAgICAgICAgICAgICAnXCI+JztcbiAgICAgICAgICAgICAgICAgICAgaWYgKHRvZ2dsZUxhYmVscykge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHRvZ2dsZUxhYmVsc1tpXSkge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVVJICs9IHRvZ2dsZUxhYmVsc1tpXTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgICAgIGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVVJICs9IHRvZ2dsZVF1ZXN0aW9uVHlwZSArXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgXCIgLSBcIiArXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25zW2ldO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlVUkgKz0gdG9nZ2xlUXVlc3Rpb25UeXBlICtcbiAgICAgICAgICAgICAgICAgICAgICAgIFwiIC0gXCIgK1xuICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25zW2ldO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIGlmICgoaSA9PSAwKSAmJiAoZGF0YS50b2dnbGVPcHRpb25zLmluY2x1ZGVzKFwibG9ja1wiKSkpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVVJICs9IFwiIChvbmx5IHRoaXMgcXVlc3Rpb24gd2lsbCBiZSBncmFkZWQpXCI7XG4gICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgICAgdG9nZ2xlVUkgKz0gXCI8L29wdGlvbj5cIjtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgdG9nZ2xlVUkgKz1cbiAgICAgICAgICAgICAgICAgICAgJzwvc2VsZWN0PjxkaXYgaWQ9XCInICtcbiAgICAgICAgICAgICAgICAgICAgc2VsZWN0b3JJZCArXG4gICAgICAgICAgICAgICAgICAgICctdG9nZ2xlU2VsZWN0ZWRRdWVzdGlvblwiPic7XG4gICAgICAgICAgICAgICAgdmFyIHRvZ2dsZUZpcnN0SUQgPSBodG1sc3JjLnNwbGl0KCdpZD1cIicpWzFdO1xuICAgICAgICAgICAgICAgIHRvZ2dsZUZpcnN0SUQgPSB0b2dnbGVGaXJzdElELnNwbGl0KCdcIicpWzBdO1xuICAgICAgICAgICAgICAgIGh0bWxzcmMgPSB0b2dnbGVVSSArIGh0bWxzcmMgKyBcIjwvZGl2PlwiO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgLy8ganVzdCByZW5kZXIgdGhpcyBjb21wb25lbnQgb24gdGhlIHBhZ2UgaW4gaXRzIHVzdWFsIHBsYWNlXG4gICAgICAgICAgICBhd2FpdCByZW5kZXJSdW5lc3RvbmVDb21wb25lbnQoaHRtbHNyYywgc2VsZWN0b3JJZCwge1xuICAgICAgICAgICAgICAgIHNlbGVjdG9yX2lkOiBzZWxlY3RvcklkLFxuICAgICAgICAgICAgICAgIHVzZVJ1bmVzdG9uZVNlcnZpY2VzOiB0cnVlLFxuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICBpZiAoZGF0YS50b2dnbGVPcHRpb25zKSB7XG4gICAgICAgICAgICAgICAgJChcIiNjb21wb25lbnQtcHJldmlld1wiKS5oaWRlKCk7XG4gICAgICAgICAgICAgICAgdmFyIHRvZ2dsZVF1ZXN0aW9uU2VsZWN0ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXG4gICAgICAgICAgICAgICAgICAgIHNlbGVjdG9ySWQgKyBcIi10b2dnbGVRdWVzdGlvblwiXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICBmb3IgKGkgPSAwOyBpIDwgdG9nZ2xlUXVlc3Rpb25TZWxlY3Qub3B0aW9ucy5sZW5ndGg7IGkrKykge1xuICAgICAgICAgICAgICAgICAgICBpZiAoXG4gICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblNlbGVjdC5vcHRpb25zW2ldLnZhbHVlID09IHRvZ2dsZUZpcnN0SURcbiAgICAgICAgICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblNlbGVjdC52YWx1ZSA9IHRvZ2dsZUZpcnN0SUQ7XG4gICAgICAgICAgICAgICAgICAgICAgICAkKFwiI1wiICsgc2VsZWN0b3JJZCkuZGF0YShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBcInRvZ2dsZV9jdXJyZW50XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlRmlyc3RJRFxuICAgICAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICAgICAgICAgICQoXCIjXCIgKyBzZWxlY3RvcklkKS5kYXRhKFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIFwidG9nZ2xlX2N1cnJlbnRfdHlwZVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uVHlwZXNbMF1cbiAgICAgICAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgICAgICAgICBicmVhaztcbiAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICB0b2dnbGVRdWVzdGlvblNlbGVjdC5hZGRFdmVudExpc3RlbmVyKFxuICAgICAgICAgICAgICAgICAgICBcImNoYW5nZVwiLFxuICAgICAgICAgICAgICAgICAgICBhc3luYyBmdW5jdGlvbiAoKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnRvZ2dsZVByZXZpZXcoXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25TZWxlY3QucGFyZW50RWxlbWVudC5pZCxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBkYXRhLnRvZ2dsZU9wdGlvbnMsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9nZ2xlUXVlc3Rpb25UeXBlc1xuICAgICAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICAgICAgfS5iaW5kKHRoaXMpXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gcmVzcG9uc2U7XG4gICAgfVxuXG4gICAgLy8gcmV0cmlldmUgaHRtbCBzb3VyY2Ugb2YgYSBxdWVzdGlvbiwgZm9yIHVzZSBpbiB2YXJpb3VzIHRvZ2dsZSBmdW5jdGlvbmFsaXRpZXNcbiAgICBhc3luYyBnZXRUb2dnbGVTcmModG9nZ2xlUXVlc3Rpb25JRCkge1xuICAgICAgICBsZXQgcmVxdWVzdCA9IG5ldyBSZXF1ZXN0KFxuICAgICAgICAgICAgXCIvcnVuZXN0b25lL2FkbWluL2h0bWxzcmM/YWNpZD1cIiArIHRvZ2dsZVF1ZXN0aW9uSUQsXG4gICAgICAgICAgICB7XG4gICAgICAgICAgICAgICAgbWV0aG9kOiBcIkdFVFwiLFxuICAgICAgICAgICAgfVxuICAgICAgICApO1xuICAgICAgICBsZXQgcmVzcG9uc2UgPSBhd2FpdCBmZXRjaChyZXF1ZXN0KTtcbiAgICAgICAgbGV0IGh0bWxzcmMgPSBhd2FpdCByZXNwb25zZS5qc29uKCk7XG4gICAgICAgIHJldHVybiBodG1sc3JjO1xuICAgIH1cblxuICAgIC8vIG9uIGNoYW5naW5nIHRoZSB2YWx1ZSBvZiB0b2dnbGUgc2VsZWN0IGRyb3Bkb3duLCByZW5kZXIgc2VsZWN0ZWQgcXVlc3Rpb24gaW4gcHJldmlldyBwYW5lbCwgYWRkIGFwcHJvcHJpYXRlIGJ1dHRvbnMsIHRoZW4gbWFrZSBwcmV2aWV3IHBhbmVsIHZpc2libGVcbiAgICBhc3luYyB0b2dnbGVQcmV2aWV3KHBhcmVudElELCB0b2dnbGVPcHRpb25zLCB0b2dnbGVRdWVzdGlvblR5cGVzKSB7XG4gICAgICAgICQoXCIjdG9nZ2xlLWJ1dHRvbnNcIikuaHRtbChcIlwiKTtcbiAgICAgICAgdmFyIHBhcmVudERpdiA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKHBhcmVudElEKTtcbiAgICAgICAgdmFyIHRvZ2dsZVF1ZXN0aW9uU2VsZWN0ID0gcGFyZW50RGl2LmdldEVsZW1lbnRzQnlUYWdOYW1lKFwic2VsZWN0XCIpWzBdO1xuICAgICAgICB2YXIgc2VsZWN0ZWRRdWVzdGlvbiA9XG4gICAgICAgICAgICB0b2dnbGVRdWVzdGlvblNlbGVjdC5vcHRpb25zW3RvZ2dsZVF1ZXN0aW9uU2VsZWN0LnNlbGVjdGVkSW5kZXhdXG4gICAgICAgICAgICAgICAgLnZhbHVlO1xuICAgICAgICB2YXIgaHRtbHNyYyA9IGF3YWl0IHRoaXMuZ2V0VG9nZ2xlU3JjKHNlbGVjdGVkUXVlc3Rpb24pO1xuICAgICAgICByZW5kZXJSdW5lc3RvbmVDb21wb25lbnQoaHRtbHNyYywgXCJ0b2dnbGUtcHJldmlld1wiLCB7XG4gICAgICAgICAgICBzZWxlY3Rvcl9pZDogXCJ0b2dnbGUtcHJldmlld1wiLFxuICAgICAgICAgICAgdXNlUnVuZXN0b25lU2VydmljZXM6IHRydWUsXG4gICAgICAgIH0pO1xuXG4gICAgICAgIC8vIGFkZCBcIkNsb3NlIFByZXZpZXdcIiBidXR0b24gdG8gdGhlIHByZXZpZXcgcGFuZWxcbiAgICAgICAgbGV0IGNsb3NlQnV0dG9uID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudChcImJ1dHRvblwiKTtcbiAgICAgICAgJChjbG9zZUJ1dHRvbikudGV4dChcIkNsb3NlIFByZXZpZXdcIik7XG4gICAgICAgICQoY2xvc2VCdXR0b24pLmFkZENsYXNzKFwiYnRuIGJ0bi1kZWZhdWx0XCIpO1xuICAgICAgICAkKGNsb3NlQnV0dG9uKS5jbGljayhmdW5jdGlvbiAoZXZlbnQpIHtcbiAgICAgICAgICAgICQoXCIjdG9nZ2xlLXByZXZpZXdcIikuaHRtbChcIlwiKTtcbiAgICAgICAgICAgIHRvZ2dsZVF1ZXN0aW9uU2VsZWN0LnZhbHVlID0gJChcIiNcIiArIHBhcmVudElEKS5kYXRhKFxuICAgICAgICAgICAgICAgIFwidG9nZ2xlX2N1cnJlbnRcIlxuICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICQoXCIjY29tcG9uZW50LXByZXZpZXdcIikuaGlkZSgpO1xuICAgICAgICB9KTtcbiAgICAgICAgJChcIiN0b2dnbGUtYnV0dG9uc1wiKS5hcHBlbmQoY2xvc2VCdXR0b24pO1xuXG4gICAgICAgIC8vIGlmIFwibG9ja1wiIGlzIG5vdCBpbiB0b2dnbGUgb3B0aW9ucywgdGhlbiBhbGxvdyBhZGRpbmcgbW9yZSBidXR0b25zIHRvIHRoZSBwcmV2aWV3IHBhbmVsIFxuICAgICAgICBpZiAoISh0b2dnbGVPcHRpb25zLmluY2x1ZGVzKFwibG9ja1wiKSkpIHtcbiAgICAgICAgICAgIGxldCBzZXRCdXR0b24gPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KFwiYnV0dG9uXCIpO1xuICAgICAgICAgICAgJChzZXRCdXR0b24pLnRleHQoXCJTZWxlY3QgdGhpcyBQcm9ibGVtXCIpO1xuICAgICAgICAgICAgJChzZXRCdXR0b24pLmFkZENsYXNzKFwiYnRuIGJ0bi1wcmltYXJ5XCIpO1xuICAgICAgICAgICAgJChzZXRCdXR0b24pLmNsaWNrKFxuICAgICAgICAgICAgICAgIGFzeW5jIGZ1bmN0aW9uICgpIHtcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgdGhpcy50b2dnbGVTZXQocGFyZW50SUQsIHNlbGVjdGVkUXVlc3Rpb24sIGh0bWxzcmMsIHRvZ2dsZVF1ZXN0aW9uVHlwZXMpO1xuICAgICAgICAgICAgICAgICAgICAkKFwiI2NvbXBvbmVudC1wcmV2aWV3XCIpLmhpZGUoKTtcbiAgICAgICAgICAgICAgICB9LmJpbmQodGhpcylcbiAgICAgICAgICAgICk7XG4gICAgICAgICAgICAkKFwiI3RvZ2dsZS1idXR0b25zXCIpLmFwcGVuZChzZXRCdXR0b24pO1xuXG4gICAgICAgICAgICAvLyBpZiBcInRyYW5zZmVyXCIgaW4gdG9nZ2xlIG9wdGlvbnMsIGFuZCBpZiBjdXJyZW50IHF1ZXN0aW9uIHR5cGUgaXMgUGFyc29ucyBhbmQgc2VsZWN0ZWQgcXVlc3Rpb24gdHlwZSBpcyBhY3RpdmUgY29kZSwgdGhlbiBhZGQgXCJUcmFuc2ZlclwiIGJ1dHRvbiB0byBwcmV2aWV3IHBhbmVsXG4gICAgICAgICAgICBpZiAodG9nZ2xlT3B0aW9ucy5pbmNsdWRlcyhcInRyYW5zZmVyXCIpKSB7XG4gICAgICAgICAgICAgICAgdmFyIGN1cnJlbnRUeXBlID0gJChcIiNcIiArIHBhcmVudElEKS5kYXRhKFwidG9nZ2xlX2N1cnJlbnRfdHlwZVwiKTtcbiAgICAgICAgICAgICAgICB2YXIgc2VsZWN0ZWRUeXBlID0gdG9nZ2xlUXVlc3Rpb25UeXBlc1t0b2dnbGVRdWVzdGlvblNlbGVjdC5zZWxlY3RlZEluZGV4XTtcbiAgICAgICAgICAgICAgICBpZiAoKGN1cnJlbnRUeXBlID09IFwiUGFyc29ucyBNaXhlZC1VcCBDb2RlXCIpICYmIChzZWxlY3RlZFR5cGUgPT0gXCJBY3RpdmUgV3JpdGUgQ29kZVwiKSkge1xuICAgICAgICAgICAgICAgICAgICBsZXQgdHJhbnNmZXJCdXR0b24gPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KFwiYnV0dG9uXCIpO1xuICAgICAgICAgICAgICAgICAgICAkKHRyYW5zZmVyQnV0dG9uKS50ZXh0KFwiVHJhbnNmZXIgUmVzcG9uc2VcIik7XG4gICAgICAgICAgICAgICAgICAgICQodHJhbnNmZXJCdXR0b24pLmFkZENsYXNzKFwiYnRuIGJ0bi1wcmltYXJ5XCIpO1xuICAgICAgICAgICAgICAgICAgICAkKHRyYW5zZmVyQnV0dG9uKS5jbGljayhcbiAgICAgICAgICAgICAgICAgICAgICAgIGFzeW5jIGZ1bmN0aW9uICgpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnRvZ2dsZVRyYW5zZmVyKHBhcmVudElELCBzZWxlY3RlZFF1ZXN0aW9uLCBodG1sc3JjLCB0b2dnbGVRdWVzdGlvblR5cGVzKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH0uYmluZCh0aGlzKVxuICAgICAgICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICAgICAgICAkKFwiI3RvZ2dsZS1idXR0b25zXCIpLmFwcGVuZCh0cmFuc2ZlckJ1dHRvbik7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9XG5cbiAgICAgICAgJChcIiNjb21wb25lbnQtcHJldmlld1wiKS5zaG93KCk7XG4gICAgfVxuXG4gICAgLy8gb24gY2xpY2tpbmcgXCJTZWxlY3QgdGhpcyBQcm9ibGVtXCIgYnV0dG9uLCBjbG9zZSBwcmV2aWV3IHBhbmVsLCByZXBsYWNlIGN1cnJlbnQgcXVlc3Rpb24gaW4gYXNzaWdubWVudHMgcGFnZSB3aXRoIHNlbGVjdGVkIHF1ZXN0aW9uLCBhbmQgc2VuZCByZXF1ZXN0IHRvIHVwZGF0ZSBncmFkaW5nIGRhdGFiYXNlXG4gICAgYXN5bmMgdG9nZ2xlU2V0KHBhcmVudElELCBzZWxlY3RlZFF1ZXN0aW9uLCBodG1sc3JjLCB0b2dnbGVRdWVzdGlvblR5cGVzKSB7XG4gICAgICAgIHZhciBzZWxlY3RvcklkID0gcGFyZW50SUQgKyBcIi10b2dnbGVTZWxlY3RlZFF1ZXN0aW9uXCI7XG4gICAgICAgIHZhciB0b2dnbGVRdWVzdGlvblNlbGVjdCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKHBhcmVudElEKS5nZXRFbGVtZW50c0J5VGFnTmFtZShcInNlbGVjdFwiKVswXTtcbiAgICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoc2VsZWN0b3JJZCkuaW5uZXJIVE1MID0gXCJcIjsgLy8gbmVlZCB0byBjaGVjayB3aGV0aGVyIHRoaXMgaXMgZXZlbiBuZWNlc3NhcnlcbiAgICAgICAgYXdhaXQgcmVuZGVyUnVuZXN0b25lQ29tcG9uZW50KGh0bWxzcmMsIHNlbGVjdG9ySWQsIHtcbiAgICAgICAgICAgIHNlbGVjdG9yX2lkOiBzZWxlY3RvcklkLFxuICAgICAgICAgICAgdXNlUnVuZXN0b25lU2VydmljZXM6IHRydWUsXG4gICAgICAgIH0pO1xuICAgICAgICBsZXQgcmVxdWVzdCA9IG5ldyBSZXF1ZXN0KFxuICAgICAgICAgICAgXCIvcnVuZXN0b25lL2FqYXgvdXBkYXRlX3NlbGVjdGVkX3F1ZXN0aW9uP21ldGFpZD1cIiArXG4gICAgICAgICAgICAgICAgcGFyZW50SUQgK1xuICAgICAgICAgICAgICAgIFwiJnNlbGVjdGVkPVwiICtcbiAgICAgICAgICAgICAgICBzZWxlY3RlZFF1ZXN0aW9uLFxuICAgICAgICAgICAge31cbiAgICAgICAgKTtcbiAgICAgICAgYXdhaXQgZmV0Y2gocmVxdWVzdCk7XG4gICAgICAgICQoXCIjdG9nZ2xlLXByZXZpZXdcIikuaHRtbChcIlwiKTtcbiAgICAgICAgJChcIiNcIiArIHBhcmVudElEKS5kYXRhKFwidG9nZ2xlX2N1cnJlbnRcIiwgc2VsZWN0ZWRRdWVzdGlvbik7XG4gICAgICAgICQoXCIjXCIgKyBwYXJlbnRJRCkuZGF0YShcInRvZ2dsZV9jdXJyZW50X3R5cGVcIiwgdG9nZ2xlUXVlc3Rpb25UeXBlc1t0b2dnbGVRdWVzdGlvblNlbGVjdC5zZWxlY3RlZEluZGV4XSk7XG4gICAgfVxuXG4gICAgLy8gb24gY2xpY2tpbmcgXCJUcmFuc2ZlclwiIGJ1dHRvbiwgZXh0cmFjdCB0aGUgY3VycmVudCB0ZXh0IGFuZCBpbmRlbnRhdGlvbiBvZiB0aGUgUGFyc29ucyBibG9ja3MgaW4gdGhlIGFuc3dlciBzcGFjZSwgdGhlbiBwYXN0ZSB0aGF0IGludG8gdGhlIHNlbGVjdGVkIGFjdGl2ZSBjb2RlIHF1ZXN0aW9uXG4gICAgYXN5bmMgdG9nZ2xlVHJhbnNmZXIocGFyZW50SUQsIHNlbGVjdGVkUXVlc3Rpb24sIGh0bWxzcmMsIHRvZ2dsZVF1ZXN0aW9uVHlwZXMpIHtcbiAgICAgICAgLy8gcmV0cmlldmUgYWxsIFBhcnNvbnMgbGluZXMgd2l0aGluIHRoZSBhbnN3ZXIgc3BhY2UgYW5kIGxvb3AgdGhyb3VnaCB0aGlzIGxpc3RcbiAgICAgICAgdmFyIGN1cnJlbnRQYXJzb25zID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQocGFyZW50SUQgKyBcIi10b2dnbGVTZWxlY3RlZFF1ZXN0aW9uXCIpLnF1ZXJ5U2VsZWN0b3JBbGwoXCJkaXZbY2xhc3NePSdhbnN3ZXInXVwiKVswXS5nZXRFbGVtZW50c0J5Q2xhc3NOYW1lKFwicHJldHR5cHJpbnQgbGFuZy1weVwiKTtcbiAgICAgICAgdmFyIGN1cnJlbnRQYXJzb25zQ2xhc3M7XG4gICAgICAgIHZhciBjdXJyZW50QmxvY2tJbmRlbnQ7XG4gICAgICAgIHZhciBpbmRlbnRDb3VudFxuICAgICAgICB2YXIgaW5kZW50O1xuICAgICAgICB2YXIgcGFyc29uc0xpbmU7XG4gICAgICAgIHZhciBwYXJzb25zTGluZXMgPSBgYDtcbiAgICAgICAgdmFyIGNvdW50O1xuICAgICAgICBmb3IgKHZhciBwID0gMDsgcCA8IGN1cnJlbnRQYXJzb25zLmxlbmd0aDsgcCsrKSB7XG4gICAgICAgICAgICBpbmRlbnRDb3VudCA9IDA7XG4gICAgICAgICAgICBpbmRlbnQgPSBcIlwiO1xuICAgICAgICAgICAgLy8gZm9yIFBhcnNvbnMgYmxvY2tzIHRoYXQgaGF2ZSBidWlsdC1pbiBpbmRlbnRhdGlvbiBpbiB0aGVpciBsaW5lc1xuICAgICAgICAgICAgY3VycmVudFBhcnNvbnNDbGFzcyA9IGN1cnJlbnRQYXJzb25zW3BdLmNsYXNzTGlzdFsyXTtcbiAgICAgICAgICAgIGlmIChjdXJyZW50UGFyc29uc0NsYXNzKSB7XG4gICAgICAgICAgICAgICAgaWYgKGN1cnJlbnRQYXJzb25zQ2xhc3MuaW5jbHVkZXMoXCJpbmRlbnRcIikpIHtcbiAgICAgICAgICAgICAgICAgICAgaW5kZW50Q291bnQgPSBwYXJzZUludChpbmRlbnRDb3VudCkgKyBwYXJzZUludChjdXJyZW50UGFyc29uc0NsYXNzLnNsaWNlKDYsY3VycmVudFBhcnNvbnNDbGFzcy5sZW5ndGgpKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICAvLyBmb3IgUGFyc29ucyBhbnN3ZXIgc3BhY2VzIHdpdGggdmVydGljYWwgbGluZXMgdGhhdCBhbGxvdyBzdHVkZW50IHRvIGRlZmluZSB0aGVpciBvd24gbGluZSBpbmRlbnRhdGlvblxuICAgICAgICAgICAgY3VycmVudEJsb2NrSW5kZW50ID0gY3VycmVudFBhcnNvbnNbcF0ucGFyZW50RWxlbWVudC5wYXJlbnRFbGVtZW50LnN0eWxlLmxlZnQ7XG4gICAgICAgICAgICBpZiAoY3VycmVudEJsb2NrSW5kZW50KSB7XG4gICAgICAgICAgICAgICAgaW5kZW50Q291bnQgPSBwYXJzZUludChpbmRlbnRDb3VudCkgKyBwYXJzZUludChjdXJyZW50QmxvY2tJbmRlbnQuc2xpY2UoMCxjdXJyZW50QmxvY2tJbmRlbnQuaW5kZXhPZihcInB4XCIpKSAvIDMwKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGZvciAodmFyIGQgPSAwOyBkIDwgaW5kZW50Q291bnQ7IGQrKykge1xuICAgICAgICAgICAgICAgIGluZGVudCArPSBcIiAgICBcIjtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIC8vIHJldHJpZXZlIGVhY2ggdGV4dCBzbmlwcGV0IG9mIGVhY2ggUGFyc29ucyBsaW5lIGFuZCBsb29wIHRocm91Z2ggdGhpcyBsaXN0XG4gICAgICAgICAgICBwYXJzb25zTGluZSA9IGN1cnJlbnRQYXJzb25zW3BdLmdldEVsZW1lbnRzQnlUYWdOYW1lKFwic3BhblwiKTtcbiAgICAgICAgICAgIGNvdW50ID0gMDtcbiAgICAgICAgICAgIGZvciAodmFyIGwgPSAwOyBsIDwgcGFyc29uc0xpbmUubGVuZ3RoOyBsKyspIHtcbiAgICAgICAgICAgICAgICBpZiAocGFyc29uc0xpbmVbbF0uY2hpbGROb2Rlc1swXS5ub2RlTmFtZSA9PSBcIiN0ZXh0XCIpIHsgLy8gUGFyc29ucyBibG9ja3MgaGF2ZSBkaWZmZXJpbmcgYW1vdW50cyBvZiBoaWVyYXJjaHkgbGV2ZWxzIChzcGFucyB3aXRoaW4gc3BhbnMpXG4gICAgICAgICAgICAgICAgICAgIGlmICgocCA9PSAwKSAmJiAoY291bnQgPT0gMCkpIHsgLy8gbmVlZCBkaWZmZXJlbnQgY2hlY2sgdGhhbiBsID09IDAgYmVjYXVzZSB0aGUgbCBudW1iZXJpbmcgZG9lc24ndCBhbGlnbiB3aXRoIGxvY2F0aW9uIHdpdGhpbiBsaW5lIGR1ZSB0byBpbmNvbnNpc3RlbnQgc3BhbiBoZWlyYXJjaHlcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhcnNvbnNMaW5lcyArPSBpbmRlbnQgKyBwYXJzb25zTGluZVtsXS5pbm5lckhUTUw7XG4gICAgICAgICAgICAgICAgICAgICAgICBjb3VudCsrO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIGVsc2UgaWYgKGNvdW50ICE9IDApIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHBhcnNvbnNMaW5lcyArPSBwYXJzb25zTGluZVtsXS5pbm5lckhUTUw7XG4gICAgICAgICAgICAgICAgICAgICAgICBjb3VudCsrO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgcGFyc29uc0xpbmVzID0gcGFyc29uc0xpbmVzICsgYFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGAgKyBpbmRlbnQgKyBwYXJzb25zTGluZVtsXS5pbm5lckhUTUw7XG4gICAgICAgICAgICAgICAgICAgICAgICBwYXJzb25zTGluZXMgPSBwYXJzb25zTGluZXMucmVwbGFjZShcIiAgICAgICAgICAgICAgICAgICAgICAgICAgICBcIiwgXCJcIik7XG4gICAgICAgICAgICAgICAgICAgICAgICBjb3VudCsrO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICAgIC8vIHJlcGxhY2UgYWxsIGV4aXN0aW5nIGNvZGUgd2l0aGluIHNlbGVjdGVkIGFjdGl2ZSBjb2RlIHF1ZXN0aW9uIHdpdGggZXh0cmFjdGVkIFBhcnNvbnMgdGV4dFxuICAgICAgICB2YXIgaHRtbHNyY0Zvcm1lciA9IGh0bWxzcmMuc2xpY2UoMCwgaHRtbHNyYy5pbmRleE9mKFwiPHRleHRhcmVhXCIpICsgaHRtbHNyYy5zcGxpdChcIjx0ZXh0YXJlYVwiKVsxXS5pbmRleE9mKFwiPlwiKSArIDEwKTtcbiAgICAgICAgdmFyIGh0bWxzcmNMYXR0ZXIgPSBodG1sc3JjLnNsaWNlKGh0bWxzcmMuaW5kZXhPZihcIjwvdGV4dGFyZWE+XCIpLCBodG1sc3JjLmxlbmd0aCk7XG4gICAgICAgIGh0bWxzcmMgPSBodG1sc3JjRm9ybWVyICsgcGFyc29uc0xpbmVzICsgaHRtbHNyY0xhdHRlcjtcblxuICAgICAgICBhd2FpdCB0aGlzLnRvZ2dsZVNldChwYXJlbnRJRCwgc2VsZWN0ZWRRdWVzdGlvbiwgaHRtbHNyYywgdG9nZ2xlUXVlc3Rpb25UeXBlcyk7XG4gICAgICAgICQoXCIjY29tcG9uZW50LXByZXZpZXdcIikuaGlkZSgpO1xuICAgIH1cbn1cblxuLypcbiAqIFdoZW4gdGhlIHBhZ2UgaXMgbG9hZGVkIGFuZCB0aGUgbG9naW4gY2hlY2tzIGFyZSBjb21wbGV0ZSBmaW5kIGFuZCByZW5kZXJcbiAqIGVhY2ggc2VsZWN0cXVlc3Rpb24gY29tcG9uZW50IHRoYXQgaXMgbm90IHBhcnQgb2YgYSB0aW1lZEFzc2Vzc21lbnQuXG4gKiovXG4kKGRvY3VtZW50KS5iaW5kKFwicnVuZXN0b25lOmxvZ2luLWNvbXBsZXRlXCIsIGFzeW5jIGZ1bmN0aW9uICgpIHtcbiAgICBsZXQgc2VsUXVlc3Rpb25zID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbChcbiAgICAgICAgXCJbZGF0YS1jb21wb25lbnQ9c2VsZWN0cXVlc3Rpb25dXCJcbiAgICApO1xuICAgIGZvciAobGV0IGNxIG9mIHNlbFF1ZXN0aW9ucykge1xuICAgICAgICB0cnkge1xuICAgICAgICAgICAgaWYgKCQoY3EpLmNsb3Nlc3QoXCJbZGF0YS1jb21wb25lbnQ9dGltZWRBc3Nlc3NtZW50XVwiKS5sZW5ndGggPT0gMCkge1xuICAgICAgICAgICAgICAgIC8vIElmIHRoaXMgZWxlbWVudCBleGlzdHMgd2l0aGluIGEgdGltZWQgY29tcG9uZW50LCBkb24ndCByZW5kZXIgaXQgaGVyZVxuICAgICAgICAgICAgICAgIGxldCB0bXAgPSBuZXcgU2VsZWN0T25lKHsgb3JpZzogY3EgfSk7XG4gICAgICAgICAgICAgICAgYXdhaXQgdG1wLmluaXRpYWxpemUoKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfSBjYXRjaCAoZXJyKSB7XG4gICAgICAgICAgICBjb25zb2xlLmxvZyhgRXJyb3IgcmVuZGVyaW5nIE5ldyBFeGVyY2lzZSAke2NxLmlkfVxuICAgICAgICAgICAgICAgICAgICAgICAgIERldGFpbHM6ICR7ZXJyfWApO1xuICAgICAgICAgICAgY29uc29sZS5sb2coZXJyLnN0YWNrKTtcbiAgICAgICAgfVxuICAgIH1cbn0pO1xuIl0sInNvdXJjZVJvb3QiOiIifQ==