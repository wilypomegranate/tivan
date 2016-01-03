(function() {
  'use strict';

  angular
    .module('materialUi')
    .controller('CameraSelectController', CameraSelectController);

  /** @ngInject */
  function CameraSelectController($timeout, $http) {
    var vm = this;

    vm.cameras = [];
    $http.get('/api/camera/').success(function(data){
      vm.cameras = data;
    });

    vm.camera = {
        id: 1,
        description: 'Default'
    }

    vm.getLiveCameraUrl = function(camera_id) {
      return 'api/video/live/' + camera_id;
    }

  }
})();
