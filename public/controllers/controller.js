var myApp = angular.module('myApp', []);

myApp.controller('categoriesCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.category = "asd";
    $http.get('/categories').then(function (response) {
        console.log(response);
        $scope.categories = response.data;
    });
}]);

myApp.controller('postsCtrl', ['$scope', '$http', function ($scope, $http) {
    console.log($scope.category);
    $http.get('/posts' , $scope.category).then(function (response) {
        console.log(response);
        $scope.posts = response.data;
    });
}]);
