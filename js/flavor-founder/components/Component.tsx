'use client'

import { useState } from "react";
import { Button } from "./ui/button";
import { Input } from "@/components/ui/input";

const fetchData = async (productName) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/get_flavors?product=${encodeURIComponent(productName)}`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching search results:", error);
        throw error;
    }
};

const LandingContent = ({ onSearchComplete }) => {
    const [inputValue, setInputValue] = useState("");

    const handleSearch = () => {
        if (!inputValue.trim()) {
            alert("Please enter a product name!");
            return;
        }

        fetchData(inputValue)
            .then((data) => {
                console.log("Search Results:", data);
                onSearchComplete(data); // Pass data back to parent
            })
            .catch(() => {
                alert("An error occurred while fetching the search results.");
            });
    };

    return (
        <div className="flex flex-col items-center">
            <h1 className="text-5xl font-bold tracking-[-3px] text-center">
                What flavours your product consist of?
            </h1>
            <div className="mt-5 text-base font-medium text-center text-zinc-500">
                Type the name of the product to find out!
            </div>
            <div className="flex items-center justify-center w-full max-w-sm space-x-2 mt-5">
                <Input 
                    placeholder="Lemon" 
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)} 
                />
                <Button onClick={handleSearch}>Search</Button>
            </div>
        </div>
    );
};

export default LandingContent;
