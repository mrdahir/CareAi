import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout/Layout";
import Home from "./pages/Home";
import ChatPage from "./pages/Chat";
import RecommendPage from "./pages/Recommend";
import MythBusterPage from "./pages/MythBuster";
import About from "./pages/About";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chat" element={<ChatPage />} />
        <Route path="/recommend" element={<RecommendPage />} />
        <Route path="/myth-buster" element={<MythBusterPage />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Layout>
  );
}
