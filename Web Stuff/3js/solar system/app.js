import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

import starsTexture from './img/stars.jpg';
import sunTexture from './img/sun.jpg';
import mercuryTexture from './img/mercury.jpg';
import venusTexture from './img/venus.jpg';
import earthTexture from './img/earth.jpg';
import marsTexture from './img/mars.jpg';
import jupiterTexture from './img/jupiter.jpg';
import saturnTexture from './img/saturn.jpg';
import saturnRingTexture from './img/saturnring.png';
import uranusTexture from './img/uranus.jpg';
import uranusRingTexture from './img/uranusring.png';
import neptuneTexture from './img/neptune.jpg';


const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
    45,
    window.innerWidth / window.innerHeight,
    0.1,
    1000,
);

const orbit = new OrbitControls(camera, renderer.domElement);

camera.position.set(-90, 140, 140);
orbit.update();

const ambientLight = new THREE.AmbientLight(0x333333, 5)
scene.add(ambientLight)

const pointLight = new THREE.PointLight(0xFFFFFF, 10000, 0, 2)
scene.add(pointLight)

const cubeTextureLoader = new THREE.CubeTextureLoader();

scene.background = cubeTextureLoader.load([
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture
]);

const textureLoader = new THREE.TextureLoader();

//add the sun
const sunGeometry = new THREE.SphereGeometry(16, 30, 30);
const sunMaterial = new THREE.MeshBasicMaterial({
    map: textureLoader.load(sunTexture)
});

const sun = new THREE.Mesh(sunGeometry, sunMaterial);

scene.add(sun);

//add mercury
const mercuryGeometry = new THREE.SphereGeometry(3, 30, 30);
const mercuryMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(mercuryTexture)
});

const mercury = new THREE.Mesh(mercuryGeometry, mercuryMaterial);

const mercuryObj = new THREE.Object3D();
mercuryObj.add(mercury);

scene.add(mercuryObj);

mercury.position.x = 30;

//add venus
const venusGeometry = new THREE.SphereGeometry(6, 30, 30);
const venusMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(venusTexture)
});

const venus = new THREE.Mesh(venusGeometry, venusMaterial);

const venusObj = new THREE.Object3D();
venusObj.add(venus);

scene.add(venusObj);

venus.position.x = 50;

//add the earth
const earthGeometry = new THREE.SphereGeometry(6, 30, 30);
const earthMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(earthTexture)
});

const earth = new THREE.Mesh(earthGeometry, earthMaterial);

const earthObj = new THREE.Object3D();
earthObj.add(earth);

scene.add(earthObj);

earth.position.x = 70;

//add mars
const marsGeometry = new THREE.SphereGeometry(3, 30, 30);
const marsMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(marsTexture)
});

const mars = new THREE.Mesh(marsGeometry, marsMaterial);

const marsObj = new THREE.Object3D();
marsObj.add(mars);

scene.add(marsObj);

mars.position.x = 90;

//add jupiter
const jupiterGeometry = new THREE.SphereGeometry(10, 30, 30);
const jupiterMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(jupiterTexture)
});

const jupiter = new THREE.Mesh(jupiterGeometry, jupiterMaterial);

const jupiterObj = new THREE.Object3D();
jupiterObj.add(jupiter);

scene.add(jupiterObj);

jupiter.position.x = 120;

//add Saturn
const saturnGeometry = new THREE.SphereGeometry(10, 30, 30);
const saturnMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(saturnTexture)
});

const saturn = new THREE.Mesh(saturnGeometry, saturnMaterial);

const saturnObj = new THREE.Object3D();
saturnObj.add(saturn);

scene.add(saturnObj);

saturn.position.x = 170;


//add Saturn rings
const saturnRingGeometry = new THREE.RingGeometry(10, 20, 32);
const saturnRingMaterial = new THREE.MeshBasicMaterial({
    map: textureLoader.load(saturnRingTexture),
    side: THREE.DoubleSide
});

const saturnRing = new THREE.Mesh(saturnRingGeometry, saturnRingMaterial);

saturnObj.add(saturnRing);
saturnRing.position.x = 170;
saturnRing.rotation.x = -0.5 * Math.PI;

//add uranus
const uranusGeometry = new THREE.SphereGeometry(8, 30, 30);
const uranusMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(uranusTexture)
});

const uranus = new THREE.Mesh(uranusGeometry, uranusMaterial);

const uranusObj = new THREE.Object3D();
uranusObj.add(uranus);

scene.add(uranusObj);

uranus.position.x = 220;

//add uranus rings
const uranusRingGeometry = new THREE.RingGeometry(8, 15, 32);
const uranusRingMaterial = new THREE.MeshBasicMaterial({
    map: textureLoader.load(uranusRingTexture),
    side: THREE.DoubleSide
});

const uranusRing = new THREE.Mesh(uranusRingGeometry, uranusRingMaterial);

uranusObj.add(uranusRing);
uranusRing.position.x = 220;
uranusRing.rotation.x = -0.5 * Math.PI;

//add neptune
const neptuneGeometry = new THREE.SphereGeometry(8, 30, 30);
const neptuneMaterial = new THREE.MeshStandardMaterial({
    map: textureLoader.load(neptuneTexture)
});

const neptune = new THREE.Mesh(neptuneGeometry, neptuneMaterial);

const neptuneObj = new THREE.Object3D();
neptuneObj.add(neptune);

scene.add(neptuneObj);

neptune.position.x = 260;

function animate() {
    renderer.render(scene, camera);

    // rotating
    sun.rotateY(0.005);

    //for all planets
    mercury.rotateY(0.00068);
    mercuryObj.rotateY(0.05);

    venus.rotateY(0.0008);
    venusObj.rotateY(0.035);

    earth.rotateY(0.002);
    earthObj.rotateY(0.02);

    mars.rotateY(0.014);
    marsObj.rotateY(0.012);

    jupiter.rotateY(0.026);
    jupiterObj.rotateY(0.009);

    saturn.rotateY(0.038);
    saturnObj.rotateY(0.0065);

    uranus.rotateY(0.05);
    uranusObj.rotateY(0.003);

    neptune.rotateY(0.062);
    neptuneObj.rotateY(0.0009);
}

renderer.setAnimationLoop(animate);

window.addEventListener('resize', function () {
    camera.aspect = window.innerWidth / this.window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});