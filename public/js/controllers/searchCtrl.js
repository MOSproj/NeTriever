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
                } else
                    self.specRange[speckey] = {
                        min: specValues.split("-")[0],
                        max: specValues.split("-")[1],
                        model_min: specValues.split("-")[0],
                        model_max: specValues.split("-")[1]
                    }
            });
            $log.log(self.specRange);
            $log.log(self.specselect);
        });

        self.specselectSettings = {
            scrollable: true,
            smartButtonMaxItems: 3,
            template: '{{ option }}',
            smartButtonTextConverter: function(skip, option) { return option; }
        }
    }
})();
