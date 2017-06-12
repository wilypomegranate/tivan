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

    vm.changeCamera = function() {
      $http.get('/api/camera/' + vm.camera.id + '/').success(function(data) {
        console.log(data);
        vm.hls.loadSource(data.stream_url);
        vm.hls.attachMedia(video);
        vm.hls.on(Hls.Events.MANIFEST_PARSED,function() {
          video.play();
        });
      });
    }

    if(Hls.isSupported()) {
      var video = document.getElementById('live');
      vm.hls = new Hls();
      vm.changeCamera();
    }

  }
})();
