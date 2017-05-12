(function(){
    "use strict";

    angular.module('myApp').controller('searchCtrl', ["$scope", "$routeParams", "$location", "$log", "categoriesSrv", postsCtrl]);

    function postsCtrl ($scope, $routeParams, $location, $log, categoriesSrv) {
        var self = this;
        var reqParams = $location.search();
        self.categoryId = $routeParams['categoryId'];

        categoriesSrv.getCategory(self.categoryId).then(function (response) {
            $log.debug(response.data);
            $log.debug(reqParams);

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
                        min: null,
                        max: null
                    };
                    if(speckey in reqParams){
                        if(parseFloat(reqParams[speckey].split(",")[0]) >= 0)
                            self.specRange[speckey]['min'] = parseFloat(reqParams[speckey].split(",")[0]);
                        if(parseFloat(reqParams[speckey].split(",")[1]) >= 0)
                            self.specRange[speckey]['max'] = parseFloat(reqParams[speckey].split(",")[1]);
                    }
                }
            });
        });

        self.specselectSettings = {
            enableSearch: true,
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
                if(val['selected'].length > 0 || key in reqParams){
                    specs[key] = val['selected'];
                }
            });
            angular.forEach(self.specRange, function (val, key) {
                if((angular.isNumber(val['min']) && val['min'] >= 0) ||
                    (angular.isNumber(val['max']) && val['max'] >= 0)){
                    specs[key] = '';
                    if(angular.isNumber(val['min']) && val['min'] >= 0)
                        specs[key] += val['min'];
                    else
                        specs[key] += '-1';
                    specs[key] += ',';
                    if(angular.isNumber(val['max']) && val['max'] >= 0)
                        specs[key] += val['max'];
                    else
                        specs[key] += '-1';
                } else if(key in reqParams) {
                    delete reqParams[key];
                }
            });
            angular.extend(reqParams, specs);
            $location.path($location.path()).search(reqParams);
        };
    }
})();
