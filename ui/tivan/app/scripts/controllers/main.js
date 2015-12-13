'use strict';

/**
 * @ngdoc function
 * @name tivanApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the tivanApp
 */
angular.module('tivanApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.events = [];

    $http.get('/api/events/').success(function(data){
        $scope.events = data;
    })

    $scope.getVideoFromEvent = function(event_id) {
        return '/api/video/retrieval/' + event_id + '/';
    }

  });
