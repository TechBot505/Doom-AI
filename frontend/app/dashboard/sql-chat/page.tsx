"use client";
import React, { useState } from "react";
import UploadForm from "@/components/custom/UploadForm";
import ChatContainer from "@/components/custom/ChatContainer";
import { Bot } from "lucide-react";

function SQLChat() {
  const [connection, setConnection] = useState<string>("");

  return (
    <div className="flex flex-col items-center dark:bg-darkPrimary bg-white gap-2">
      <div className="relative pt-12">
        <div className="relative flex flex-col items-center max-w-screen-xl mx-auto px-8 text-center">
          <h1 className="bg-gradient-to-br from-amber-300 to to-orange-600 text-transparent bg-clip-text text-2xl md:text-4xl font-bold leading-tight mb-6">
            Chat with MySQL Database
          </h1>
          <p className="text-gray-500 dark:text-white text-lg max-w-2xl text-center mb-8">
            Seamlessly chat with your SQL databases—query, analyze, and
            visualize data in real-time.
          </p>
        </div>
      </div>
      <div className="w-full sm:px-16 px-8 py-4 mb-2">
        <UploadForm setConnection={setConnection} />
      </div>
      {connection && (
        <div className="bg-green-300 px-4 py-1 mx-4 rounded-md mb-4">
          <p className="text-gray-900 text-sm">{connection}</p>
        </div>
      )}
      <div className="flex flex-col gap-4 w-full sm:px-16 px-8 rounded-full mb-4">
        <div className="flex gap-2 items-center">
          <h1 className="text-2xl font-bold ">Start Chatting</h1>
          <Bot size={28}/>
        </div>
        <ChatContainer connection={connection} />
      </div>
    </div>
  );
}

export default SQLChat;
