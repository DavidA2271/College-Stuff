import * as THREE from 'three';

let camera, scene, renderer, mesh;

function init() {
    //Step 1: Set up a scene
    scene = new THREE.Scene;

    //Step 2: Set up a camera. Perspective Camera.
    camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight, // always usee this
        0.1, //near plane
        1000 //far plane
    );

    //Step 3: Set up a renderer. WebGLRenderer.
    renderer = new THREE.WebGLRenderer(
        { antialias: true } //if canvas is set up this is different
    );

    //Step 4: Set up the size of the renderer
    renderer.setSize(window.innerWidth, window.innerHeight); // use entire browser window

    //Step 5: Add renderer to Canvas element
    document.body.appendChild(renderer.domElement);

    //Step 6: Create geometry
    const geometry = new THREE.SphereGeometry(10, 100, 100);

    //Step 7: Create texture
    const texture = new THREE.TextureLoader().load('resources/earthmap1k.jpg');

    //Step 7.2: Create material with texture
    const material = new THREE.MeshPhongMaterial({ map: texture });

    //Step 8: Create mesh with geometry and material
    mesh = new THREE.Mesh(geometry, material);

    mesh.rotation.x += 0.5;

    //Step 9: Add mesh to scene
    scene.add(mesh);

    //Step 10: Position camera
    camera.position.z = 25;

    //Step 11: Add lights
    let light1 = new THREE.AmbientLight(0xffffff);
    light1.position.set(100, 50, 100);
    scene.add(light1);
}

function animate() {
    requestAnimationFrame(animate);

    mesh.rotation.y += 0.01;

    renderer.render(scene, camera);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

init();
animate();