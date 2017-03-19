(function(){
    "use strict";

    angular.module('myApp').controller('categoriesCtrl', ["$scope", "postsServices", categoriesCtrl]);

    function categoriesCtrl ($scope, postsServices) {
        postsServices.getCategories().then(function (response) {
            console.log(response);
            $scope.categories = response.data;
        });
    }
})();
