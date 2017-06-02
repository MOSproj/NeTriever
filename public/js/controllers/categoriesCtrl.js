(function(){
    "use strict";

    angular.module('myApp').controller('categoriesCtrl', ["$scope", "$log", "$location", "categoriesSrv", categoriesCtrl]);

    function categoriesCtrl ($scope, $log, $location, categoriesSrv) {
        var self = this;

        self.isActive = function (viewLocation) {
            return viewLocation === $location.path();
        };

        /*categoriesSrv.getCategories().then(function (response) {
         $log.debug(response.data);
         self.categories = response.data;
         });*/

        categoriesSrv.getCategoriesNames().then(function (response) {
            //console.log(response.data);
            self.categoriesNames = response.data;
        });
    }
})();
