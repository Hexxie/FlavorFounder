'use client'

import { useState } from "react";
import LandingContent from "@/components/Component";
import Product from "@/components/Product";

export default function Home() {
    const [showProduct, setShowProduct] = useState(false);
    const [productData, setProductData] = useState(null);

    const handleProductDisplay = (data) => {
        setProductData(data);
        setShowProduct(true);
    };

    return (
        <main className="flex flex-col items-center justify-center min-h-screen">
            <LandingContent onSearchComplete={handleProductDisplay} />
            {showProduct && <Product data={productData} />}
        </main>
    );
}
