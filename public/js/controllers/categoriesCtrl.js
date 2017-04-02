(function(){
    "use strict";

    angular.module('myApp').controller('categoriesCtrl', ["$scope", "$log", "$location", "categoriesSrv", categoriesCtrl]);

    function categoriesCtrl ($scope, $log, $location, categoriesSrv) {
        var self = this;

        self.isActive = function (viewLocation) {
            var lastIndexOfSlash = $location.path().lastIndexOf("/");
            return viewLocation === $location.path().substring(0,lastIndexOfSlash + 1);
        };

        categoriesSrv.getCategories().then(function (response) {
            $log.debug(response.data);
            self.categories = response.data;
        });
    }
})();
