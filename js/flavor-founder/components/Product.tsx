import Image from 'next/image';
import Link from 'next/link';

const Product = ({ data }) => {
    if (!data) return null; // Render nothing if no data is provided

    const { product_name, flavor_count, image_path, wiki_link  } = data; // Destructure the required data

    const nonZeroTastes = Object.entries(flavor_count)
    .filter(([key, value]) => value > 0) // Filter out tastes with value 0
    .map(([key, value]) => ({ name: key, value })); // Convert to array of objects

    return (
        <div className="max-w-[1500px] mx-auto px-6 py-10">
            <div className="flex flex-col md:flex-row items-center md:items-start space-y-6 md:space-y-0 md:space-x-10">
                {/* Left Section - Image and Wiki Link */}
                <div className="py-4 px-4 max-w-sm mx-auto space-y-2 bg-white">
                    <div className="">
                        <Image
                            src={image_path}
                            alt="Product"
                            height="300"
                            width="300"
                            className="rounded-lg shadow-lg"
                        />
                    </div>
                    <div className="relative w-60 h-60">
                        {wiki_link && (
                            <Link
                                href={wiki_link}
                            >
                                Learn more on Wikipedia
                            </Link>
                        )}
                    </div>
                </div>

                {/* Right Section - Tastes */}
                <div className="py-4 px-4 max-w-sm mx-auto space-y-2 bg-white">
                    <h2 className="text-2xl font-bold mb-4">{product_name}</h2>
                    {nonZeroTastes.length > 0 ? (
                    <ul className="list-disc list-inside space-y-2">
                        {nonZeroTastes.map((taste, index) => (
                            <li
                                key={index}
                                className="capitalize"
                                style={{
                                    fontSize: `${Math.min(16 + taste.value / 2, 40)}px`, // Dynamically adjust font size
                                }}
                            >
                                {taste.name} ({taste.value})
                            </li>
                        ))}
                    </ul>
            ) : (
                <p>No tastes available</p>
            )}
                </div>
            </div>
        </div>
    );
};

export default Product;
