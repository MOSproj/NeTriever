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

            self.category['specRange'] = {};
            self.category['specselect'] = {};
            angular.forEach(self.category['specs'], function(specValues, speckey) {
                if (angular.isArray(specValues)) {
                    self.category['specselect'][speckey] = {
                        'data': specValues,
                        'selected': []
                    };
                } else
                    self.category['specRange'][speckey] = specValues;
            });
            $log.log(self.category['specRange']);
            $log.log(self.category['specselect']);
        });

        self.specselectSettings = {
            scrollable: true,
            smartButtonMaxItems: 3,
            template: '{{ option }}',
            smartButtonTextConverter: function(skip, option) { return option; }
        }
    }
})();
