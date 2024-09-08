"use client";
import { Button } from "@/components/ui/button";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Bot, Loader2, User } from "lucide-react";
import axios from "axios";
import { useState } from "react";

interface Message {
  role: "user" | "bot";
  content: string;
}

const chatSchema = z.object({
  user_query: z.string().min(1).max(1000),
});

interface ChatContainerProps {
  connection: string;
}

function ChatContainer({ connection }: ChatContainerProps) {
  const [messages, setMessages] = useState<Message[]>([
    { role: "bot", content: "Hello! How can I help you today?" },
  ]);
  const [loading, setLoading] = useState(false);

  const form = useForm<z.infer<typeof chatSchema>>({
    resolver: zodResolver(chatSchema),
    defaultValues: {
      user_query: "",
    },
  });

  async function onSubmit(values: z.infer<typeof chatSchema>) {
    setLoading(true);
    try {
      console.log(values.user_query);
      const response = await axios.post(
        "http://localhost:8000/api/get-response",
        values
      );
      console.log(response.data.response);
      setMessages([
        ...messages,
        { role: "user", content: values.user_query },
        { role: "bot", content: response.data.response },
      ]);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
    form.reset();
  }

  return (
    <div className="flex flex-col justify-between bg-darkSecondary rounded-md p-2 sm:p-4">
      <div className="h-[300px] overflow-y-auto space-y-3 w-full">
        <ul>
          {messages.map((msg, idx) => (
            <li
              key={idx}
              className={`${msg.role === "user" ? "text-right" : "text-left"} flex items-center`}
            >
                <Bot size={24} className={`inline-block ${msg.role === "user" ? "hidden" : ""}`} />
              <span
                className={`${
                  msg.role === "user"
                    ? "bg-gradient-to-br from-amber-300 to to-orange-600 text-transparent bg-clip-text"
                    : "bg-gradient-to-br from-gray-300 to-gray-500 text-transparent bg-clip-text"
                } px-4 py-2 rounded-lg inline-block`}
              >
                {msg.content}
              </span>
              <User size={24} className={`inline-block ${msg.role === "bot" ? "hidden" : ""}`} />
            </li>
          ))}
        </ul>
      </div>
      <div className="pt-4">
        <Form {...form}>
          <form
            onSubmit={form.handleSubmit(onSubmit)}
            className="flex gap-2 sm:gap-4"
          >
            <div className="8 w-full">
              <FormField
                control={form.control}
                name="user_query"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input
                        placeholder="Ask a question to your database"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>
            <Button
              type="submit"
              className="text-lg px-3 py-4 gap-2 bg-gradient-to-br dark:text-white from-amber-300 to to-orange-600 hover:scale-105 transition-all duration-300"
              disabled={loading || !connection}
            >
              Ask
              {!loading && <Bot size={24} className="hover:animate-spin" />}
              {loading && <Loader2 size={24} className="animate-spin" />}
            </Button>
          </form>
        </Form>
      </div>
    </div>
  );
}

export default ChatContainer;
