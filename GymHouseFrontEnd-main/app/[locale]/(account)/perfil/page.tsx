import type { Metadata } from "next";
import ProfileP  from "../../../../components/screens/ProfileP";

export const metadata: Metadata = {
    title: "Profile",
    description: "Profile is for people that want to see their profile."
};

export default function profile() {
    return (
        <ProfileP />
    );
}

