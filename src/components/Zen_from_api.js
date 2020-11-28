import React, {useEffect, useState} from "react";
import {useAuth0} from "@auth0/auth0-react";

const ZenFromApi = () => {
    const {isAuthenticated, getAccessTokenSilently} = useAuth0();
    const [currentZenSec, setCurrentZenSec] = useState("");


    useEffect(() => {
        const getZenSec = async () => {

            try {
                const accessToken = await getAccessTokenSilently();

                fetch('/api/zensec',
                    {
                        headers: {
                            Authorization: `Bearer ${accessToken}`,
                        },
                    }).then(res => res.json()).then(data => {
                    setCurrentZenSec(data.zensec);
                });

            } catch (e) {
                console.log(e.message);
            }
        };

        getZenSec();

    }, [getAccessTokenSilently]);

    return (
        isAuthenticated && (
            <p>Random Python Zen from secure API: {currentZenSec}</p>
        )
    );
};

export default ZenFromApi;
