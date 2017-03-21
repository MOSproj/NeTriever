(function(){
    "use strict";

    angular.module('myApp').controller('categoriesCtrl', ["$scope", "$location", "categoriesSrv", categoriesCtrl]);

    function categoriesCtrl ($scope, $location, categoriesSrv) {
        var self = this;
        self.isActive = function (viewLocation) {
            return viewLocation === $location.path();
        };
        categoriesSrv.getCategories().then(function (response) {
            console.log(response);
            self.categories = response.data;
        });
    }
})();
