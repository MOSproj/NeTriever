(function(){
    "use strict";

    angular.module('myApp').controller('categoriesCtrl', ["$scope", "categoriesServices", categoriesCtrl]);

    function categoriesCtrl ($scope, categoriesServices) {
        categoriesServices.getCategories().then(function (response) {
            console.log(response);
            $scope.categories = response.data;
        });
    }
})();
