(function() {
  'use strict';

  angular
    .module('materialUi')
    .controller('CameraController', CameraController)
    .directive('livevideo', LiveVideo)
  ;

  function LiveVideo($http) {
    return {
      link: function(scope, elem) {
        $http.get('/api/camera/' + scope.camera.id + '/').success(function(data){
          let stream_url = data.stream_url;
          let video = elem[0];
          if(Hls.isSupported()) {
            let hls = new Hls();
            hls.loadSource(stream_url);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED,function() {
              video.play();
            });
          }
        });
      }
    }
  }

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
