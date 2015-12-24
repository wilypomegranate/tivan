(function() {
  'use strict';

  angular
    .module('materialUi')
    .controller('CameraController', CameraController);

  /** @ngInject */
  function CameraController($timeout, $http) {
    var vm = this;

    vm.cameras = [];
    $http.get('/api/camera/').success(function(data){
      vm.cameras = data;
    });

    vm.getLiveCameraUrl = function(camera_id) {
      return '/api/video/live/' + camera_id;
    }
 
  }
})();
