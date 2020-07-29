// ==UserScript==
// @name         SynackClick
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Will auto OK all PopUps on platform
// @author       You
// @match        https://platform.synack.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    window.confirm = () => {
    return true
    }

})();
