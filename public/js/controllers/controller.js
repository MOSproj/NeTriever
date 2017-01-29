myApp.controller('categoriesCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.category = "";
    $http.get('/categories').then(function (response) {
        console.log(response);
        $scope.categories = response.data;
    });

    $scope.updatePosts = function () {
        console.log($scope.category);
    }
}]);

myApp.controller('postsCtrl', ['$scope', '$http', function ($scope, $http) {
    if ($scope.category == "") {
        $http.get('/posts').then(function (response) {
            console.log(response);
            $scope.posts = response.data;
        });
    } else {
        $http.get('/posts/' + category).then(function (response) {
            console.log(response);
            $scope.posts = response.data;
        });
    }
}]);