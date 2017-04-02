(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http, $log){
        return {
            getPosts : function(category, page){
                return $http.get('/api/category/' + category + '/page/' + page);
            }
        };
    }
})();
