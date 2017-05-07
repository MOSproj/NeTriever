(function(){
    "use strict";

    angular.module('myApp').controller('searchCtrl', ["$scope", "$routeParams", "$location", "$log", "categoriesSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $location, $log, categoriesSrv) {
        var self = this;
        var reqParams = $location.search();
        self.categoryId = $routeParams['categoryId'];

        categoriesSrv.getCategory(self.categoryId).then(function (response) {
            $log.debug(response.data);

            self.category = response.data;

            self.specRange = {};
            self.specselect = {};
            angular.forEach(self.category['specs'], function(specValues, speckey) {
                if (angular.isArray(specValues)) {
                    self.specselect[speckey] = {
                        'data': specValues,
                        'selected': []
                    };
                    if(speckey in reqParams){
                        self.specselect[speckey]['selected'] = reqParams[speckey];
                    }
                } else {
                    self.specRange[speckey] = {
                        min: specValues.split("-")[0],
                        max: specValues.split("-")[1],
                        model_min: specValues.split("-")[0],
                        model_max: specValues.split("-")[1]
                    };
                    if(speckey in reqParams){
                        self.specRange[speckey]['model_min'] = parseInt(reqParams[speckey].split("-")[0]);
                        self.specRange[speckey]['model_max'] = parseInt(reqParams[speckey].split("-")[1]);
                    }
                }

            });
        });

        self.specselectSettings = {
            scrollable: true,
            showCheckAll: false,
            showUncheckAll: false,
            keyboardControls: true,
            smartButtonMaxItems: 5,
            template: '{{ option }}',
            smartButtonTextConverter: function(skip, option) { return option; }
        };

        self.search = function () {
            var specs = {};
            angular.forEach(self.specselect, function (val, key) {
                if(val['selected'].length > 0){
                    specs[key] = val['selected'];
                }
                if(key in reqParams && reqParams[key] !== val['selected']){
                    specs[key] = val['selected'];
                }
            });
            angular.forEach(self.specRange, function (val, key) {
                if(val['min'] !== val['model_min'] ||  val['max'] !== val['model_max']){
                    specs[key] = val['model_min'] + '-' + val['model_max'];
                }
                if(key in reqParams &&
                    (reqParams[key].split("-")[0] !== val['model_min'] ||
                    reqParams[key].split("-")[1] !== val['model_max'])){
                    specs[key] = val['model_min'] + '-' + val['model_max'];
                }
            });
            angular.extend(reqParams, specs);
            $location.path($location.path()).search(reqParams);
        };
    }
})();
