import ThemeToggle from "@/components/custom/ThemeToggle";
import { Menu, Search } from "lucide-react";
import React from "react";

interface PROPS {
  setShowSidebar: (value: boolean) => void;
}

function Header({ setShowSidebar }: PROPS) {
  return (
    <div className="p-5 shadow-sm border-b-2 flex flex-row gap-3 dark:bg-darkSecondary bg-white justify-between items-center">
      <div className="lg:hidden">
        <Menu
          size={32}
          onClick={() => {
            setShowSidebar(true);
          }}
        />
      </div>
      <div className="sm:flex sm:flex-row hidden dark:bg-gray-700 gap-2 items-center p-2 border rounded-full max-w-lg">
        <Search size={24} />
        <input
          type="text"
          placeholder="Search..."
          className="dark:text-white dark:bg-gray-700 border-none outline-none"
        />
      </div>
      <div className="flex gap-5 items-center">
        <ThemeToggle />
      </div>
    </div>
  );
}

export default Header;
