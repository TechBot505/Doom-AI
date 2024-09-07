import React from "react";
import Link from "next/link";
import { Bot } from "lucide-react";
import { Button } from "@/components/ui/button";

function PDFChat() {
  return (
    <div className="flex flex-col items-center dark:bg-darkPrimary bg-white">
      <div className="relative pt-12 pb-12">
        <div className="relative flex flex-col items-center max-w-screen-xl mx-auto px-8 z-10 text-center">
          <h1 className="bg-gradient-to-br from-amber-300 to to-orange-600 text-transparent bg-clip-text text-2xl md:text-4xl font-bold leading-tight mb-6">
            Chat with PDF Files
          </h1>
          <p className="text-gray-500 dark:text-white text-lg max-w-2xl text-center mb-8">
            Effortlessly chat with your PDF files—extract, explore, and
            understand information in real-time.
          </p>
          <Link href="/dashboard">
            <Button
              type="button"
              className="text-lg px-3 py-4 gap-2 bg-gradient-to-br dark:text-white from-amber-300 to to-orange-600 hover:scale-105 transition-all duration-300"
            >
              Upload
              <Bot size={24} className="hover:animate-spin" />
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default PDFChat;
