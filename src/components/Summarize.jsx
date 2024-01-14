import React, { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";

import { styles } from "../styles";
import { summaryTypes } from "../constants";
import { useSummary } from "../contexts";

const Summarize = () => {
    const myRef = useRef(null);
    const scrollToRef = (ref) => window.scrollTo(0, ref.current.offsetTop);
    const executeScroll = () => scrollToRef(myRef);

    const { setSummary } = useSummary();

    const [url, setUrl] = useState("");
    const [startTime, setStartTime] = useState("");
    const [endTime, setEndTime] = useState("");
    const [wordCount, setWordCount] = useState("");
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [summaryType, setSummaryType] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        setSummary(""); // Reset summary for new request

        try {
            const response = await fetch("http://localhost:5000/get-summary", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    url,
                    startTime,
                    endTime,
                    wordCount,
                }),
            });

            const data = await response.json();
            if (data) {
                setSummary(data);
                executeScroll();
            }
            // Handle other response data or errors as needed
        } catch (error) {
            console.error("Error:", error);
            // Handle error (e.g., display an error message)
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className="pt-[30vh] p-4 w-[55vw] mx-auto min-h-screen">
            <h2 class={`text-[40px] font-light text-center mt-10 mb-5`}>
                Create a video summary in one click
            </h2>
            <form
                onSubmit={handleSubmit}
                class="flex flex-col gap-5 items-center"
            >
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter YouTube URL"
                    className="p-2 border border-gray-300 rounded-2xl w-full"
                />
                <div class="flex justify-between space-x-5">
                    <input
                        type="text"
                        value={startTime}
                        onChange={(e) => setStartTime(e.target.value)}
                        placeholder="Start Time (e.g., 00:00)"
                        className="p-2 border border-gray-300 rounded-2xl w-1/4"
                    />
                    <input
                        type="text"
                        value={endTime}
                        onChange={(e) => setEndTime(e.target.value)}
                        placeholder="End Time (e.g., 10:00)"
                        className="p-2 border border-gray-300 rounded-2xl w-1/4"
                    />
                    <input
                        type="number"
                        value={wordCount}
                        onChange={(e) => setWordCount(e.target.value)}
                        placeholder="Word Count"
                        className="p-2 border border-gray-300 rounded-2xl w-1/4"
                    />
                    <select
                        value={summaryType}
                        onChange={(e) => setSummaryType(e.target.value)}
                        className={`p-2 border border-gray-300 rounded-2xl w-1/4 ${
                            summaryType === "" ? "text-gray-200" : "black"
                        }`}
                    >
                        <option value="">Summary type</option>
                        {summaryTypes.map((type, index) => (
                            <option key={index} value={type.value}>
                                {type.label}
                            </option>
                        ))}
                    </select>
                </div>
                <button
                    type="submit"
                    className={`p-2 w-[120px] text-white rounded-2xl ${
                        isSubmitting
                            ? "bg-gray-500"
                            : "bg-blue-500 hover:bg-blue-600"
                    }`}
                    disabled={isSubmitting}
                >
                    {isSubmitting
                        ? "Submitting..."
                        : "summary"
                        ? "Regenerate"
                        : "Submit"}
                </button>
            </form>
        </div>
    );
};

export default Summarize;
