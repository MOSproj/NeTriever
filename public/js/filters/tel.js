(function () {
    angular.module('myApp').filter('tel', function () {
        return function (tel) {
            if (!tel) { return ''; }

            var value = tel.toString().trim().replace(/^\+/, '');

            if (value.match(/[^0-9]/)) {
                return tel;
            }

            var answer = value.slice(0,3);
            answer += '-';
            answer += value.slice(3,6);
            answer += '-';
            answer += value.slice(6);

            return answer;
        };
    });
})();
