import React from "react";

import { useSummary } from "../contexts";

const Summary = () => {
    const { summary } = useSummary();

    return (
        <div ref="summary" class="w-[55vw] items-center mx-auto min-h-screen">
            {summary && (
                <>
                    <a href={summary.url}>
                        <h3 class="text-center text-[20px] font-semibold m-5">
                            {summary.title}
                        </h3>
                    </a>
                    <div className="mt-4 p-4 bg-gray-500 rounded-2xl">
                        {summary.text}
                    </div>
                </>
            )}
        </div>
    );
};

export default Summary;
