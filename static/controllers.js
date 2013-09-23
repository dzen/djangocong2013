var module = angular.module('DjangoCong', []);


module.controller('WebsocketController', function ($scope) {
    $scope.ws =  new WebSocket($scope.server);
    $scope.data = {};
    $scope.ws.onopen = function(event) {
        console.log("ws opened");
    };
    $scope.ws.onmessage = function(msg) {
        var data = JSON.parse(msg.data);
        $scope.$apply(function() {
            $scope.data = data;
            console.log($scope.data);
        });
    };
});
