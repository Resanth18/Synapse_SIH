
import "@fontsource/inter";


// WebGL capability check
function checkWebGLSupport() {
  try {
    const canvas = document.createElement("canvas");
    const gl =
      canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    return !!gl;
  } catch (e) {
    return false;
  }
}

// Control keys for camera movement
const controls = [
  { name: "forward", keys: ["KeyW", "ArrowUp"] },
  { name: "backward", keys: ["KeyS", "ArrowDown"] },
  { name: "leftward", keys: ["KeyA", "ArrowLeft"] },
  { name: "rightward", keys: ["KeyD", "ArrowRight"] },
  { name: "up", keys: ["KeyQ"] },
  { name: "down", keys: ["KeyE"] },
];

const queryClient = new QueryClient();
const store = createXRStore();

function App() {
  const [webglSupported, setWebglSupported] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!checkWebGLSupport()) {
      setWebglSupported(false);
      setError(
        "WebGL is not supported in your browser. Please enable WebGL or use a modern browser."
      );
    }
  }, []);

  }

  return (
    <QueryClientProvider client={queryClient}>
      <div
        style={{
          width: "100vw",
          height: "100vh",
          position: "relative",
          overflow: "hidden",
        }}
      >
        <KeyboardControls map={controls}>
          {/* WebXR VR Button */}
          <div style={{ position: "absolute", top: 10, right: 10, zIndex: 1000 }}>
            <VRButton store={store} />
          </div>

          {/* 3D Canvas */}
          <Canvas
            shadows
            camera={{
              position: [0, 15, 25],
              fov: 60,
              near: 0.1,
              far: 1000,
            }}
            gl={{
              antialias: true,
              powerPreference: "high-performance",
              alpha: false,
            }}
            onCreated={() => {
              console.log("WebGL context created successfully");
            }}
          >
            <XR store={store}>
              <color attach="background" args={["#87CEEB"]} />
              <Suspense fallback={null}>
                <FarmScene />
              </Suspense>
              <Stats />
            </XR>
          </Canvas>

          {/* UI Overlay */}
          <FarmUI />
        </KeyboardControls>
      </div>
    </QueryClientProvider>
  );


export default App;
