(function(){
    "use strict";

    angular.module('myApp').controller('homeCtrl', ["$scope", homeCtrl]);

    function homeCtrl ($scope) {
        var self = this;

        self.devs = [
            {
                "name": "אוהד כהן",
                "img": "ohad.jpg",
                "facebook": "ohadc89",
                "linkedin": "ohad-cohen-9020a5126"
            },
            {
                "name": "מירית לסרי",
                "img": "mirit.jpg",
                "facebook": "1823866195",
                "linkedin": "mirit-lasry-49a119144"
            },
            {
                "name": "סיון כהן",
                "img": "sivan.jpg",
                "facebook": "sivan.cohen.50",
                "linkedin": "sivan-cohen-a48a74119"
            }
        ];
    }
})();
