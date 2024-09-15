const updateUserTimeZone = async () => {
    const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    try {
        const response = await fetch('/update-timezone', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ timeZone: userTimeZone })
        });

        if (response.ok) {
            console.log('Time zone updated successfully');
        } else {
            console.log('Failed to update time zone');
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

// 自动执行更新时区
updateUserTimeZone();
