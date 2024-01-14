import React, { useState } from "react";

const YouTubeURLInput = () => {
    const [url, setUrl] = useState("");
    const [startTime, setStartTime] = useState("");
    const [endTime, setEndTime] = useState("");
    const [wordCount, setWordCount] = useState("");
    const [summary, setSummary] = useState("");
    const [isSubmitting, setIsSubmitting] = useState(false);

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
            if (data.summary) {
                setSummary(data.summary);
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
        <div className="mt-[100px] min-h-screen p-4 w-[60vw] mx-auto">
            <form onSubmit={handleSubmit} className="flex flex-col gap-2">
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter YouTube URL"
                    className="p-2 border border-gray-300 rounded"
                />
                <input
                    type="text"
                    value={startTime}
                    onChange={(e) => setStartTime(e.target.value)}
                    placeholder="Start Time (e.g., 00:00:00)"
                    className="p-2 border border-gray-300 rounded"
                />
                <input
                    type="text"
                    value={endTime}
                    onChange={(e) => setEndTime(e.target.value)}
                    placeholder="End Time (e.g., 00:10:00)"
                    className="p-2 border border-gray-300 rounded"
                />
                <input
                    type="number"
                    value={wordCount}
                    onChange={(e) => setWordCount(e.target.value)}
                    placeholder="Word Count"
                    className="p-2 border border-gray-300 rounded"
                />
                <button
                    type="submit"
                    className={`p-2 text-white rounded ${
                        isSubmitting
                            ? "bg-gray-500"
                            : "bg-blue-500 hover:bg-blue-600"
                    }`}
                    disabled={isSubmitting}
                >
                    {isSubmitting ? "Submitting..." : "Submit"}
                </button>
            </form>
            {summary && (
                <div className="mt-4 p-4 bg-gray-800 rounded">{summary}</div>
            )}
        </div>
    );
};

export default YouTubeURLInput;
