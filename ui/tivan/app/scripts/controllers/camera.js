'use strict';

/**
 * @ngdoc function
 * @name tivanApp.controller:CameraCtrl
 * @description
 * # CameraCtrl
 * Controller of the tivanApp
 */
angular.module('tivanApp')
  .controller('CameraCtrl', function ($scope, $http) {
      $scope.cameras = [];
      $http.get('/camera/').success(function(data){
        $scope.cameras = data;
      })
  });
