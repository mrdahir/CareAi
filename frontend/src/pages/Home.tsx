import { Link } from "react-router-dom";
import { MessageCircle, Sparkles, Shield } from "lucide-react";
import Card from "../components/Common/Card";
import Button from "../components/Common/Button";
import ProgrammeStats from "../components/Common/ProgrammeStats";
import { useT } from "../i18n/useT";

export default function Home() {
  const tr = useT();
  const features = [
    {
      to: "/chat",
      icon: MessageCircle,
      title: tr("home.feature.chat.title"),
      desc: tr("home.feature.chat.desc"),
    },
    {
      to: "/recommend",
      icon: Sparkles,
      title: tr("home.feature.recommend.title"),
      desc: tr("home.feature.recommend.desc"),
    },
    {
      to: "/myth-buster",
      icon: Shield,
      title: tr("home.feature.myth.title"),
      desc: tr("home.feature.myth.desc"),
    },
  ];

  return (
    <div className="space-y-8">
      <section className="text-center py-8">
        <h1 className="text-3xl font-bold text-care-900 sm:text-4xl">
          {tr("home.title")}
        </h1>
        <p className="mt-3 text-gray-600 max-w-xl mx-auto">{tr("home.subtitle")}</p>
        <Link to="/chat" className="inline-block mt-6">
          <Button>{tr("home.cta")}</Button>
        </Link>
      </section>
      <div className="grid gap-4 sm:grid-cols-3">
        {features.map((f) => (
          <Link key={f.to} to={f.to}>
            <Card className="h-full hover:border-care-300 transition">
              <f.icon className="h-8 w-8 text-care-600 mb-2" aria-hidden />
              <h2 className="font-semibold text-care-800">{f.title}</h2>
              <p className="text-sm text-gray-600 mt-1">{f.desc}</p>
            </Card>
          </Link>
        ))}
      </div>
      <ProgrammeStats />
    </div>
  );
}
