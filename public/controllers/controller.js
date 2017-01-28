var myApp = angular.module('myApp', []);
myApp.controller('AppCtrl', ['$scope', '$http', function ($scope, $http) {
    console.log("Hello World from controller");

    $http.get('/posts').then(function (response) {
        console.log(response);
        $scope.posts = response;
    });
}]);
